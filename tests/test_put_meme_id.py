def test_update_meme(created_meme, put_meme_id_api, get_meme_id_api):
    new_text = "updated_blablabla"
    new_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s"
    new_tags = ["updated", "test"]
    new_info = {"meta": "updated"}

    update_resp = put_meme_id_api.update_meme(
        meme_id=created_meme,
        text=new_text,
        url=new_url,
        tags=new_tags,
        info=new_info,
    )
    assert update_resp.status_code == 200, update_resp.text

    get_resp = get_meme_id_api.get_meme(created_meme)
    assert get_resp.status_code == 200, get_resp.text

    data = get_resp.json()

    assert data["text"] == new_text
    assert data["url"] == new_url
    assert data["tags"] == new_tags
    assert data["info"] == new_info
