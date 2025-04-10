import requests


class Test:
    def check_code(self):
         jokes_list  = requests.get("https://api.chucknorris.io/jokes/categories")
         print(jokes_list.json(), type(jokes_list))

         categories = jokes_list.json()

         for category in categories:
             joke = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
             joke_text = joke.json().get("value")
             print(f"Категория: {category} | Шутка: {joke_text}")

joke1 = Test()
joke1.check_code()
