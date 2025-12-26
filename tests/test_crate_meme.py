import pytest
from Test_repo28.data.data import generate_meme_payload


@pytest.mark.parametrize(
    "field,empty_value",
    [
        ("text", ""),
        ("url", ""),
        ("tags", []),
        ("info", {}),
        ("info", {"meta": 1}),
    ],
)
def test_create_meme_with_empty_values(
    post_meme_api, get_meme_id_api, field, empty_value
):
    payload = generate_meme_payload()
    payload[field] = empty_value

    post_meme_api.create_meme(
        text=payload["text"],
        url=payload["url"],
        tags=payload["tags"],
        info=payload["info"],
    )
    post_meme_api.assert_status_code(200)

    meme_id = post_meme_api.assert_meme_created()

    get_meme_id_api.get_meme(meme_id)
    get_meme_id_api.assert_status_code(200)
    get_meme_id_api.assert_meme_equals(payload)
