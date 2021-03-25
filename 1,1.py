import math

x = 22
a = x ** 7 + 22 * x ** 2
b = (38 * x ** 5 - 26 * x ** 6) / (math.tan(x) - math.log(x))
c = ((x ** 6) / 85) - 2 * x ** 3 - 56
result = a + math.sqrt(b) - c
print(f"{result:.2e}")
