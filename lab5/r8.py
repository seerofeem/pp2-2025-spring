import re
def insert_spaces_before_capitals(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    

    print("Inserting spaces before capital letters:", insert_spaces_before_capitals(content))


process_file('C:\\Users\\Arsen\\Desktop\\pp2\\lab5\\row.txt')