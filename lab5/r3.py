import re
def find_uppercase_followed_by_lowercase(s):
    return re.findall(r'[A-Z][a-z]+', s)
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    print("Uppercase followed by lowercase:", find_uppercase_followed_by_lowercase(content))


process_file('C:\\Users\\Arsen\\Desktop\\pp2\\lab5\\row.txt')