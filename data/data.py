import random
import string


def generate_meme_payload():
    return {
        "text": "test-" + "".join(random.choices(string.ascii_letters, k=6)),
        "url": (
            "https://www.boredpanda.com/blog/wp-content/uploads/2022/09/"
            "it-humor-and-memes-204-632853f7bbbad__700.jpg"
        ),
        "tags": ["funny", "test"],
        "info": {"meta": random.randint(1, 100)},
    }


INVALID_MEME_FIELDS = [
    ("text", None),
    ("text", 123),
    ("tags", "not-an-array"),
    ("info", "not-an-object"),
]
