from Test_repo28.endpoints.base import BaseClient


class AuthorizationAPI(BaseClient):
    """
    POST /authorize
    GET  /authorize/<token>
    """

    def create_token(self, name: str):
        body = {"name": name}
        self.post("/authorize", json=body)
        return self.response

    def token_is_alive(self, token: str):
        self.get(f"/authorize/{token}")
        return self.response

    def check_token_is_in_response(self):
        body = self.response.json()
        assert "token" in body, "Response has no 'token'"
        assert body["token"], "Token is empty"
