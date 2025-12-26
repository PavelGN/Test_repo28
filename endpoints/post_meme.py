from Test_repo28.endpoints.base import BaseClient


class PostMemeAPI(BaseClient):

    def create_meme(self, text: str, url: str, tags: list, info: dict):
        body = {
            "text": text,
            "url": url,
            "tags": tags,
            "info": info,
        }
        self.post("/meme", json=body)
        return self.response

    def assert_meme_created(self):
        body = self.response.json()
        assert "id" in body, "Response has no 'id'"
        assert isinstance(body["id"], int), "'id' is not int"
        return body["id"]
