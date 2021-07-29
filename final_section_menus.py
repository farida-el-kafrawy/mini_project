from mini_project_week5 import add_courier_db, add_product_db, update_product_db, update_courier_db, delete_courier_db, delete_product_db, view_couriers, view_products
from mini_project_week3 import delete_order, order_list, update_order, add_order, order_save_and_exit

def courier_menu():
    menu_input = int(input("What would you like to do?"))
    if menu_input ==0:
        print("go back")
    elif menu_input == 1:
        view_couriers()
    elif menu_input == 2:
        add_courier_db()
    elif menu_input == 3:
        update_courier_db()
    elif menu_input == 4:
        delete_courier_db()
        
def products_menu():
    menu_input = int(input("What would you like to do?"))
    if menu_input ==0:
        print("go back")
    elif menu_input == 1:
        view_products()
    elif menu_input == 2:
        add_product_db()
    elif menu_input == 3:
        update_product_db()
    elif menu_input == 4:
        delete_product_db()

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
