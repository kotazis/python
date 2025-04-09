import requests


url = "https://api.chucknorris.io/jokes/random"
print(url)

result = requests.get(url)
print(result.status_code)

assert 200 == result.status_code, "Статус не верен"
print("Статус верен")

result.encoding = 'utf-8'
print(result.json())
