words = ["One", "Two", "Three", "Four", "Five"]

try:
    num = int(input("Введите число от 1 до 5: "))
    if 1 <= num <= 5:
        print("Соответствующее слово:", words[num - 1])
    else:
        print("Ошибка: введите число от 1 до 5.")
except ValueError:
    print("Ошибка: введите целое число.")
