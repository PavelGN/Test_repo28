from Test_repo28.endpoints.base import BaseClient


class DeleteMemeByIdAPI(BaseClient):

    def delete_meme(self, meme_id: int):
        self.delete(f"/meme/{meme_id}")
        return self.response
