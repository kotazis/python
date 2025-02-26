print("Выберите операцию:", "\n1. Сложение", "\n2. Вычитание", "\n3. Умножение", "\n4. Деление")

try:
    operation = input("Выберите операцию (1/2/3/4): ")
    if operation in ['1', '2', '3', '4']:

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if operation == '1':
             print(f"Результат: {num1} + {num2} = {num1 + num2}")
        elif operation == '2':
              print(f"Результат: {num1} - {num2} = {num1 - num2}")
        elif operation == '3':
             print(f"Результат: {num1} * {num2} = {num1 * num2}")
        elif operation == '4':
              print(f"Результат: {num1} / {num2} = {num1 / num2}")

    else: print("Неверный выбор операции.")

except ValueError:
    print("Ошибка: Введено не число")
except ZeroDivisionError:
    print("Деление на ноль невозможно")
