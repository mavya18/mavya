num1 = float(input("Введите первое число: "))
operation = input("Выберите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Ошибка: деление на ноль!")
        result = None
else:
    print("Неизвестная операция!")
    result = None

print(f"Результат: {result}")
