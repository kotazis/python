from api_main import GoogleMapsAPI

start = GoogleMapsAPI()
place_id = start.post_send()
start.put_send(place_id, "address nomber 1")
start.check_put(place_id)
