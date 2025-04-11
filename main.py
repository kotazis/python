import requests


class Test:
    def check_code(self):
        jokes_list = requests.get("https://api.chucknorris.io/jokes/categories")
        categories_raw = jokes_list.json()
        
        categories = {i + 1: name for i, name in enumerate(categories_raw)}

        print("Доступные категории:")
        for num, name in categories.items():
            print(f"{num}: {name}")

        category_num = int(input("Введите номер категории: "))

        assert category_num in categories, "Такой категории нет"

        category = categories[category_num]

        joke = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
        joke_text = joke.json().get("value")
        print(f"Категория: {category} | Шутка: {joke_text}")


joke1 = Test()
joke1.check_code()
