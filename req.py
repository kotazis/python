import requests


class Test:
    def __init__(self):
        self.url = "https://api.chucknorris.io/jokes/random"
        self.full_url = None
        self.result = None
        self.joke_category = None

    def type_joke(self, joke_category):     # Получение случайной шутки по определенной категории
        self.joke_category = joke_category
        self.full_url = f"{self.url}?category={joke_category}"
        print(self.full_url)

    def check_code(self):       # Проверку на статус-код
        self.result = requests.get(self.full_url)
        assert self.result.status_code == 200, "Статус не верен"
        print(f"Статус {self.result.status_code} верен")

    def json_output(self):      # Вывод на печать самой шутки
        self.result.encoding = 'utf-8'
        print(self.result.json()["value"])

    def joke_output(self):      # Проверку на содержании имени Chuck в теле шутки, Проверка на соответствие категории
        data = self.result.json()
        assert "Chuck" in data["value"], "В шутке нет слова 'Chuck'"
        print("В шутке есть слово 'Chuck'")
        assert self.joke_category in  data["categories"], "Категории не совпадают"
        print("Категории совпадают")


joke1 = Test()
joke1.type_joke("music")
joke1.check_code()
joke1.json_output()
joke1.joke_output()




