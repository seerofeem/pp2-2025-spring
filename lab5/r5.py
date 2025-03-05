import re

def replace_space_comma_dot(s):
    return re.sub(r'[ ,.]', ':', s)
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    

    print("Replacing space, comma, dot with colon:", replace_space_comma_dot(content))


process_file('C:\\Users\\Arsen\\Desktop\\pp2\\lab5\\row.txt')