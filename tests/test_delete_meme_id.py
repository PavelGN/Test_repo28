def test_delete_meme(created_meme, delete_meme_id_api, get_meme_id_api):
    meme_id, _ = created_meme

    delete_meme_id_api.delete_meme(meme_id)
    delete_meme_id_api.client.assert_status_code(200)

    get_meme_id_api.get_meme(meme_id)
    get_meme_id_api.client.assert_status_code(404)
