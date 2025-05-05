from utils.api import GooglMapsApi
from requests import Response


class TestCreatePlace:
    def test_create_new_place(self):
        print("\nМетод POST")
        api = GooglMapsApi(base_url="https://rahulshettyacademy.com", key="?key=qaclick123")

        result_post: Response = api.create_new_place()
        check_post = result_post.json()

        place_id = check_post.get("place_id")

        print("Метод GET POST")
        result_get: Response = api.get_new_place(place_id)

        print("Метод PUT")
        result_put: Response = api.put_new_place(place_id)

        print("Метод GET PUT")
        result_get: Response = api.get_new_place(place_id)

        print("Метод DELETE")
        result_delete: Response = api.delete_new_place(place_id)

        print("Метод GET DELETE")
        result_delete: Response = api.get_new_place(place_id)
