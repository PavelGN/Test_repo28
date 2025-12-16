def test_get_meme(created_meme, get_meme_id_api):
    get_resp = get_meme_id_api.get_meme(created_meme)
    assert get_resp.status_code == 200