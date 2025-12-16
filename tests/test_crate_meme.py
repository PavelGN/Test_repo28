def test_created_meme_fields(created_meme, get_meme_id_api, meme_payload):
    get_resp = get_meme_id_api.get_meme(created_meme)
    assert get_resp.status_code == 200

    data = get_resp.json()

    assert data["text"] == meme_payload["text"]
    assert data["url"] == meme_payload["url"]
    assert data["tags"] == meme_payload["tags"]
    assert data["info"] == meme_payload["info"]
