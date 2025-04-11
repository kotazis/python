import requests


class Test:
    def check_code(self):
        #['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie',
        # 'music', 'political', 'religion', 'science', 'sport', 'travel']
        category = input("Введите номер категории: ")
        jokes_list = requests.get("https://api.chucknorris.io/jokes/categories")
        categories = jokes_list.json()
        print(categories)

        assert category in  categories, "Такой категории нет"

        joke = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
        joke_text = joke.json().get("value")
        print(f"Категория: {category} | Шутка: {joke_text}")


joke1 = Test()
joke1.check_code()
