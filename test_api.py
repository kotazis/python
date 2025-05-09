import pytest
from utils.api import GooglMapsApi
from utils.checking import Checking


@pytest.fixture
def api() -> GooglMapsApi:
    return GooglMapsApi(base_url="https://rahulshettyacademy.com", key="?key=qaclick123")


def test_create_place(api: GooglMapsApi):
    response = api.create_new_place()
    Checking.check_status_code(response, 200)
    Checking.check_json_token(response, ["status", "place_id", "scope", "reference", "id"])

def test_get_place(api: GooglMapsApi):
    place_id = api.create_new_place().json()["place_id"]
    response = api.get_new_place(place_id)
    Checking.check_status_code(response, 200)
    Checking.check_json_token(response, ["location", "accuracy", "name", "phone_number", "address","types", "website", "language"])

def test_update_place(api: GooglMapsApi):
    place_id = api.create_new_place().json()["place_id"]
    response = api.put_new_place(place_id)
    Checking.check_status_code(response, 200)

def test_delete_place(api: GooglMapsApi):
    place_id = api.create_new_place().json()["place_id"]
    response = api.delete_new_place(place_id)
    Checking.check_status_code(response, 200)
    response_after = api.get_new_place(place_id)
    Checking.check_status_code(response_after, 404)

