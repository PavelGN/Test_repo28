from Test_repo28.endpoints.base import BaseClient


class GetMemeAPI(BaseClient):

    def list_memes(self):
        self.get("/meme")
        return self.response

    def check_response_contains_data(self):
        body = self.response.json()
        assert "data" in body, "Response has no 'data' field"
        assert isinstance(body["data"], list), "'data' is not a list"

    def assert_meme_in_list(self, meme_id: int):
        body = self.response.json()
        ids = [meme["id"] for meme in body["data"]]
        assert meme_id in ids, "Meme with given id not found in list"
