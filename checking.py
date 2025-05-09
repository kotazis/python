import json
from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert  status_code == response.status_code, "Ошибка, статус код = " + str(response.status_code)
        print("Успешно, статус код = " + str(response.status_code))

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token)  == expected_value, "Ошибка, отсутствие полей"
        print("Все поля присутствуют")

