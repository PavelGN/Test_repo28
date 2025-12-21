def test_authorize_with_valid_name(auth_api):
    auth_api.create_token("test_user")

    auth_api.client.assert_status_code(200)
    auth_api.assert_token_response()


def test_authorize_with_empty_name(auth_api):
    auth_api.create_token("")

    auth_api.client.assert_status_code(200)
    auth_api.assert_token_response()


def test_token_is_alive(auth_api):
    auth_api.create_token("alive_user")
    auth_api.client.assert_status_code(200)

    token = auth_api.client.response.json()["token"]

    auth_api.token_is_alive(token)
    auth_api.client.assert_status_code(200)
