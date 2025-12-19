class BaseClient:
    def __init__(self, base_url, session):
        self.base_url = base_url.rstrip('/')
        self.session = session

    def set_auth_token(self, token):
        self.session.headers.update({'Authorization': token})

    def get(self, path: str, params: dict = None, headers: dict = None):
        url = f"{self.base_url}/{path.lstrip('/')}"

        combined_headers = dict(self.session.headers)
        if headers:
            combined_headers.update(headers)

        response = self.session.get(url, params=params, headers=combined_headers)
        return response

    def post(self, path: str, json: dict = None, headers: dict = None):
        url = f"{self.base_url}/{path.lstrip('/')}"

        combined_headers = dict(self.session.headers)
        if headers:
            combined_headers.update(headers)

        response = self.session.post(url, json=json, headers=combined_headers)

        return response

    def put(self, path: str, json: dict = None, headers: dict = None):
        url = f"{self.base_url}/{path.lstrip('/')}"

        combined_headers = dict(self.session.headers)
        if headers:
            combined_headers.update(headers)

        response = self.session.put(url, json=json, headers=combined_headers)

        return response

    def delete(self, path: str, headers: dict = None):
        url = f"{self.base_url}/{path.lstrip('/')}"

        combined_headers = dict(self.session.headers)
        if headers:
            combined_headers.update(headers)

        response = self.session.delete(url, headers=combined_headers)

        return response


    @staticmethod
    def assert_status_code(response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected status {expected_status}, "
            f"got {response.status_code}. "
        )


    @staticmethod
    def assert_meme_equals(actual: dict, expected: dict):
        assert actual["text"] == expected["text"], "Field 'text' mismatch"
        assert actual["url"] == expected["url"], "Field 'url' mismatch"
        assert actual["tags"] == expected["tags"], "Field 'tags' mismatch"
        assert actual["info"] == expected["info"], "Field 'info' mismatch"

    @staticmethod
    def assert_memes_list_response(body: dict):
        assert "data" in body, "Response has no 'data' field"
        assert isinstance(body["data"], list), "'data' field is not a list"

    @staticmethod
    def assert_meme_in_list(memes: list, meme_id: int):
        ids = [meme["id"] for meme in memes]
        assert meme_id in ids, "Created meme is not present in the memes list"

    @staticmethod
    def assert_token_response(body: dict):
        assert "token" in body, "Response has no 'token' field"
        assert body["token"], "Token value is empty"