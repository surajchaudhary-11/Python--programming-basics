a, b = 17, 5
print(a + b, a - b, a * b, a / b)
print(a // b, a % b, a ** b)           # arithmetic
print(a > b, a == b, a != b)           # comparison
print(a > 10 and b < 10)               # logical
print(not (a > b))
a += 3; print(a)                       # assignment
print(5 & 3, 5 | 3, 5 ^ 3, 5 << 1)     # bitwise
print(3 in [1, 2, 3], 3 not in [1, 2]) # membership
x = [1]; y = [1]
print(x == y, x is y)                  # identity