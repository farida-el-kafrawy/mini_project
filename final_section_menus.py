from mini_project_week5 import add_courier_db, add_product_db, update_product_db, update_courier_db, delete_courier_db, delete_product_db, view_couriers, view_products
from mini_project_week6 import check_courier, check_order_status, delete_order, view_orders, update_order, add_order
import json

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
        view_orders()
    elif menu_input == 2:
        add_order()
    elif menu_input ==3:
        update_order()
    elif menu_input ==4:
        delete_order()
    elif menu_input == 5:
        check_courier()
    elif menu_input ==6:
        check_order_status()
