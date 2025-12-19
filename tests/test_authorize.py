from Test_repo28.endpoints.base import BaseClient


def test_authorize_with_valid_name(auth_api):
    resp = auth_api.create_token("test_user")
    BaseClient.assert_status_code(resp, 200)

    body = resp.json()
    BaseClient.assert_token_response(body)


def test_authorize_with_empty_name(auth_api):
    resp = auth_api.create_token("")
    BaseClient.assert_status_code(resp, 200)

    body = resp.json()
    BaseClient.assert_token_response(body)


def test_token_is_alive(auth_api):
    create_resp = auth_api.create_token("alive_user")
    token = create_resp.json()["token"]

    check_resp = auth_api.token_is_alive(token)
    BaseClient.assert_status_code(check_resp, 200)