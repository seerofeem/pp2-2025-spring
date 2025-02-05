from func import is_palindrome

phrase = str(input("Enter the word: "))
if is_palindrome(phrase):
    print(f"'{phrase}' is a palindrome!")
else:
    print(f"'{phrase}' is not a palindrome!")

