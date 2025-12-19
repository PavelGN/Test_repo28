from Test_repo28.endpoints.base import BaseClient


def test_get_meme(created_meme, get_meme_id_api):
    meme_id, _ = created_meme

    get_resp = get_meme_id_api.get_meme(meme_id)
    BaseClient.assert_status_code(get_resp, 200)
