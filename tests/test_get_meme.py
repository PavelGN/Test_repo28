def test_list_memes_contains_created_meme(created_meme, get_meme_api):
    list_resp = get_meme_api.list_memes()
    assert list_resp.status_code == 200

    body = list_resp.json()
    assert "data" in body, "В ответе нет поля 'data'"

    memes = body["data"]
    assert isinstance(memes, list), "'data' должен быть списком"

    ids = [meme["id"] for meme in memes]
    assert created_meme in ids, "Созданный мем отсутствует в списке"
