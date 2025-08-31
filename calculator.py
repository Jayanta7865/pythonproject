def add(numbers):
    return sum(numbers)
def sub(numbers):
    result=numbers[0]
    for i in numbers[1:]:
        result-=i
    return result
def mul(numbers):
    result=1
    for i in numbers:
        result*=i
    return result
def div(numbers):
    result=numbers[0]
    for i in numbers[1:]:
        if i==0:
            return ("Error,Zero division Error..")
        else:
            result/=i
        return result
   
def calculator():
    while True:
        print("\n---- Simple Calculator ----")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        choice=int(input("Enter your choice(1-5): "))
        if choice == 5:
            print("Exiting calculator. Goodbye!")
            break
        
        numbers=list(map(float,input("Enter the number you want to oparetion using space: ").split()))
        
        if choice == 1:
            print(f"Result: {add(numbers)}")
        elif choice == 2:
            print(f"Result: {sub(numbers)}")
        elif choice == 3:
            print(f"Result: {mul(numbers)}")
        elif choice == 4:
            print(f"Result: {div(numbers)}")
        else:
            print("Invalid choice! Please try again.")
        again = input("Do you want to solve another equation? (yes/no): ").lower()
        if again != "yes":
            print("Exiting calculator. Goodbye!")
            break


calculator()
           


    


