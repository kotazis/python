import requests


class http_methods:
    headers = {"Content-type" : 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        return requests.get(
            url,
            headers=http_methods.headers,
            cookies=http_methods.cookie
        )


    @staticmethod
    def post(url, body):
        return requests.post(
            url,
            json=body,
            headers=http_methods.headers,
            cookies=http_methods.cookie
        )

    @staticmethod
    def put(url, body):
        return requests.put(
            url,
            json=body,
            headers=http_methods.headers,
            cookies=http_methods.cookie
        )

    @staticmethod
    def delete(url, body):
        return requests.delete(
            url,
            json=body,
            headers=http_methods.headers,
            cookies=http_methods.cookie
        )
