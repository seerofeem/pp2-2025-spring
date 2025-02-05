def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = list(range(1,51))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)