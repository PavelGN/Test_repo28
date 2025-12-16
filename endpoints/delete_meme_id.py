from Test_repo28.endpoints.base import BaseClient


class DeleteMemeByIdAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    def delete_meme(self, meme_id: int):
        return self.client.delete(f"/meme/{meme_id}")
