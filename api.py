from utils.http_methods import HttpMethods


base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class GooglMapsApi:
    @staticmethod
    def create_new_place():
        json_body= {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
             ],
            "website": "http://google.com",
            "language": "French-IN"}
        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_body)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return  result_get
