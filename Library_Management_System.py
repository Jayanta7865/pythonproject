# file_name="liabrary data.txt"
# with open(file_name,"a") as f:
liabrary={}
a="Welcome to my Liabrary"
print(a.center(100))
def add_book():
    n = int(input("How many books do you want to add? "))
    for i in range(n):
        print(f"\nAdding Book {i+1}:")
        book_id = input("Enter Book ID: ")
        if book_id in liabrary:
            print("Book ID already exists! Skipping...")
            continue  
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        qty = int(input("Enter Quantity: "))
        liabrary[book_id] = {"title": title, "author": author, "quantity": qty}
        
        print("Book added successfully!")
    # for i,item in liabrary[book_id].items():
    #         f.write(str(i))
            # f.write(":")
            # f.write(str(item))
            # f.write("\n")
def display_book():
    if not liabrary:
        print("No book avilable!!")
    else:
        print("\n Avilable books")
        for bid,info in liabrary.items():
            print(f"ID:{bid},Title:{info['title']},Author:{info['author']},Qty:{info['quantity']}")
    
def search_book():
    id=input("Enter book id or title to search:")
    found=False
    for bid,info in liabrary.items():
        if bid==id or id in info['title'].lower():
            print(f"ID:{bid},Title:{info['title']},Author:{info['author']},Qty:{info['quantity']}")
            found=True
    if not found:
        print("Id or title not match!\n Book not found")
def issue_book():
    book_id=input("Enter book Id to issued: ")
    if book_id in liabrary and liabrary [book_id]['quantity']>0:
        liabrary [book_id]['quantity']-=1
        print("Book issue Suessfully!!")
    else:
        print("Book not available")
def return_book():
    book_id=input("Enter book id to return: ")
    if book_id in liabrary:
        liabrary [book_id]['quantity']+=1
        print("Book return Suessfully....")
    else:
        print("Invalid Book id")
def remove_book():
    book_id=input("Enter Book Id to remove: ")
    if book_id in liabrary:
        del liabrary[book_id]
        print("Book removed Suessfully!!")
    else:
        print("Book id not found")
def menu():
    
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Remove Book")
    print("7. Exit")
def main():
    while True:
        menu()
        choice = input("\nEnter choice: ")
        if choice == "1":
            add_book()  
        elif choice == "2":
            display_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            remove_book()
        elif choice == "7":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()





