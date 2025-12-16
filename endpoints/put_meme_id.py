from Test_repo28.endpoints.base import BaseClient


class PutMemeByIdAPI:
    def __init__(self, client: BaseClient):
        self.client = client

    def update_meme(self, meme_id: int, text: str, url: str, tags: list, info: dict):
        body = {
            "id": meme_id,
            "text": text,
            "url": url,
            "tags": tags,
            "info": info,
        }
        return self.client.put(f"/meme/{meme_id}", json=body)
