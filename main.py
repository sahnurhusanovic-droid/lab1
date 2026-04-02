import psycopg2
import csv
conn = psycopg2.connect(
    dbname="phonebook",  
    user="postgres",
    password="shahnur__08",
    host="localhost",
    port="5433"
)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()

#1 Insert fron console

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Added!")

# 🔹 2. Insert from CSV
def insert_from_csv():
    with open("date.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("CSV inserted!")

#3 Update
def update_contact():
    name = input("Enter name to update: ")
    new_phone=input("New phone: ")
    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE name=%s",
        (new_phone,name)
    )
    conn.commit()
    print("Updated!")
    
#4 Search name
def search_by_name():
    name=input("Search name: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        ('%'+name+'%',)
    )
    for row in cur.fetchall():
        print(row)
        
#5 Search none prefix
def search_by_prefix():
    prefix=input("Phone prefix: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix +'%',)
    )
    for row in cur.fetchall():
        print(row)
        
#6 Delete
def delete_contact():
    value = input("Enter name or phone: ")
    cur.execute(
        "DELETE FROM phonebook WHERE name=%s OR phone=%s",
        (value,value)
    )
    conn.commit()
    print("Deleted!")
    
#7 Show all contacts
def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts!")
    
# MENU
while True:
    print("\n1.Add console")
    print("2.Add CSV")
    print("3.Update")
    print("4.Search name")
    print("5.Search prefix")
    print("6.Delete")
    print("7. Show all contacts")
    print("0.Exit")
    
    choice=input("Choose: ")
    
    if choice=="1":
        insert_from_console()
    elif choice=="2":
        insert_from_csv()
    elif choice=="3":
        update_contact()
    elif choice=="4":
        search_by_name()
    elif choice=="5":
        search_by_prefix()
    elif choice=="6":
        delete_contact()
    elif choice=="7":
        show_all()
    elif choice=="0":
        break
cur.close()
conn.close()