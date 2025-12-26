import pytest
from Test_repo28.data.data import generate_meme_payload, INVALID_MEME_FIELDS


def test_get_nonexistent_meme(get_meme_id_api):
    get_meme_id_api.get_meme(99999999)
    get_meme_id_api.assert_status_code(404)


def test_delete_nonexistent_meme(delete_meme_id_api):
    delete_meme_id_api.delete_meme(99999999)
    delete_meme_id_api.assert_status_code(404)


def test_update_nonexistent_meme(put_meme_id_api):
    put_meme_id_api.update_meme(
        meme_id=99999999,
        text="text",
        url=(
            "https://encrypted-tbn0.gstatic.com/images?"
            "q=tbn:ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s"
        ),
        tags=["test"],
        info={"a": 1},
    )
    put_meme_id_api.assert_status_code(404)


@pytest.mark.parametrize("field,invalid_value", INVALID_MEME_FIELDS)
def test_create_meme_with_invalid_data(post_meme_api, field, invalid_value):
    payload = generate_meme_payload()
    payload[field] = invalid_value

    post_meme_api.create_meme(
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )
    post_meme_api.assert_status_code(400)


@pytest.mark.parametrize("field,invalid_value", INVALID_MEME_FIELDS)
def test_update_meme_with_invalid_data(
    created_meme,
    put_meme_id_api,
    field,
    invalid_value,
):
    meme_id, payload = created_meme
    payload[field] = invalid_value

    put_meme_id_api.update_meme(
        meme_id=meme_id,
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )
    put_meme_id_api.assert_status_code(400)


def test_token_is_not_alive(auth_api):
    auth_api.token_is_alive("invalid_token_123")
    auth_api.assert_status_code(404)


def test_authorize_without_name(auth_api):
    auth_api.post("/authorize", json={})
    auth_api.assert_status_code(400)


def test_create_meme_without_auth(unauth_post_meme_api):
    payload = generate_meme_payload()

    unauth_post_meme_api.create_meme(
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )
    unauth_post_meme_api.assert_status_code(401)


def test_get_memes_without_auth(unauth_get_meme_api):
    unauth_get_meme_api.list_memes()
    unauth_get_meme_api.assert_status_code(401)


def test_update_meme_without_auth(unauth_put_meme_id_api):
    unauth_put_meme_id_api.update_meme(
        meme_id=1,
        text="text",
        url=(
            "https://encrypted-tbn0.gstatic.com/images?"
            "q=tbn:ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s"
        ),
        tags=["test"],
        info={"a": 1},
    )
    unauth_put_meme_id_api.assert_status_code(401)


def test_delete_meme_without_auth(unauth_delete_meme_id_api):
    unauth_delete_meme_id_api.delete_meme(1)
    unauth_delete_meme_id_api.assert_status_code(401)


def test_get_meme_by_id_without_auth(unauth_get_meme_id_api):
    unauth_get_meme_id_api.get_meme(1)
    unauth_get_meme_id_api.assert_status_code(401)
