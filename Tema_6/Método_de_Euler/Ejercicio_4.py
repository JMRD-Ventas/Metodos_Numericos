def fibonacci_even_sum(n):
    a, b = 0, 1
    sum = 0
    while b < n:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    return sum

print(fibonacci_even_sum(4000000))  # Salida: 4613732