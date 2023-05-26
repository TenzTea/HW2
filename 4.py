def is_first_greater(a, b):
    if a > b:
        return True
    else:
        return False

# Ввод чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Проверка и вывод результата
if is_first_greater(a, b):
    print("Первое число больше второго.")
else:
    print("Первое число не больше второго.")
