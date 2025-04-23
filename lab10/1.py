import psycopg2
import csv


def get_connection():
    return psycopg2.connect(dbname="asd" ,user="postgres" ,password="Qwertylox007!" ,host="localhost" ,port="5432")

try:
    conn = get_connection()
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone_number VARCHAR(15),
            email VARCHAR(100)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_data_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            cur.execute("""
                INSERT INTO phonebook (first_name, last_name, phone_number, email) 
                VALUES (%s, %s, %s, %s);
            """, row)
    conn.commit()
    cur.close()
    conn.close()


def insert_data_manually():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email (optional): ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO phonebook (first_name, last_name, phone_number, email)
        VALUES (%s, %s, %s, %s);
    """, (first_name, last_name, phone_number, email))
    conn.commit()
    cur.close()
    conn.close()


def update_user_data(user_name, new_phone=None, new_first_name=None):
    conn = get_connection()
    cur = conn.cursor()
    if new_phone:
        cur.execute("""
            UPDATE phonebook
            SET phone_number = %s
            WHERE first_name = %s;
        """, (new_phone, user_name))

    if new_first_name:
        cur.execute("""
            UPDATE PhoneBook
            SET first_name = %s
            WHERE first_name = %s;
        """, (new_first_name, user_name))

    conn.commit()
    cur.close()
    conn.close()


def query_data(filter_by, value):
    conn = get_connection()
    cur = conn.cursor()
    if filter_by == 'first_name':
        cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s;", (value,))
    elif filter_by == 'last_name':
        cur.execute("SELECT * FROM PhoneBook WHERE last_name = %s;", (value,))
    elif filter_by == 'phone_number':
        cur.execute("SELECT * FROM PhoneBook WHERE phone_number = %s;", (value,))
    else:
        print("Invalid filter!")
        return

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_data(user_name=None, phone_number=None):
    conn = get_connection()
    cur = conn.cursor()

    if user_name:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (user_name,))
    if phone_number:
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s;", (phone_number,))

    conn.commit()
    cur.close()
    conn.close()





if __name__ == '__main__':
    create_table()
    insert_data_from_csv("C:\\Users\\Arsen\\Desktop\\pp2\\lab10\\contacts.csv")
    # insert_data_manually()
