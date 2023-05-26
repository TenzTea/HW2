def is_sum_greater(a, b, c):
    if a + b > c:
        return True
    else:
        return False

# Ввод чисел
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

# Проверка и вывод результата
if is_sum_greater(a, b, c):
    print("Сумма чисел a и b больше числа c.")
else:
    print("Сумма чисел a и b не больше числа c.")
