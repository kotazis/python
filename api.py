from utils.http_methods import HttpMethods


class GooglMapsApi:
    def __init__(self, base_url, key):

        self.base_url = "https://rahulshettyacademy.com"
        self.key = "?key=qaclick123"

    def create_new_place(self):
        body_json= {
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
        post_url = self.base_url + post_resource + self.key
        print(post_url)
        result_post = HttpMethods.post(post_url, body_json)
        print(result_post.text)
        return result_post

    def get_new_place(self, place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = self.base_url + get_resource + self.key + "&place_id" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return  result_get

    def put_new_place(self, place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = self.base_url + put_resource + self.key
        print(put_url)
        put_json = {
            "place_id" : place_id,
             "address" : "100 Lenina street, RU",
            "key" : "qaclick123"
        }
        result_put = HttpMethods.put(put_url, put_json)
        print(result_put.text)
        return result_put

    def delete_new_place(self, place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = self.base_url + delete_resource + self.key
        print(delete_url)
        delete_json = {
            "place_id": place_id
        }
        result_delete = HttpMethods.delete(delete_url, delete_json)
        print(result_delete.text)
        return  result_delete
