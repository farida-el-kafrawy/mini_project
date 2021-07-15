from mini_project_week2 import courier_list

order_1 = {
"customer_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 1,
"status": "preparing"
}
order_2 = {
"customer_name": "Sam",
"customer_address": "Unit 2, 24 Main Street, LONDON, WH1 2ER",
"customer_phone": "0784447334",
"courier": 2,
"status": "preparing"
}

order_list = [order_1, order_2]
print(order_list)
    
def add_order():
    customer_name = input("Enter customer name")
    customer_address = input("Enter customer address")
    customer_phone = input("Enter customer phone number")
    with open('courier_list.txt', 'w') as f:
            for i in range(len(courier_list)):
                print(f"{i+1}. {courier_list[i].title()}")
    courier_number= input("Which courier is delivering this order. Select number please.")
    new_order = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "courier": courier_number,
        "status": "preparing",
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
        order_list[update_choice-1]["customer_address"] = update_address
    elif update_property ==3:
        update_phone = input("Enter new phone number")
        order_list[update_choice-1]["customer_phone"] = update_phone
    elif update_property ==4:
        update_courier= input("Enter new courier")
        order_list[update_choice-1]["courier"] = update_courier
    elif update_property ==5:
        update_status = input("Enter new status")
        order_list[update_choice-1]["status"] = update_status
update_order()
print(order_list)