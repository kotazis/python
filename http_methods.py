import requests


class HttpMethods:
    headers = {"Content-type" : 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        return requests.get(
            url,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )

    @staticmethod
    def post(url, body):
        return requests.post(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )

    @staticmethod
    def put(url, body):
        return requests.put(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )

    @staticmethod
    def delete(url, body):
        return requests.delete(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
