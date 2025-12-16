from Test_repo28.endpoints.base import BaseClient


class GetMemeAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    def list_memes(self):
        return self.client.get("/meme")
