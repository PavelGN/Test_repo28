from Test_repo28.endpoints.base import BaseClient


def test_delete_meme(created_meme, delete_meme_id_api, get_meme_id_api):
    meme_id, _ = created_meme

    delete_resp = delete_meme_id_api.delete_meme(meme_id)
    BaseClient.assert_status_code(delete_resp, 200)

    get_resp = get_meme_id_api.get_meme(meme_id)
    BaseClient.assert_status_code(get_resp, 404)
