import re 
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    

    print("Splitting at uppercase letters:", split_at_uppercase(content))


process_file('C:\\Users\\Arsen\\Desktop\\pp2\\lab5\\row.txt')