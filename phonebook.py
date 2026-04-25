import json
import csv
from connect import get_connection


def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    birthday = input("Enter birthday (YYYY-MM-DD): ")
    group_id = input("Enter group id (1-Family, 2-Work, 3-Friend, 4-Other): ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
    """, (name, email, birthday, group_id))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added!")


def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        ORDER BY c.id
    """)

    rows = cur.fetchall()

    print("\n--- ALL CONTACTS ---")

    if len(rows) == 0:
        print("No contacts found.")
    else:
        for row in rows:
            print("----------------------")
            print("ID:", row[0])
            print("Name:", row[1])
            print("Email:", row[2])
            print("Birthday:", row[3])
            print("Group:", row[4])
            print("Phone:", row[5])
            print("Type:", row[6])

    cur.close()
    conn.close()


def search_contacts():
    query = input("Enter search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (query,))
    rows = cur.fetchall()

    print("\n--- SEARCH RESULT ---")

    if len(rows) == 0:
        print("Nothing found.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def add_phone():
    name = input("Enter contact name: ")
    phone = input("Enter phone: ")
    ptype = input("Enter type (home/work/mobile): ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()

    print("Phone added!")


def move_to_group():
    name = input("Enter contact name: ")
    group_name = input("Enter new group name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL move_to_group(%s, %s)", (name, group_name))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact moved to group!")


def filter_by_group():
    group_name = input("Enter group name (Family/Work/Friend/Other): ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
        ORDER BY c.id
    """, (group_name,))

    rows = cur.fetchall()

    print("\n--- FILTER BY GROUP ---")

    if len(rows) == 0:
        print("No contacts in this group.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def sort_contacts():
    print("Sort by:")
    print("1. Name")
    print("2. Birthday")
    print("3. Date added")

    choice = input("Choose: ")

    if choice == "1":
        sort_field = "c.name"
    elif choice == "2":
        sort_field = "c.birthday"
    elif choice == "3":
        sort_field = "c.created_at"
    else:
        print("Wrong choice!")
        return

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
        SELECT c.id, c.name, c.email, c.birthday, c.created_at, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY {sort_field}
    """)

    rows = cur.fetchall()

    print("\n--- SORTED CONTACTS ---")

    for row in rows:
        print("----------------------")
        print("ID:", row[0])
        print("Name:", row[1])
        print("Email:", row[2])
        print("Birthday:", row[3])
        print("Date added:", row[4])
        print("Group:", row[5])

    cur.close()
    conn.close()


def pagination_contacts():
    page = 0
    limit = 3

    while True:
        offset = page * limit

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.id, c.name, c.email, c.birthday, g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            ORDER BY c.id
            LIMIT %s OFFSET %s
        """, (limit, offset))

        rows = cur.fetchall()

        cur.close()
        conn.close()

        print("\n--- PAGE", page + 1, "---")

        if len(rows) == 0:
            print("No contacts on this page.")
        else:
            for row in rows:
                print(row)

        command = input("next / prev / quit: ")

        if command == "next":
            page += 1
        elif command == "prev":
            if page > 0:
                page -= 1
            else:
                print("You are on first page.")
        elif command == "quit":
            break
        else:
            print("Wrong command!")


def export_to_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        ORDER BY c.id
    """)

    rows = cur.fetchall()

    contacts = []

    for row in rows:
        contact = {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "birthday": str(row[3]),
            "group": row[4],
            "phone": row[5],
            "phone_type": row[6]
        }
        contacts.append(contact)

    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    cur.close()
    conn.close()

    print("Contacts exported to contacts.json")


def import_from_json():
    try:
        with open("contacts.json", "r") as file:
            data = json.load(file)
    except:
        print("contacts.json not found!")
        return

    conn = get_connection()
    cur = conn.cursor()

    for contact in data:
        name = contact["name"]
        email = contact["email"]
        birthday = contact["birthday"]
        group_name = contact["group"]
        phone = contact["phone"]
        phone_type = contact["phone_type"]

        cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
        group = cur.fetchone()

        if group is None:
            cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group_name,))
            group_id = cur.fetchone()[0]
        else:
            group_id = group[0]

        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        existing = cur.fetchone()

        if existing:
            answer = input(f"{name} exists. skip / overwrite? ")

            if answer == "skip":
                continue
            elif answer == "overwrite":
                cur.execute("""
                    UPDATE contacts
                    SET email=%s, birthday=%s, group_id=%s
                    WHERE name=%s
                """, (email, birthday, group_id, name))
                contact_id = existing[0]
            else:
                continue
        else:
            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (name, email, birthday, group_id))
            contact_id = cur.fetchone()[0]

        if phone:
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (contact_id, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()

    print("Import from JSON finished!")


def import_from_csv():
    conn = get_connection()
    cur = conn.cursor()

    try:
        file = open("contacts.csv", "r")
    except:
        print("contacts.csv not found!")
        return

    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        email = row["email"]
        birthday = row["birthday"]
        group_name = row["group"]
        phone = row["phone"]
        phone_type = row["phone_type"]

        cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
        group = cur.fetchone()

        if group is None:
            cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group_name,))
            group_id = cur.fetchone()[0]
        else:
            group_id = group[0]

        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (name) DO UPDATE
            SET email = EXCLUDED.email,
                birthday = EXCLUDED.birthday,
                group_id = EXCLUDED.group_id
            RETURNING id
        """, (name, email, birthday, group_id))

        contact_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES (%s, %s, %s)
        """, (contact_id, phone, phone_type))

    file.close()
    conn.commit()
    cur.close()
    conn.close()

    print("CSV import finished!")


def main():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Add contact")
        print("2. Show all contacts")
        print("3. Search contacts")
        print("4. Add phone")
        print("5. Move contact to group")
        print("6. Filter by group")
        print("7. Sort contacts")
        print("8. Pagination")
        print("9. Export to JSON")
        print("10. Import from JSON")
        print("11. Import from CSV")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            add_phone()
        elif choice == "5":
            move_to_group()
        elif choice == "6":
            filter_by_group()
        elif choice == "7":
            sort_contacts()
        elif choice == "8":
            pagination_contacts()
        elif choice == "9":
            export_to_json()
        elif choice == "10":
            import_from_json()
        elif choice == "11":
            import_from_csv()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Wrong choice!")


if __name__ == "__main__":
    main()