from typing import Optional
from requests import Response

from Test_repo28.endpoints.base import BaseClient


class AuthorizationAPI:
    """
    Класс для работы с авторизацией API:
      - POST /authorize
      - GET  /authorize/<token>
    """

    def __init__(self, client: BaseClient):
        self.client = client

    def create_token(self, name: str) -> Response:
        """
        Создаёт новый токен.
        POST /authorize
        Тело: {"name": "<name>"}
        """
        body = {"name": name}
        return self.client.post("/authorize", json=body)

    def token_is_alive(self, token: str) -> Optional[Response]:
        """
        Проверяет, жив ли токен.
        GET /authorize/<token>
        Если token пустой — возвращает None.
        """
        if not token:
            return None

        return self.client.get(f"/authorize/{token}")

    def assert_token_response(self):
        body = self.client.response.json()
        assert "token" in body
        assert body["token"]
