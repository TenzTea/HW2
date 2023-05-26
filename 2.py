def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

# Ввод числа
a = int(input("Введите число a: "))

# Проверка и вывод результата
if is_even(a):
    print("Число является четным.")
else:
    print("Число не является четным.")
