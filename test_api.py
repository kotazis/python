from utils.api import GooglMapsApi
from requests import Response
from utils.checking import Checking


class TestCreatePlace:
    def test_create_new_place(self):
        print("\nМетод POST")
        api = GooglMapsApi(base_url="https://rahulshettyacademy.com", key="?key=qaclick123")
        result_post: Response = api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post,200)

        print("Метод GET POST")
        result_get: Response = api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Метод PUT")
        result_put: Response = api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)

        print("Метод GET PUT")
        result_get: Response = api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Метод DELETE")
        result_delete: Response = api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print("Метод GET DELETE")
        result_delete: Response = api.get_new_place(place_id)
        Checking.check_status_code(result_delete, 404)
