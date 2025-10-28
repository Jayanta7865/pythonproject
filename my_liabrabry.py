import os

BOOK_FILE = "library.txt"
USER_FILE = "users.txt"
ISSUE_FILE = "issued.txt"

# ----------------- FILE HANDLING -------------------
def load_books():
    books = {}
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, "r") as f:
            for line in f:
                book_id, title, author, qty = line.strip().split("|")
                books[book_id] = {"title": title, "author": author, "quantity": int(qty)}
    return books

def save_books(books):
    with open(BOOK_FILE, "w") as f:
        for book_id, details in books.items():
            f.write(f"{book_id}|{details['title']}|{details['author']}|{details['quantity']}\n")

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                user_id, username, password = line.strip().split("|")
                users[user_id] = {"username": username, "password": password}
    return users

def save_users(users):
    with open(USER_FILE, "w") as f:
        for user_id, details in users.items():
            f.write(f"{user_id}|{details['username']}|{details['password']}\n")

def load_issued():
    issued = {}
    if os.path.exists(ISSUE_FILE):
        with open(ISSUE_FILE, "r") as f:
            for line in f:
                uid, book_id = line.strip().split("|")
                if uid not in issued:
                    issued[uid] = []
                issued[uid].append(book_id)
    return issued

def save_issued(issued):
    with open(ISSUE_FILE, "w") as f:
        for uid, books in issued.items():
            for book_id in books:
                f.write(f"{uid}|{book_id}\n")

# ----------------- ADMIN FUNCTIONS -------------------
def add_book(books):
    while True:
        book_id = input("Enter Book ID: ")
        if book_id in books:
            print("❌ Book ID already exists!")
            continue
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        qty = int(input("Enter Quantity: "))
        books[book_id] = {"title": title, "author": author, "quantity": qty}
        save_books(books)
        print("✅ Book added successfully!")

        more = input("Add another book? (y/n): ").lower()
        if more != "y":
            break

def remove_book(books):
    book_id = input("Enter Book ID to remove: ")
    if book_id in books:
        del books[book_id]
        save_books(books)
        print("🗑️ Book removed successfully!")
    else:
        print("❌ Book not found.")

def view_all_books(books):
    if not books:
        print("📂 No books available.")
        return
    print("\n--- Library Books ---")
    print("{:<10} {:<30} {:<40} {:<5}".format("ID", "Title", "Author", "Qty"))
    for book_id, details in books.items():
        print("{:<10} {:<30} {:<40} {:<5}".format(
            book_id, details['title'], details['author'], details['quantity']
        ))

def search_book(books):
    keyword = input("Enter Book ID or Title to search: ").lower()
    found = False
    for book_id, details in books.items():
        if keyword in book_id.lower() or keyword in details['title'].lower():
            print(f"🔎 {book_id} - {details['title']} by {details['author']} (Qty: {details['quantity']})")
            found = True
    if not found:
        print("❌ Book not found.")

def view_all_users(users):
    if not users:
        print("📂 No users registered.")
        return
    print("\n--- Registered Users ---")
    print("{:<15} {:<20}".format("User ID", "Username"))
    for user_id, details in users.items():
        print("{:<15} {:<20}".format(user_id, details['username']))

def remove_user(users):
    user_id = input("Enter User ID to remove: ")
    if user_id in users:
        del users[user_id]
        save_users(users)
        print("🗑️ User removed successfully!")
    else:
        print("❌ User not found.")

# ----------------- USER FUNCTIONS -------------------
def issue_book(uid, books, issued):
    while True:
        book_id = input("Enter Book ID to issue: ")
        if book_id in books and books[book_id]["quantity"] > 0:
            books[book_id]["quantity"] -= 1
            if uid not in issued:
                issued[uid] = []
            issued[uid].append(book_id)
            save_books(books)
            save_issued(issued)
            print(f"📖 Book '{books[book_id]['title']}' issued successfully!")
        else:
            print("❌ Book not available.")

        more = input("Issue another book? (yes/no): ").lower()
        if more != "yes":
            break

def return_book(uid, books, issued):
    if uid not in issued or not issued[uid]:
        print("❌ You have no books to return!")
        return

    while True:
        print("\n--- Your Issued Books ---")
        for bid in issued[uid]:
            print(f"{bid}: {books[bid]['title']}")

        book_id = input("Enter Book ID to return (or 'q' to stop): ")

        if book_id.lower() == "q":
            break

        if book_id in issued[uid]:
            issued[uid].remove(book_id)
            books[book_id]["quantity"] += 1  # keep quantity as int
            save_books(books)
            save_issued(issued)
            print(f"📚 Book '{books[book_id]['title']}' returned successfully!")
        else:
            print("❌ You didn’t issue this book!")

        if not issued[uid]:
            print("✅ All your books have been returned.")
            break

# ----------------- MENUS -------------------
def admin_panel(books, users):
    while True:
        print("\n===== Admin Panel =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. View All Users")
        print("6. Remove User")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            view_all_books(books)
        elif choice == "4":
            search_book(books)
        elif choice == "5":
            view_all_users(users)
        elif choice == "6":
            remove_user(users)
        elif choice == "7":
            break
        else:
            print("❌ Invalid choice!")

def user_panel(uid, books, issued):
    while True:
        print("\n===== User Panel =====")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            issue_book(uid, books, issued)
        elif choice == "2":
            return_book(uid, books, issued)
        elif choice == "3":
            view_all_books(books)
        elif choice == "4":
            search_book(books)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice!")

# ----------------- USER REGISTER & LOGIN -------------------
def register_user(users):
    uid = input("Create User ID: ")
    if uid in users:
        print("❌ User ID already exists!")
        return users
    uname = input("Enter Username: ")
    pwd = input("Create Password: ")
    users[uid] = {"username": uname, "password": pwd}
    save_users(users)
    print("✅ User registered successfully!")
    return users

def login(users):
    uid = input("Enter User ID: ")
    pwd = input("Enter Password: ")
    if uid in users and users[uid]["password"] == pwd:
        print(f"✅ Welcome {users[uid]['username']}!")
        return uid
    else:
        print("❌ Invalid login!")
        return None

# ----------------- MAIN PROGRAM -------------------
def main():
    books = load_books()
    users = load_users()
    issued = load_issued()

    a="....Library Management System...."
    print(f"\n{a.center(120)}")
    b="-"*140
    print(b)
    while True:
        role = input("\nAre you 'admin' or 'user'? (type exit to quit): ").lower()

        if role == "admin":
            uname = input("Admin Username: ")
            pwd = input("Admin Password: ")
            if uname == "admin" and pwd == "admin123":
                admin_panel(books, users)  
            else:
                print("❌ Wrong admin credentials!")

        elif role == "user":
            action = input("Do you want to 'login' or 'register'? ").lower()
            if action == "register":
                users = register_user(users)
            elif action == "login":
                uid = login(users)
                if uid:
                    user_panel(uid, books, issued)
            else:
                print("❌ Invalid action!")

        elif role == "exit":
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid input! Please type 'admin' or 'user'.")

if __name__ == "__main__":
    main()
