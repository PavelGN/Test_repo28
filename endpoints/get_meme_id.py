from Test_repo28.endpoints.base import BaseClient


class GetMemeByIdAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_meme(self, meme_id: int):
        return self.client.get(f"/meme/{meme_id}")
