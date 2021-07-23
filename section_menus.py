from mini_project_week4 import add_product, update_product, delete_product, product_list, courier_list, add_courier, update_courier, delete_courier, courier_save_and_exit, product_save_and_exit
from mini_project_week3 import delete_order, order_list, update_order, add_order, order_save_and_exit

def courier_menu():
    menu_input = int(input("What would you like to do?"))
    if menu_input ==0:
        print("go back")
    elif menu_input == 1:
        for i in range(len(courier_list)):
            print(f"{i+1}. {courier_list[i]['name']} \n")
    elif menu_input == 2:
        add_courier()
        courier_save_and_exit()
    elif menu_input == 3:
        update_courier()
        courier_save_and_exit()
    elif menu_input == 4:
        delete_courier()
        courier_save_and_exit()
        
def products_menu():
    menu_input = int(input("What would you like to do?"))
    if menu_input ==0:
        print("go back")
    elif menu_input == 1:
        for i in range(len(product_list)):
            print(f"{i+1}. {product_list[i]['name']} \n")
    elif menu_input == 2:
        add_product()
        product_save_and_exit()
    elif menu_input == 3:
        update_product()
        product_save_and_exit()
    elif menu_input == 4:
        delete_product()
        product_save_and_exit()

def orders_menu():
    menu_input = int(input("What would you like to do?"))
    if menu_input ==0:
        print("go back")
    elif menu_input == 1:
        print(order_list)
    elif menu_input == 2:
        add_order()
        order_save_and_exit()
    elif menu_input ==3:
        update_order()
        order_save_and_exit()
    elif menu_input ==4:
        delete_order()
        order_save_and_exit()

def save_everything():
    product_save_and_exit()
    courier_save_and_exit()
    order_save_and_exit()
    