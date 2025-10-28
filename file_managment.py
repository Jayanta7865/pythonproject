import os
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename}: Created sussfully...")
          
    except FileExistsError:
        print(f"File {filename} already exits...")
    except Exception as E:
        print("An error occurred")
    
def view_files():
    files=os.listdir()
    if not files:
        print("File not found!!")
    else:
        print("Files in directory.")
        for file in files:
            print(file)
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} is deleted successfully..")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred.")
def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
            print(f"Content of '{filename}' :\n {content}")
    except FileNotFoundError:
        print(f"{filename} not exits..")
    except Exception as e:
        print("An error occurred.")
def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content=input("Enter data to add = ")
            f.write(content + "\n")
            print(f"Content added to {filename} Successfully..")

    except FileNotFoundError:
        print(f"{filename} not exits..")
    except Exception as e:
        print("An error occurred.")
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}' successfully!")
    except FileNotFoundError:
        print(f"File '{old_name}' not found!")
    except Exception as e:
        print("An error occurred:", e)


def main():
    while True:
        print("File Managment System")
        print("1.Creat file")
        print("2.View all files")
        print("3.Delete file")
        print("4.Read file")
        print("5.Edit file")
        print("6.Rename file")
        print("7.Exit")

        choice=int(input("Enter your choice (1-6): "))
        if choice==1:
            filename=input("Enter file name to create: ")
            create_file(filename)
        elif choice==2:
            view_files()
        elif choice==3:
            filename=input("Enter file name to delete: ")
            delete_file(filename)
        elif choice==4:
            filename=input("Enter file name to read: ")
            read_file(filename)
        elif choice==5:
            filename=input("Enter file name to edit: ")
            edit_file(filename)
        elif choice == 6:
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            rename_file(old_name, new_name)
        elif choice==7:
            print("System Exits!!")
            break
            
        else:
            print("Please! choose correct option.")
if __name__=="__main__" :
    main()  
        






    