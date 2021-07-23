import csv
### Products
# Coke = {
# "name": "Coke Zero",
# "price": float(0.8)
# }

# Fanta = {
# "name": "Fanta",
# "price": float(0.8)
# }

# product_list = [Coke, Fanta]
    
with open("products_list.csv", "r") as f:
    reader = csv.DictReader(f)
    product_list = list(reader)
    # print(product_list)

def add_product():
    product_name = input("Enter product name")
    product_price = input("Enter product price")
    product_name = {
        "name": product_name,
        "price": product_price,
    }
    product_list.append(product_name)
    print(product_list)

def delete_product():
    for i in range(len(product_list)):
        print(f"{i+1}. {product_list[i]['name']} \n")
    user_index_selection = int(input("Which item do you wish to delete? (Select number)"))
    product_name = product_list[user_index_selection-1]
    product_list.pop(user_index_selection-1)
    print(f"{product_name['name']} removed from list")

def update_product():
    for i in range(len(product_list)):
        print(f"{i+1}. {product_list[i]['name']} \n")
    user_index_selection = int(input("Which item do you wish to update? (Select number)"))
    name_or_price = int(input("""
Enter 1 to update name
Enter 2 to update price
Enter 3 to update both
                        """))
    if name_or_price == 1:
        user_new_name = input("What is the new product name?")
        product_list[user_index_selection-1]['name'] = str(user_new_name)
    elif name_or_price == 2:
        user_new_price = input("What is the new price?")
        product_list[user_index_selection-1]['price'] = user_new_price
    elif name_or_price ==3:
        user_new_name = input("What is the new product name?")
        user_new_price = input("What is the new price?")
        product_list[user_index_selection-1]['name'] = str(user_new_name)
        product_list[user_index_selection-1]['price'] = user_new_price
    print("Product updated")

# updateitem= update_item()
def product_save_and_exit():
    with open('products_list.csv', 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, 
                        fieldnames=product_list[0].keys())
        fc.writeheader()
        fc.writerows(product_list)
        
### Couriers 
# Bob = {
# "name": "Bob",
# "phone": "0789887889"
# }

# Jack = {
# "name": "Bob",
# "phone": "0789887889"
# }

# courier_list = [Bob, Jack]

with open("courier_list.csv", "r") as f:
    reader = csv.DictReader(f)
    courier_list = list(reader)
    print(courier_list)
    
def add_courier():
    courier_name = input("Enter courier name")
    courier_phone = input("Enter courier phone number")
    courier_name = {
        "name": courier_name,
        "phone": courier_phone,
    }
    courier_list.append(courier_name)
    print(f"{courier_name['name']} added.")

def delete_courier():
    for i in range(len(courier_list)):
        print(f"{i+1}. {courier_list[i]['name']} \n")
    user_index_selection = int(input("Which courier do you wish to delete? (Select number)"))
    courier_name = courier_list[user_index_selection-1]
    courier_list.pop(user_index_selection-1)
    print(f"{courier_name['name']} removed from list.")

def update_courier():
    for i in range(len(courier_list)):
        print(f"{i+1}. {courier_list[i]['name']} \n")
    user_index_selection = int(input("Which item do you wish to update? (Select number)"))
    name_or_phone = int(input("""
Enter 1 to update name
Enter 2 to update phone number
Enter 3 to update both
                    """))
    if name_or_phone == 1:
        user_new_name = input("What is the new courier name?")
        courier_list[user_index_selection-1]['name'] = str(user_new_name)
    elif name_or_phone == 2:
        user_new_phone = input("What is the new phone number?")
        courier_list[user_index_selection-1]['phone'] = user_new_phone
    elif name_or_phone ==3:
        user_new_name = input("What is the new courier name?")
        user_new_phone = input("What is the new phone number?")
        courier_list[user_index_selection-1]['name'] = str(user_new_name)
        courier_list[user_index_selection-1]['phone'] = user_new_phone
    print("Courier updated")

# updateitem= update_item()
def courier_save_and_exit():
    with open('courier_list.csv', 'w', encoding='utf8', newline='') as output:
        gc = csv.DictWriter(output, 
                        fieldnames=courier_list[0].keys())
        gc.writeheader()
        gc.writerows(courier_list)


