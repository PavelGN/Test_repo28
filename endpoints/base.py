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



