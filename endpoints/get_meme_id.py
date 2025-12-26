from Test_repo28.endpoints.base import BaseClient


class GetMemeByIdAPI(BaseClient):

    def get_meme(self, meme_id: int):
        self.get(f"/meme/{meme_id}")
        return self.response

    def assert_meme_id(self, expected_id: int):
        body = self.response.json()
        assert body["id"] == expected_id, (
            "Returned meme ID does not match requested ID"
        )

