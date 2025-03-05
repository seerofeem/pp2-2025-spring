import re
def match_a_anything_b(s):
    return re.fullmatch(r'a.*b', s) is not None
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("Matching 'a' followed by anything ending in 'b':", match_a_anything_b(content))


process_file('C:\\Users\\Arsen\\Desktop\\pp2\\lab5\\row.txt')