from mini_project_week5 import add_courier_db, add_product_db, update_product_db, update_courier_db, delete_courier_db, delete_product_db, view_couriers, view_products
from mini_project_week6 import check_order_status, check_courier, view_orders, add_order, update_order, delete_order, orders_export_csv
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
    else: 
        print("Try again")
        courier_menu()
        
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
    else: 
        print("Try again")
        courier_menu()
        
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
        check_order_status()
    elif menu_input == 6:
        check_courier()
    else: 
        print("Try again")
        courier_menu()
