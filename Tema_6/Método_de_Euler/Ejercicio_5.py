def largest_palindrome_product(digits):
    min_value = 10 ** (digits - 1)
    max_value = 10 ** digits - 1
    largest = 0
    for i in range(max_value, min_value - 1, -1):
        for j in range(i, min_value - 1, -1):
            product = i * j
            if str(product) == str(product)[::-1] and product > largest:
                largest = product
    return largest

print(largest_palindrome_product(3))