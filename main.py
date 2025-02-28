age = int(input("Введите возраст "))
nationality = input("Назоваите страну вашего гражданства ")
disqualified = input("Являетесь ли вы дисквалифицированным? да/нет ")

if  disqualified == "да":
    disqualified = True
else:
    disqualified = False

if age >= 18 and nationality == "Россия" and disqualified == False:
    print("Вы можете голосовать на выборах")
else:
    print("Вы не можете голосовать на выборах")

