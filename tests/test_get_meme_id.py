def test_get_meme(created_meme, get_meme_id_api):
    meme_id, _ = created_meme

    get_meme_id_api.get_meme(meme_id)
    get_meme_id_api.assert_status_code(200)
    get_meme_id_api.assert_meme_id(meme_id)

