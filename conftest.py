import pytest
import requests
import random
import string

from Test_repo28.endpoints.base import BaseClient
from Test_repo28.endpoints.authorize import AuthorizationAPI
from Test_repo28.endpoints.post_meme import PostMemeAPI
from Test_repo28.endpoints.get_meme import GetMemeAPI
from Test_repo28.endpoints.get_meme_id import GetMemeByIdAPI
from Test_repo28.endpoints.put_meme_id import PutMemeByIdAPI
from Test_repo28.endpoints.delete_meme_id import DeleteMemeByIdAPI


BASE_URL = "http://memesapi.course.qa-practice.com"


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    yield s
    s.close()


@pytest.fixture(scope="session")
def base_client(session):
    return BaseClient(BASE_URL, session)


@pytest.fixture(scope="session")
def auth_token(base_client):
    auth_api = AuthorizationAPI(base_client)

    # Если токена нет или он мёртв — создаём новый
    resp = auth_api.create_token("pytest_user")
    assert resp.status_code == 200, (
        "Не удалось создать токен: "
        f"{resp.text}"
    )
    token = resp.json().get("token")
    assert token, "В ответе авторизации нет поля 'token'"

    # Проверка, что токен живой
    alive = auth_api.token_is_alive(token)
    assert alive.status_code == 200, "Полученный токен не работает"

    # Устанавливаем токен
    base_client.set_auth_token(token)

    return token


@pytest.fixture
def post_meme_api(base_client, auth_token):
    return PostMemeAPI(base_client)


@pytest.fixture
def get_meme_api(base_client, auth_token):
    return GetMemeAPI(base_client)


@pytest.fixture
def get_meme_id_api(base_client, auth_token):
    return GetMemeByIdAPI(base_client)


@pytest.fixture
def put_meme_id_api(base_client, auth_token):
    return PutMemeByIdAPI(base_client)


@pytest.fixture
def delete_meme_id_api(base_client, auth_token):
    return DeleteMemeByIdAPI(base_client)


@pytest.fixture
def meme_payload():
    text = "test-" + "".join(random.choices(string.ascii_letters, k=6))
    url = (
        "https://www.boredpanda.com/blog/wp-content/uploads/2022/09/"
        "it-humor-and-memes-204-632853f7bbbad__700.jpg"
    )
    tags = ["funny", "test"]
    info = {"meta": random.randint(1, 100)}

    return {
        "text": text,
        "url": url,
        "tags": tags,
        "info": info,
    }


@pytest.fixture
def created_meme(post_meme_api, delete_meme_id_api, meme_payload):
    resp = post_meme_api.create_meme(
        text=meme_payload["text"],
        url=meme_payload["url"],
        tags=meme_payload["tags"],
        info=meme_payload["info"],
    )
    assert resp.status_code == 200, resp.text

    meme_id = resp.json()["id"]

    yield meme_id

    delete_meme_id_api.delete_meme(meme_id)
