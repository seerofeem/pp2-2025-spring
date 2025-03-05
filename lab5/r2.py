import re
def find_lowercase_with_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    

    print("Lowercase with underscore:", find_lowercase_with_underscore(content))


process_file('C:\\Users\\Arsen\\Desktop\\pp2\\lab5\\row.txt')