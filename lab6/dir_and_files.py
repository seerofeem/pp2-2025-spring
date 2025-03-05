import os
import shutil

def list_directories_and_files(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))], \
           [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def check_access(path):
    return os.access(path, os.F_OK), os.access(path, os.R_OK), os.access(path, os.W_OK), os.access(path, os.X_OK)

def path_exists(path):
    return os.path.exists(path), os.path.basename(path), os.path.dirname(path)

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

def write_list_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines("\n".join(data))

def generate_text_files():
    for letter in range(65, 91):
        with open(f"{chr(letter)}.txt", "w") as f:
            f.write(f"File {chr(letter)}.txt")

def copy_file(src, dest):
    shutil.copy2(src, dest)

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
path = "C:\\Users\\Arsen\\Desktop\\pp2"
print(list_directories_and_files(path))
print(check_access(path))
print(path_exists(path))
file = "C:\\Users\\Arsen\\Desktop\\pp2\\lab5\\row.txt"
print(count_lines(file))
file2 = "C:\\Users\\Arsen\\Desktop\\pp2\\lab6\\test.txt"
data = ['a','b','c','d']
print(write_list_to_file(file2, data))
print(generate_text_files())
print(copy_file("C:\\Users\\Arsen\\Desktop\\pp2\\A.txt", "C:\\Users\\Arsen\\Desktop\\pp2\\B.txt"))
print(delete_file("C:\\Users\\Arsen\\Desktop\\pp2\\Z.txt"))