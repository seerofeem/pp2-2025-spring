import psycopg2
import csv

# connect to postgres
conn = psycopg2.connect(
    dbname="asd",
    user="postgres",
    password="Qwertylox007!",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# drop and create book table
cur.execute("DROP TABLE IF EXISTS book")
cur.execute("""
CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    phone VARCHAR(20) UNIQUE
)
""")
conn.commit()
cur.execute("DROP FUNCTION IF EXISTS search_by_pattern(TEXT)")
# function: search by name or phone pattern
cur.execute("""
CREATE OR REPLACE FUNCTION search_by_pattern(p_pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR(100), phone VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY
    SELECT b.id, b.first_name, b.phone FROM book b
    WHERE b.first_name ILIKE '%' || p_pattern || '%'
       OR b.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

# procedure: insert or update user by name
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM book WHERE first_name = p_name) THEN
        UPDATE book SET phone = p_phone WHERE first_name = p_name;
    ELSE
        INSERT INTO book (first_name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;
""")

# procedure: bulk insert users with phone check
cur.execute("""
CREATE OR REPLACE PROCEDURE bulk_insert_users(
    p_names TEXT[],
    p_phones TEXT[],
    OUT incorrect_data TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    incorrect_data := '{}';
    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^\d{10,15}$' THEN
            BEGIN
                INSERT INTO book (first_name, phone)
                VALUES (p_names[i], p_phones[i]);
            EXCEPTION WHEN unique_violation THEN
                UPDATE book SET phone = p_phones[i] WHERE first_name = p_names[i];
            END;
        ELSE
            incorrect_data := array_append(incorrect_data, p_names[i] || ' - ' || p_phones[i]);
        END IF;
    END LOOP;
END;
$$;
""")
cur.execute("DROP FUNCTION IF EXISTS get_paginated_data(INT, INT)")
# function: get paginated data
cur.execute("""
CREATE OR REPLACE FUNCTION get_paginated_data(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, first_name VARCHAR(100), phone VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM book
    ORDER BY id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
""")

# procedure: delete user by name or phone
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM book WHERE first_name = p_name OR phone = p_phone;
END;
$$;
""")

# helper: check if phone exists
def phone_exists(phone):
    cur.execute("SELECT 1 FROM book WHERE phone = %s", (phone,))
    return cur.fetchone() is not None

# insert data from csv
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not phone_exists(row['phone']):
                cur.execute("INSERT INTO book (first_name, phone) VALUES (%s, %s)",
                            (row['first_name'], row['phone']))
    conn.commit()

# insert single user from console
def insert_from_console():
    name = input("enter name: ")
    phone = input("enter phone: ")
    if not phone_exists(phone):
        cur.execute("INSERT INTO book (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()

# update name using phone
def update_name_by_phone(old_phone, new_name):
    cur.execute("UPDATE book SET first_name = %s WHERE phone = %s", (new_name, old_phone))
    conn.commit()

# update phone using name
def update_phone_by_name(name, new_phone):
    cur.execute("UPDATE book SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()

# show all records
def query_all():
    cur.execute("SELECT * FROM book")
    print(cur.fetchall())

# search by name
def query_by_name(name):
    cur.execute("SELECT * FROM book WHERE first_name = %s", (name,))
    print(cur.fetchall())

# search by phone prefix
def query_by_phone_partial(partial):
    cur.execute("SELECT * FROM book WHERE phone LIKE %s", (partial + '%',))
    print(cur.fetchall())

# delete by name
def delete_by_name(name):
    cur.execute("DELETE FROM book WHERE first_name = %s", (name,))
    conn.commit()

# delete by phone
def delete_by_phone(phone):
    cur.execute("DELETE FROM book WHERE phone = %s", (phone,))
    conn.commit()

insert_from_csv("C:\\Users\\Arsen\\Desktop\\pp2\\lab11\\phonebook.csv")

insert_from_console()

cur.execute("SELECT * FROM search_by_pattern(%s)", ("Joh",))
print(cur.fetchall()) 

cur.execute("CALL insert_or_update_user(%s, %s)", ("Alice", "87007654321"))
conn.commit()

cur.execute("""
    CALL bulk_insert_users(
        ARRAY['TestUser1', 'InvalidPhoneUser', 'TestUser2'],
        ARRAY['87001112233', 'notaphone', '87009998877'],
        NULL
    )
""")

cur.execute("SELECT * FROM get_paginated_data(%s, %s)", (5, 0))
print(cur.fetchall())

cur.execute("CALL delete_user(%s, %s)", ("Alice", "87007654321"))
conn.commit()

query_all()
query_by_name("John")
query_by_phone_partial("8700")
# close connection
cur.close()
conn.close()
