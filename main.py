print("Выберите операцию:","\n1. Сложение","\n2. Вычитание","\n3. Умножение","\n4. Деление")

while True:
    operation = input("Выберите операцию (1/2/3/4): ")
    if operation in ['1', '2', '3', '4']:
        break
    else:
        print("Выберите номер операции")

while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Введите числа")

if operation == '1':
    print(f"Результат: {num1} + {num2} = {num1 + num2}")
elif operation == '2':
    print(f"Результат: {num1} - {num2} = {num1 - num2}")
elif operation == '3':
    print(f"Результат: {num1} * {num2} = {num1 * num2}")
elif operation == '4':
    if num2 == 0:
        print("Не возможно деление на ноль")
    else:
        print(f"Результат: {num1} / {num2} = {num1 / num2}")
