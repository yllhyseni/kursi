menu = {
    "pizza": 12.99,
    "burger": 8.99,
    "salad": 6.99,
    "cocacola": 2.00
}

order_list = []

def run_restaurant():
    print("Welcome to our restaurant!")
    while True:
        display_menu()
        take_order()
        calculate_total()
        more_order = input("Do you want to order more products? (yes/no): ").strip().lower()
        if more_order != 'yes':
            print(f"Thank you for your order!")
            break

def display_menu():
    print("\nMenu:")
    for name, price in menu.items():
        print(f"{name}: ${price:.2f}")
    print()

def take_order():
    while True:
        order = input("Shkruaj produktin qe deshiron (ose 'done' për të përfunduar): ").strip().lower()
        if order == 'done':
            break
        elif order in menu:
            order_list.append(order)
            print(f"Produkt: {order}, Çmimi: ${menu[order]:.2f}")
        else:
            print("Produkti nuk është në menu.")

def calculate_total():
    total = sum(menu[item] for item in order_list)
    print(f"Totali: ${total:.2f}")
    order_list.clear()  


run_restaurant()
