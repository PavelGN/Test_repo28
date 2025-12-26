import pytest
import requests

from Test_repo28.data.data import generate_meme_payload
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
def auth_token(session):
    auth_api = AuthorizationAPI(BASE_URL, session)

    auth_api.create_token("pytest_user")
    auth_api.assert_status_code(200)
    auth_api.check_token_is_in_response()

    token = auth_api.response.json()["token"]

    auth_api.token_is_alive(token)
    auth_api.assert_status_code(200)

    session.headers.update({"Authorization": token})
    return token



@pytest.fixture
def post_meme_api(session, auth_token):
    return PostMemeAPI(BASE_URL, session)


@pytest.fixture
def get_meme_api(session, auth_token):
    return GetMemeAPI(BASE_URL, session)


@pytest.fixture
def get_meme_id_api(session, auth_token):
    return GetMemeByIdAPI(BASE_URL, session)


@pytest.fixture
def put_meme_id_api(session, auth_token):
    return PutMemeByIdAPI(BASE_URL, session)


@pytest.fixture
def delete_meme_id_api(session, auth_token):
    return DeleteMemeByIdAPI(BASE_URL, session)



@pytest.fixture
def created_meme(post_meme_api, delete_meme_id_api):
    payload = generate_meme_payload()

    post_meme_api.create_meme(
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )
    post_meme_api.assert_status_code(200)
    meme_id = post_meme_api.assert_meme_created()

    yield meme_id, payload

    delete_meme_id_api.delete_meme(meme_id)



@pytest.fixture
def unauth_session():
    s = requests.Session()
    yield s
    s.close()


@pytest.fixture
def unauth_post_meme_api(unauth_session):
    return PostMemeAPI(BASE_URL, unauth_session)


@pytest.fixture
def unauth_get_meme_api(unauth_session):
    return GetMemeAPI(BASE_URL, unauth_session)


@pytest.fixture
def unauth_get_meme_id_api(unauth_session):
    return GetMemeByIdAPI(BASE_URL, unauth_session)


@pytest.fixture
def unauth_put_meme_id_api(unauth_session):
    return PutMemeByIdAPI(BASE_URL, unauth_session)


@pytest.fixture
def unauth_delete_meme_id_api(unauth_session):
    return DeleteMemeByIdAPI(BASE_URL, unauth_session)


@pytest.fixture
def auth_api(session):
    return AuthorizationAPI(BASE_URL, session)
