import pytest
from Test_repo28.data.data import generate_meme_payload
from Test_repo28.data.data import INVALID_MEME_FIELDS
from Test_repo28.endpoints.base import BaseClient


def test_get_nonexistent_meme(get_meme_id_api):
    resp = get_meme_id_api.get_meme(99999999)
    BaseClient.assert_status_code(resp, 404)


def test_delete_nonexistent_meme(delete_meme_id_api):
    resp = delete_meme_id_api.delete_meme(99999999)
    BaseClient.assert_status_code(resp, 404)


def test_update_nonexistent_meme(put_meme_id_api):
    resp = put_meme_id_api.update_meme(
        meme_id=99999999,
        text="text",
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s",
        tags=["test"],
        info={"a": 1},
    )
    BaseClient.assert_status_code(resp, 404)


@pytest.mark.parametrize("field,invalid_value", INVALID_MEME_FIELDS)
def test_create_meme_with_invalid_data(post_meme_api, field, invalid_value):
    payload = generate_meme_payload()
    payload[field] = invalid_value

    resp = post_meme_api.create_meme(
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )

    BaseClient.assert_status_code(resp, 400)



@pytest.mark.parametrize("field,invalid_value", INVALID_MEME_FIELDS)
def test_update_meme_with_invalid_data(
    created_meme,
    put_meme_id_api,
    field,
    invalid_value,
):
    meme_id, payload = created_meme

    payload[field] = invalid_value

    resp = put_meme_id_api.update_meme(
        meme_id=meme_id,
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )

    BaseClient.assert_status_code(resp, 400)


def test_token_is_not_alive(auth_api):
    resp = auth_api.token_is_alive("invalid_token_123")
    BaseClient.assert_status_code(resp, 404)


def test_authorize_without_name(auth_api):
    resp = auth_api.client.post("/authorize", json={})
    BaseClient.assert_status_code(resp, 400)