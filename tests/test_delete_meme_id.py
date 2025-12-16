def test_delete_meme(post_meme_api, delete_meme_id_api, get_meme_id_api, meme_payload):
    create_resp = post_meme_api.create_meme(
        text=meme_payload["text"],
        url=meme_payload["url"],
        tags=meme_payload["tags"],
        info=meme_payload["info"],
    )
    assert create_resp.status_code == 200, create_resp.text

    meme_id = create_resp.json()["id"]

    delete_resp = delete_meme_id_api.delete_meme(meme_id)
    assert delete_resp.status_code == 200, delete_resp.text

    get_resp = get_meme_id_api.get_meme(meme_id)
    assert get_resp.status_code == 404
