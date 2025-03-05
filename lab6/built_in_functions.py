from functools import reduce
import time
import math

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)

def count_case(s):
    return sum(1 for c in s if c.isupper()), sum(1 for c in s if c.islower())

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(n, ms):
    time.sleep(ms / 1000)
    print(f"Square root of {n} after {ms} milliseconds is {math.sqrt(n)}")

def all_true(tpl):
    return all(tpl)
lst = [2, 4, 6, 8]
print(multiply_list(lst))
s = "Hello World!"
print(count_case(s))
print(is_palindrome(s))
n = 12312
ms = 2221
print(delayed_sqrt(n, ms))
tpl = (True, True, False)
print(all_true(tpl))