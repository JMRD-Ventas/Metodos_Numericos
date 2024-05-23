def largest_palindrome_product(digits):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    min_value = 10 ** (digits - 1)
    max_value = 10 ** digits - 1
    largest = max_value ** 2
    for i in range(max_value, min_value - 1, -1):
        for j in range(i, min_value - 1, -1):
            product = i * j
            if is_palindrome(product) and product < largest:
                largest = product
    return largest

print(largest_palindrome_product(3))  # Salida: 906609