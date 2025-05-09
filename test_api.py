import pytest
from utils.api import GooglMapsApi
from utils.checking import Checking
from requests import Response


@pytest.fixture(scope="class")
def api() -> GooglMapsApi:
    return GooglMapsApi(base_url="https://rahulshettyacademy.com", key="?key=qaclick123")


@pytest.fixture
def place_id(api: GooglMapsApi) -> str:
    response: Response = api.create_new_place()
    Checking.check_status_code(response, 200)
    Checking.check_json_token(response, ["status", "place_id", "scope", "reference", "id"])
    return response.json()["place_id"]


class TestCreatePlace:

    def test_post_create_place(self, place_id: str):
        print("\nМетод POST — проверка уже в fixture")
        assert place_id is not None 

    def test_get_after_post(self, api: GooglMapsApi, place_id: str):
        print("Метод GET POST")
        response = api.get_new_place(place_id)
        Checking.check_status_code(response, 200)
        Checking.check_json_token(response, ["location", "accuracy", "name", "phone_number", "address", "types", "website", "language"])

    def test_put_update_place(self, api: GooglMapsApi, place_id: str):
        print("Метод PUT")
        response = api.put_new_place(place_id)
        Checking.check_status_code(response, 200)
        Checking.check_json_token(response, ["msg"])

    def test_get_after_put(self, api: GooglMapsApi, place_id: str):
        print("Метод GET PUT")
        api.put_new_place(place_id)
        response = api.get_new_place(place_id)
        Checking.check_status_code(response, 200)
        Checking.check_json_token(response, ["location", "accuracy", "name", "phone_number", "address", "types", "website", "language"])

    def test_delete_place(self, api: GooglMapsApi, place_id: str):
        print("Метод DELETE")
        response = api.delete_new_place(place_id)
        Checking.check_status_code(response, 200)
        Checking.check_json_token(response, ["status"])

    def test_get_after_delete(self, api: GooglMapsApi, place_id: str):
        print("Метод GET DELETE")
        api.delete_new_place(place_id)
        response = api.get_new_place(place_id)
        Checking.check_status_code(response, 404)
        Checking.check_json_token(response, ["msg"])
