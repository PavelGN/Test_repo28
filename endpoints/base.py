class BaseClient:
    def __init__(self, base_url, session):
        self.base_url = base_url.rstrip("/")
        self.session = session
        self.response = None

    def set_auth_token(self, token):
        self.session.headers.update({"Authorization": token})

    def get(self, path: str, params: dict = None, headers: dict = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        self.response = self.session.get(url, params=params, headers=headers)
        return self.response

    def post(self, path: str, json: dict = None, headers: dict = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        self.response = self.session.post(url, json=json, headers=headers)
        return self.response

    def put(self, path: str, json: dict = None, headers: dict = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        self.response = self.session.put(url, json=json, headers=headers)
        return self.response

    def delete(self, path: str, headers: dict = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        self.response = self.session.delete(url, headers=headers)
        return self.response

    def assert_status_code(self, expected_status):
        assert self.response is not None, "No response to assert"
        assert self.response.status_code == expected_status, (
            f"Expected status {expected_status}, "
            f"got {self.response.status_code}. "
        )

    def assert_meme_equals(self, expected: dict):
        body = self.response.json()
        assert body["text"] == expected["text"]
        assert body["url"] == expected["url"]
        assert body["tags"] == expected["tags"]
        assert body["info"] == expected["info"]