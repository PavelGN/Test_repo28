from Test_repo28.endpoints.base import BaseClient


class GetMemeByIdAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_meme(self, meme_id: int):
        return self.client.get(f"/meme/{meme_id}")

    def assert_meme_equals(self, expected: dict):
        body = self.client.response.json()
        assert body["text"] == expected["text"]
        assert body["url"] == expected["url"]
        assert body["tags"] == expected["tags"]
        assert body["info"] == expected["info"]

    def assert_meme_id(self, expected_id: int):
        body = self.client.response.json()
        assert body["id"] == expected_id, "Returned meme ID does not match requested ID"
