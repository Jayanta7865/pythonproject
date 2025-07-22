menu = {
    "pizza":199,
    "burger":99,
    "salad":99,
    "soda": 69,
    "coffee":199,
    "tea":149,
    "sandwich":299,
    "pasta":239,
    "ice cream":79,

}
a="Welcome to the Jayanta's cafe"
print(a.center(100))
def display_menu():
    print("---- Menu ----")
    for item, price in menu.items():
        print(f"{item}: rs.{price:.2f}")
        

def take_order():
    order = []
    while True:
        item = input("\nEnter item to order (or 'done' to finish): ").title().lower()
        if item == 'done':
            break
        if item in menu:
            order.append(item)
        else:
            print("Item not found. Please choose from the menu.")
    return order

def calculate_bill(order):
    total = sum(menu[item] for item in order)
    return total

def print_receipt(order, total):
    print("\n--- Receipt ---")
    for item in order:
        print(f"{item}: rs.{menu[item]:.2f}")
    print(f"Total Ammount: rs.{total:.2f}")

def main():
    display_menu()
    order = take_order()
    total = calculate_bill(order)
    print_receipt(order, total)
# print("\n Thank you for visiting Jayant's cafe")

if __name__ == "__main__":
    main()


print("\n Visit again soon")
print("\nHave a great day!")
