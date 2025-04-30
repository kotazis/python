import requests


class http_methods:
    headers = {"Content-type" : 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result = requests.get(url, headers=http_methods.headers, cookies=http_methods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
        return result
