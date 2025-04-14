import requests

class GoogleMapsAPI:
    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com"
        self.key = "?key=qaclick123"
        self.address = ""

    def post_send(self):
        post_url = self.base_url + "/maps/api/place/add/json" + self.key
        json_post_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        response = requests.post(post_url, json=json_post_location)

        print("[POST]", response.json(), "| Код: ", response.status_code)
        assert response.status_code == 200, "Ошибка статус кода"
        print("[POST] Статус код корректен")

        data = response.json()
        place_id = data.get("place_id", "")
        return place_id

    def put_send(self, place_id, new_address):
        self.address = new_address  # сохраняем адрес для дальнейшей проверки
        put_url = self.base_url + "/maps/api/place/update/json" + self.key

        json_put_location = {
            "place_id": place_id,
            "address": new_address,
            "key": "qaclick123"
        }

        result_put = requests.put(put_url, json=json_put_location)
        print("[PUT]", result_put.json(), "| Код: ", result_put.status_code)
        assert result_put.status_code == 200, "Ошибка статус кода"
        print("[PUT] Статус код корректен")

        check_put = result_put.json()
        assert check_put["msg"] == "Address successfully updated", "Ошибка запроса"
        print("[PUT] Запрос прошел успешно")
        return new_address

    def check_put(self, place_id):
        get_url = f"{self.base_url}/maps/api/place/get/json{self.key}&place_id={place_id}"
        result_get = requests.get(get_url)
        print("[GET]", result_get.json(), "| Код: ", result_get.status_code)
        assert result_get.status_code == 200, "[GET] Ошибка статус кода"

        result_get_json = result_get.json()
        actual_address = result_get_json.get("address")
        print("[GET] Адрес из ответа:", actual_address)
        print("[GET] Ожидаемый адрес:", self.address)
        assert actual_address == self.address, "Адрес не совпадает"
        print("[GET] Адрес успешно проверен")


