def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Ввод сторон треугольника
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))

# Проверка и вывод результата
if is_triangle(a, b, c):
    print("Можно построить треугольник.")
else:
    print("Нельзя построить треугольник.")