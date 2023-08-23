1. 

number = int(input("Введите число: "))
if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

2.

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник с такими сторонами может существовать")
else:
    print("Треугольник с такими сторонами не может существовать")

3.

n = int(input("Введите число N: "))
sum = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        sum += 0.1*j
print(sum)

4.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(1001):
    if is_prime(i):
        sum += i
print(sum)

5.

side = float(input("Введите длину стороны квадрата: "))
radius = float(input("Введите радиус круга: "))

square_area = side ** 2
circle_area = 3.14 * radius ** 2

if square_area > circle_area:
    perimeter = 4 * side
else:
    perimeter = 2 * 3.14 * radius

print("Периметр фигуры: ", perimeter)