from mini_project_week5 import view_couriers
import csv
import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Noorsis4",
  database="mini_project"
)
mycursor = mydb.cursor()
# order_1 = {
# "customer_name": "John",
# "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
# "customer_phone": "0789887334",
# "courier": 1,
# "status": "Preparing"
# }
# order_2 = {
# "customer_name": "Sam",
# "customer_address": "Unit 2, 24 Main Street, LONDON, WH1 2ER",
# "customer_phone": "0784447334",
# "courier": 2,
# "status": "Preparing"
# }

with open("order_list.csv", "r") as f:
    reader = csv.DictReader(f)
    a = list(reader)
    
order_list= a

# print(json.dumps(order_list, sort_keys=False, indent=4))

def add_order():
    customer_name = input("Enter customer name")
    customer_address = input("Enter customer address")
    customer_phone = input("Enter customer phone number")
    view_couriers()
    courier_number= input("Which courier is delivering this order. Select number please.")
    new_order = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "courier": courier_number,
        "status": "Preparing",
    }
    order_list.append(new_order)
    print(order_list)

def update_order():
    for i in range(len(order_list)):
        print(f"{i+1}. {order_list[i]}")
    update_choice = int(input("Which order do you want to update? Choose number"))
    update_property = int(input("""
What do you want to update?
1. Customer Name
2. Customer Address
3. Customer Phone Number
4. Courier
5. Order status
    """))
    if update_property == 1:
        update_name = input("Enter new name")
        order_list[update_choice-1]["customer_name"] = update_name
        for i in range(len(order_list)):
            print(f"{i+1}. {order_list[i]}")
    elif update_property ==2:
        update_address= input("Enter new address")
        order_list[update_choice-1]["customer_address"] = "f{update_address}"
    elif update_property ==3:
        update_phone = input("Enter new phone number")
        order_list[update_choice-1]["customer_phone"] = update_phone
    elif update_property ==4:
        view_couriers()
        update_courier= input("Which courier is delivering this order. Select number please.")
        order_list[update_choice-1]["courier"] = update_courier
    elif update_property ==5:
        update_status = int(input("""
Enter new status
1. Preparing
2. With courier
3. Delivered
    """))
        if update_status ==3:
            order_list[update_choice-1]['status'] = "Delivered"
        elif update_status ==2:
            order_list[update_choice-1]['status'] = "With courier"
        elif update_status ==1:
            order_list[update_choice-1]['status'] = "Preparing"
        print("Order delivery status updated")
    
def delete_order():
    for i in range(len(order_list)):
        print(f"{i+1}. {order_list[i]}")
    order_to_delete = int(input("Which order do you wish to delete? (Select number)"))
    order_list.pop(order_to_delete-1)
    print("Order deleted")

def order_save_and_exit():
    with open('order_list.csv', 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, 
            fieldnames=order_list[0].keys())
        fc.writeheader()
        fc.writerows(order_list)
        
        
# update_order()
# order_save_and_exit()