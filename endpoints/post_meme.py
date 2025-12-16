from Test_repo28.endpoints.base import BaseClient


class PostMemeAPI:


    def __init__(self, client: BaseClient):
        self.client = client

    def create_meme(self, text: str, url: str, tags: list, info: dict):
        body = {
            "text": text,
            "url": url,
            "tags": tags,
            "info": info
        }
        return self.client.post("/meme", json=body)
