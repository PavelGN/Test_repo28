from Test_repo28.endpoints.base import BaseClient


class PutMemeByIdAPI(BaseClient):

    def update_meme(
        self,
        meme_id: int,
        text: str,
        url: str,
        tags: list,
        info: dict,
    ):
        body = {
            "id": meme_id,
            "text": text,
            "url": url,
            "tags": tags,
            "info": info,
        }
        self.put(f"/meme/{meme_id}", json=body)
        return self.response
