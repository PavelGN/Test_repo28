from Test_repo28.endpoints.base import BaseClient


def test_list_memes_contains_created_meme(created_meme, get_meme_api):
    meme_id, _ = created_meme

    list_resp = get_meme_api.list_memes()
    BaseClient.assert_status_code(list_resp, 200)

    body = list_resp.json()

    BaseClient.assert_memes_list_response(body)
    BaseClient.assert_meme_in_list(body["data"], meme_id)

