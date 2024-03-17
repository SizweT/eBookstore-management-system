"""
A bookstore program to be used by a clerk. This program create a database
and then provide the clerk with options to append/add new books, update
existing books, search for existing books, and deleting existing books from the
database
"""

import sqlite3


# Function to create the database and a table if they don't exist
def create_database_and_a_table():
    try:
        db = sqlite3.connect('ebookstore_db.db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS ebookstore (
            id INTEGER PRIMARY KEY, 
            title TEXT, 
            author TEXT,
            qty INTEGER)''')
        db.commit()
        # Enter records into the database one at a time
        try:
            cursor.execute('''INSERT OR IGNORE INTO ebookstore (id, title, 
                author, qty) VALUES(?,?,?,?)''',
                           (3001, 'A Tale of Two Cities',
                            'Charles Dickens', 30))
            cursor.execute('''INSERT OR IGNORE INTO ebookstore (id, title, 
                author, qty) VALUES(?,?,?,?)''', (
                3002, "Harry Potter and the Philosopher's Stone",
                'J.K. Rowling',
                40))
            cursor.execute('''INSERT OR IGNORE INTO ebookstore (id, title, 
                author, qty) VALUES(?,?,?,?)''', (
                3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25))
            cursor.execute('''INSERT OR IGNORE INTO ebookstore (id, title, 
                author, qty) VALUES(?,?,?,?)''',
                           (3004, 'The Lord of the Rings',
                            'J.R.R Tolkien', 37))
            cursor.execute('''INSERT OR IGNORE INTO ebookstore (id, title, 
                author, qty) VALUES(?,?,?,?)''',
                           (3005, 'Alice in Wonderland', 'Lewis Carrol',
                            12))
            db.commit()

        except sqlite3.Error as e:
            print("An error occurred while entering records:", e)

        db.close()
        print("Database and table created successfully!")

    except sqlite3.Error as e:
        print("An error occurred while creating database and table:", e)


# Function to enter a new book record/row
def enter_book():
    try:
        id_num = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        qty = int(input("Enter book quantity: "))

        db = sqlite3.connect('ebookstore_db.db')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO ebookstore (id, title, author, qty) 
                        VALUES(?,?,?,?)''', (id_num, title, author, qty))
        db.commit()
        db.close()
        print("Book added successfully!")
    except (sqlite3.Error, ValueError) as e:
        print("An error occurred while entering book:", e)


# Function to update a book record
def update_book():
    try:
        id_num = int(input("Enter book ID to update: "))
        qty = int(input("Enter new quantity: "))

        db = sqlite3.connect('ebookstore_db.db')
        cursor = db.cursor()
        cursor.execute('''UPDATE ebookstore SET qty=? WHERE id=?''',
                       (qty, id_num))
        db.commit()
        db.close()
        print("Book quantity updated successfully!")
    except (sqlite3.Error, ValueError) as e:
        print("An error occurred while updating book:", e)


# Function to delete a book record
def delete_book():
    try:
        id_num = int(input("Enter book ID to delete: "))

        db = sqlite3.connect('ebookstore_db.db')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM ebookstore WHERE id=?''',
                       (id_num,))
        db.commit()
        db.close()
        print("Book deleted successfully!")
    except (sqlite3.Error, ValueError) as e:
        print("An error occurred while deleting book:", e)


# Function to search for a book by title
def search_book():
    try:
        title = input("Enter book title to search: ")

        db = sqlite3.connect('ebookstore_db.db')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM ebookstore WHERE title LIKE ?''',
                       ('%' + title + '%',))
        books = cursor.fetchall()
        db.close()

        if books:
            print("Matching books found:")
            for book in books:
                print("ID:", book[0])
                print("Title:", book[1])
                print("Author:", book[2])
                print("Quantity:", book[3])
        else:
            print("No matching books found.")
    except sqlite3.Error as e:
        print("An error occurred while searching for book:", e)


# Main function to display menu and handle user input
def main():
    while True:
        print("\nMenu:")
        print("1. Enter a book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Search for a book")
        print("5. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            enter_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    create_database_and_a_table()
    main()
