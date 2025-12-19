import pytest
from Test_repo28.data.data import generate_meme_payload
from Test_repo28.endpoints.base import BaseClient


def test_created_meme_fields(created_meme, get_meme_id_api):
    meme_id, payload = created_meme

    get_resp = get_meme_id_api.get_meme(meme_id)
    BaseClient.assert_status_code(get_resp, 200)

    data = get_resp.json()

    BaseClient.assert_meme_equals(data, payload)


@pytest.mark.parametrize(
    "field,empty_value",
    [
        ("text", ""),
        ("url", ""),
        ("tags", []),
        ("info", {}),
    ],
)
def test_create_meme_with_empty_values(post_meme_api, field, empty_value):
    payload = generate_meme_payload()
    payload[field] = empty_value

    resp = post_meme_api.create_meme(
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )

    BaseClient.assert_status_code(resp, 200)