def test_get_nonexistent_meme(get_meme_id_api):
    resp = get_meme_id_api.get_meme(99999999)
    assert resp.status_code == 404


def test_delete_nonexistent_meme(delete_meme_id_api):
    resp = delete_meme_id_api.delete_meme(99999999)
    assert resp.status_code == 404


def test_update_nonexistent_meme(put_meme_id_api):
    resp = put_meme_id_api.update_meme(
        meme_id=99999999,
        text="text",
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s",
        tags=["test"],
        info={"a": 1},
    )
    assert resp.status_code == 404


def test_create_meme_without_required_field(post_meme_api, meme_payload):
    resp = post_meme_api.create_meme(
        text=None,
        url=meme_payload["url"],
        tags=meme_payload["tags"],
        info=meme_payload["info"],
    )
    assert resp.status_code == 400


def test_create_meme_with_invalid_text_type(post_meme_api, meme_payload):
    resp = post_meme_api.create_meme(
        text=123,
        url=meme_payload["url"],
        tags=meme_payload["tags"],
        info=meme_payload["info"],
    )
    assert resp.status_code == 400


def test_create_meme_with_invalid_tags_type(post_meme_api, meme_payload):
    resp = post_meme_api.create_meme(
        text=meme_payload["text"],
        url=meme_payload["url"],
        tags="not-an-array",
        info=meme_payload["info"],
    )
    assert resp.status_code == 400


def test_create_meme_with_invalid_info_type(post_meme_api, meme_payload):
    resp = post_meme_api.create_meme(
        text=meme_payload["text"],
        url=meme_payload["url"],
        tags=meme_payload["tags"],
        info="not-an-object",
    )
    assert resp.status_code == 400


