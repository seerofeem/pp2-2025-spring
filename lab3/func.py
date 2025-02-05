code = """
# 1
def grams_to_ounces(grams):
    return 28.3495231 * grams
grams = float(input("Enter the grams: "))
ounces = grams_to_ounces(grams)
print(f"{grams} grams = {ounces:.2f} ounces")

# 2
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}F = {celsius:.2f}C")

# 3 
# x+y=35 (total heads)
# 2x+4y=94 (total legs)
def solve(numheads, numlegs):
    for chickens in range(numheads + 1): 
        rabbits = numheads - chickens 
        if 2 * chickens + 4 * rabbits == numlegs:  
            return chickens, rabbits  
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")

# 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n): 
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
numbers = list(map(int, input("Enter numbers: ").split()))
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

# 5
import itertools

def print_permutations():
    user_input = input("Enter a string: ")
    permutations = itertools.permutations(user_input)
    for perm in permutations:
        print("".join(perm))

print_permutations()

# 6
def reverse_words():
    user_input = input("Enter a sentence: ")
    words = user_input.split()  
    reversed_words = " ".join(reversed(words))  
    return reversed_words

rev = reverse_words()
print("Reversed sentence:", rev)

# 7
def double3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
nums = [1, 3, 3, 5, 2]
result = double3(nums)
print(result) 
nums2 = [1, 2, 3, 4, 3]
result = double3(nums2)
print(result) 

# 8
def spy_game(nums):
    sequence = [0, 0, 7]
    index = 0
    for num in nums:
        if num == sequence[index]:
            index += 1 
        if index == len(sequence): 
            return True
    return False
print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

# 9
import math
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

radius = float(input("Enter the radius: "))
volume = sphere_volume(radius)
print(f"The volume is {volume:.2f}")

# 10
def unique(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
numbers = [1, 2, 2, 3, 4, 1, 5, 6, 4]
result = unique(numbers)
print(result) 

# 11 
def is_palindrome(phrase):
    cl = ''.join(char.lower() for char in phrase if char.isalnum())
    if cl == cl[::-1]:
        return "The phrase is a palindrome."
    else:
        return "The phrase is not a palindrome."
input_phrase = input("Enter a word or phrase: ")
print(is_palindrome(input_phrase))

# 12
def histogram(lst):
    for num in lst:
        print('*' * num)
user_input = input("Enter a list of integers: ")
user_list = list(map(int, user_input.split()))

histogram(user_list)

# 13 
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")

    number_to_guess = random.randint(1, 20)
    
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    cnt = 0
    
    while True:
        guess = int(input("Take a guess.\n"))
        cnt += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break
guess_the_number()
"""
with open("C:\Users\Arsen\Desktop\pp2\lab3\func.py", "w") as file:
    file.write(code)










