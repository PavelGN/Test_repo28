def test_list_memes_contains_created_meme(created_meme, get_meme_api):
    meme_id, _ = created_meme

    get_meme_api.list_memes()
    get_meme_api.client.assert_status_code(200)
    get_meme_api.assert_memes_list_response()
    get_meme_api.assert_meme_in_list(meme_id)
