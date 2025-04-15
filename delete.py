import requests

class GoogleMapsAPI:
    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com"
        self.key = "?key=qaclick123"
        self.place_ids = []

    def post_send(self):
        post_url = self.base_url + "/maps/api/place/add/json" + self.key
        json_post = {
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

        for i in range(5):
            response = requests.post(post_url, json=json_post)
            data = response.json()
            place_id = data.get("place_id", "")
            self.place_ids.append(place_id)
            print(f"[POST{i}] place_id: {place_id} | Статус: {response.status_code}")
            assert response.status_code == 200, f"[POST{i}] Ошибка: Ожидался статус 200, получено {response.status_code}"
            print(f"[POST{i}] Статус код верен")

    def file_create(self):
        with open("place_ids.txt", "w", encoding="utf-8") as f:
            f.writelines(f"{ids}\n" for ids in self.place_ids if ids)
        print("Все place_id записаны в place_ids.txt\n")

    def get_send(self):
        get_url_base = self.base_url + "/maps/api/place/get/json" + self.key

        with open("place_ids.txt", "r", encoding="utf-8") as f:
            place_ids = [line.strip() for line in f if line.strip()]

        for i, place_id in enumerate(place_ids):
            url = f"{get_url_base}&place_id={place_id}"
            response = requests.get(url)
            print(f"[GET{i}] place_id: {place_id} | Статус: {response.status_code}")
            print(f"[GET{i}] Ответ JSON:\n{response.json()}\n")

    def delete_selected(self):
        delete_url = self.base_url + "/maps/api/place/delete/json" + self.key

        with open("place_ids.txt", "r", encoding="utf-8") as f:
            place_ids = [line.strip() for line in f if line.strip()]

        to_delete_indexes = [1, 3]  # 2-й и 4-й элементы (нумерация с 0)
        for i in to_delete_indexes:
            load = {"place_id": place_ids[i]}
            response = requests.post(delete_url, json=load)
            print(f"[DELETE{i+1}] place_id: {place_ids[i]} | Статус: {response.status_code}")
            assert response.status_code == 200, f"[DELETE{i+1}] Ошибка: Ожидался статус 200, получено {response.status_code}"
            print(f"[DELETE{i+1}] Удаление прошло успешно")



    def get_filter_valid(self):
        get_url_base = self.base_url + "/maps/api/place/get/json" + self.key

        with open("place_ids.txt", "r", encoding="utf-8") as f:
            place_ids = [line.strip() for line in f if line.strip()]

        valid_ids = []
        for i, place_id in enumerate(place_ids):
            url = f"{get_url_base}&place_id={place_id}"
            response = requests.get(url)
            json_data = response.json()

            print(f"[CHECK{i}] place_id: {place_id} | Статус: {response.status_code}")
            print(f"[CHECK{i}] Ответ JSON: {json_data}")

            if response.status_code == 200:
                valid_ids.append(place_id)
                print(f"[CHECK{i}] Локация существует")
            else:
                print(f"[CHECK{i}] Локация не существует")

        with open("valid_place_ids.txt", "w", encoding="utf-8") as f:
            for pid in valid_ids:
                f.write(pid + "\n")

        print("\n valid_place_ids.txt успешно создан только с существующими place_id\n")


start = GoogleMapsAPI()
start.post_send()
start.file_create()
start.get_send()
start.delete_selected()
start.get_filter_valid()
