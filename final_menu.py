# main menu
from mini_project_week5 import add_courier_db, add_product_db, update_product_db, update_courier_db, delete_courier_db, delete_product_db, view_couriers, view_products, courier_export_csv, product_export_csv
from mini_project_week6 import check_order_status, check_courier, view_orders, add_order, update_order, delete_order, orders_export_csv
from rich.console import Console

rich = Console()

def back_or_no():
    while True:
        try: 
            rich.print("\n [#228B22] Would you like to go back to the main menu? [/]")
            go_back = int(input("""
    Press 1 for Yes
    Press 2 for No"""))
            if go_back == 1:
                main_menu()
            elif go_back ==2: 
                print("""
 ▐█▀▄─ ▀▄─▄▀ █▀▀──█
─▐█▀▀▄ ──█── █▀▀──▀
─▐█▄▄▀ ──▀── ▀▀▀──▄
""")
                exit()
            else: 
                rich.print("""[#808080] 
Option was not found. 
Try again. [/]""")
        except ValueError:
            rich.print("""[#808080] 
Option was not found. 
Try again. [/]""")

def main_menu():
    rich.print("""[bold][#228B22]
    Main Menu
Central Perk Cafe [/][/]""")
    rich.print("""[#808080]
      )  (
     (   ) )
      ) ( ( [/]
[green]    _______[/][#808080])[/][green]_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------' [/]""")
    main_selection = rich.input("""
[#228B22]  A. Home [/]
[#A7DBD8]  B. Products [/]
[#3CAEA3]  C. Couriers [/]
[#F6D55C]  D. Orders [/]
[#ED553B]  E. Save and Exit [/]

Please make a selection A, B, C or D or E:
""")
    if main_selection =="B" or main_selection == "b":
        products_menu()
        back_or_no()
    if main_selection == "C" or main_selection == "c":
        courier_menu()
        back_or_no()
    if main_selection == "D" or main_selection == "d":
        orders_menu()
        back_or_no()
    if main_selection == "E" or main_selection == "e":
        save_and_exit()
    if main_selection == "A" or main_selection == "a":
        rich.print("[#228B22] Back to Home [/]")
        main_menu()
    else:
        rich.print(f"""[#808080] 
Option '{main_selection}' was not found. 
Try again.
Back to main menu. [/]""")
        main_menu()

def courier_menu():
    rich.print("""[#3CAEA3]
  Press 0 to return to main menu
  Press 1 to view courier list
  Press 2 to add new courier
  Press 3 to update existing courier
  Press 4 to delete courier
[/]  """)
    while True:
        try: 
            menu_input = int(input("What would you like to do?"))
            if menu_input ==0:
                main_menu()
            elif menu_input == 1:
                view_couriers()
                back_or_no()
            elif menu_input == 2:
                add_courier_db()
                back_or_no()
            elif menu_input == 3:
                update_courier_db()
                back_or_no()
            elif menu_input == 4:
                delete_courier_db()
                back_or_no()
            else: 
                rich.print("""[#808080] 
Option was not found. 
Try again. [/]""")
                courier_menu()
        except ValueError:
            rich.print("""[#808080] 
Option was not found. 
Try again. [/]""")
            courier_menu()


def products_menu():
    rich.print("""[#A7DBD8]
  Press 0 to return to main menu
  Press 1 to view product list
  Press 2 to add new product
  Press 3 to update existing product
  Press 4 to delete product
[/] """)
    while True:
        try: 
            menu_input = int(input("What would you like to do?"))
            if menu_input ==0:
                main_menu()
            elif menu_input == 1:
                view_products()
                back_or_no()
            elif menu_input == 2:
                add_product_db()
                back_or_no()
            elif menu_input == 3:
                update_product_db()
                back_or_no()
            elif menu_input == 4:
                delete_product_db()
                back_or_no()
            else: 
                rich.print("""[#808080] 
Option was not found. 
Try again. [/]""")
                products_menu()
        except ValueError:
            rich.print("""[#808080] 
Option was not found. 
Try again. [/]""")
            products_menu()


def orders_menu():
    rich.print("""[#F6D55C]
  Press 0 to return to main menu
  Press 1 to view orders
  Press 2 to add order
  Press 3 to update order
  Press 4 to delete order
  Press 5 to check order status
  Press 6 to check which courier has an order
[/] """)
    while True:
        try: 
            menu_input = int(input("What would you like to do?"))
            if menu_input ==0:
                main_menu()
            elif menu_input == 1:
                view_orders()
                back_or_no()
            elif menu_input == 2:
                add_order()
                back_or_no()
            elif menu_input ==3:
                update_order()
                back_or_no()
            elif menu_input ==4:
                delete_order()
                back_or_no()
            elif menu_input == 5:
                check_order_status()
                back_or_no()
            elif menu_input == 6:
                check_courier()
                back_or_no()
            else: 
                rich.print("""[#808080] 
Option was not found. 
Try again. [/]""")
                orders_menu()
        except ValueError:
            rich.print("""[#808080] 
Option was not found. 
Try again. [/]""")
            orders_menu()
            
def save_and_exit():
    while True:
        try:
            export = int(rich.input("[#ED553B] Would you like to export orders, products and couriers as CSV, write 1 for yes or 2 for no [/]"))
            if export == 1:
                product_export_csv()
                courier_export_csv()
                orders_export_csv()
                print("Everything saved to current folder")
                print("""
 ▐█▀▄─ ▀▄─▄▀ █▀▀──█
─▐█▀▀▄ ──█── █▀▀──▀
─▐█▄▄▀ ──▀── ▀▀▀──▄
""")
                exit()
            elif export == 2: 
                print("""
 ▐█▀▄─ ▀▄─▄▀ █▀▀──█
─▐█▀▀▄ ──█── █▀▀──▀
─▐█▄▄▀ ──▀── ▀▀▀──▄
""")
                exit()
            else:
                rich.print("""[#808080]Option was not found. 
Try again. [/]""")
                save_and_exit()
        except ValueError: 
            rich.print("""[#808080]Option was not found. 
Try again. [/]""")

save_and_exit()