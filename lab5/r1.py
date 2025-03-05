import re
def match_a_followed_by_2_or_3_b(s):
    return re.fullmatch(r'a{1}b{2,3}', s) is not None
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("Matching 'a' followed by 2-3 'b's:", match_a_followed_by_2_or_3_b(content))


process_file('C:\\Users\\Arsen\\Desktop\\pp2\\lab5\\row.txt')