def test_update_meme(created_meme, put_meme_id_api, get_meme_id_api):
    meme_id, payload = created_meme

    payload["text"] = "updated_blablabla"
    payload["url"] = (
        "https://encrypted-tbn0.gstatic.com/images?"
        "q=tbn:ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s"
    )
    payload["tags"] = ["updated", "test"]
    payload["info"] = {"meta": "updated"}

    put_meme_id_api.update_meme(
        meme_id=meme_id,
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )
    put_meme_id_api.client.assert_status_code(200)

    get_meme_id_api.get_meme(meme_id)
    get_meme_id_api.client.assert_status_code(200)
    get_meme_id_api.assert_meme_equals(payload)
