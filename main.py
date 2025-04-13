import requests

class GoogleMapsAPI:
    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com"
        self.key = "?key=qaclick123"
        self.place_ids = []  # 🟢 Атрибут экземпляра для хранения всех place_id

    def post_send(self):
        post_url = self.base_url + "/maps/api/place/add/json" + self.key
        json_loc = {
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
            response = requests.post(post_url, json=json_loc)
            data = response.json()
            place_id = data.get("place_id", "")
            self.place_ids.append(place_id)
            print(f"[POST{i}] place_id: {place_id} | Статус: {response.status_code}")

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


start = GoogleMapsAPI()
start.post_send()
start.file_create()
start.get_send()
