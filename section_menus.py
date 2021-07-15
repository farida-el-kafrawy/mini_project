from mini_project_week1 import add_item, update_item, delete_item, product_list
from mini_project_week2 import courier_list, add_courier, update_courier, delete_courier
from mini_project_week3 import order_list

def courier_menu():
    menu_input = int(input("What would you like to do?"))
    if menu_input ==0:
        print("go back")
    elif menu_input == 1:
        with open('courier_list.txt', 'w') as f:
            for i in range(len(courier_list)):
                print(f"{i+1}. {courier_list[i].title()}")
    elif menu_input == 2:
        add_courier()
    elif menu_input == 3:
        update_courier()
    elif menu_input == 4:
        delete_courier()
        
def products_menu():
    menu_input = int(input("What would you like to do?"))
    if menu_input ==0:
        print("go back")
    elif menu_input == 1:
        with open('product_list.txt', 'w') as f:
            for i in range(len(product_list)):
                print(f"{i+1}. {product_list[i].title()}")
    elif menu_input == 2:
        add_item()
    elif menu_input == 3:
        update_item()
    elif menu_input == 4:
        delete_item()

def orders_menu():
    menu_input = int(input("What would you like to do?"))
    if menu_input ==0:
        print("go back")
    elif menu_input == 1:
        print(order_list)
    
