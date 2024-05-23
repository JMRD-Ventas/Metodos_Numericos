def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple(n):
    lcm_value = 1
    for i in range(1, n + 1):
        lcm_value = lcm(lcm_value, i)
    return lcm_value

print(smallest_multiple(20))  # Salida: 232792560