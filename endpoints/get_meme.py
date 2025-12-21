from Test_repo28.endpoints.base import BaseClient


class GetMemeAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    def list_memes(self):
        return self.client.get("/meme")

    def assert_memes_list_response(self):
        body = self.client.response.json()
        assert "data" in body
        assert isinstance(body["data"], list)

    def assert_meme_in_list(self, meme_id: int):
        body = self.client.response.json()
        ids = [meme["id"] for meme in body["data"]]
        assert meme_id in ids