import pytest
import requests
from Test_repo28.data.data import generate_meme_payload

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

    auth_api.create_token("pytest_user")
    base_client.assert_status_code(200)
    auth_api.assert_token_response()

    token = base_client.response.json()["token"]

    auth_api.token_is_alive(token)
    base_client.assert_status_code(200)

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
def created_meme(post_meme_api, delete_meme_id_api):
    payload = generate_meme_payload()

    post_meme_api.create_meme(
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )
    post_meme_api.client.assert_status_code(200)

    meme_id = post_meme_api.client.response.json()["id"]

    yield meme_id, payload

    delete_meme_id_api.delete_meme(meme_id)


@pytest.fixture
def auth_api(base_client):
    return AuthorizationAPI(base_client)


@pytest.fixture
def unauth_base_client():
    session = requests.Session()
    client = BaseClient(BASE_URL, session)
    yield client
    session.close()


@pytest.fixture
def unauth_post_meme_api(unauth_base_client):
    return PostMemeAPI(unauth_base_client)


@pytest.fixture
def unauth_get_meme_api(unauth_base_client):
    return GetMemeAPI(unauth_base_client)


@pytest.fixture
def unauth_get_meme_id_api(unauth_base_client):
    return GetMemeByIdAPI(unauth_base_client)


@pytest.fixture
def unauth_put_meme_id_api(unauth_base_client):
    return PutMemeByIdAPI(unauth_base_client)


@pytest.fixture
def unauth_delete_meme_id_api(unauth_base_client):
    return DeleteMemeByIdAPI(unauth_base_client)
