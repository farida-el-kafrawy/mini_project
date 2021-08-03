# main menu
from final_section_menus import products_menu, courier_menu, orders_menu
from mini_project_week5 import courier_export_csv, product_export_csv
from mini_project_week6 import orders_export_csv
from rich.console import Console


rich = Console()

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
        rich.print("""[#A7DBD8]
  Press 0 to return to main menu
  Press 1 to view product list
  Press 2 to add new product
  Press 3 to update existing product
  Press 4 to delete product
[/] """)
        products_menu()
        rich.print("\n [#228B22] Would you like to go back to the main menu? [/]")
        go_back = int(input("""
Press 1 for Yes
Press 2 for No"""))
        if go_back == 1:
            main_menu()
        else: print("Bye, see you soon!")
    if main_selection == "C" or main_selection == "c":
        rich.print("""[#3CAEA3]
  Press 0 to return to main menu
  Press 1 to view courier list
  Press 2 to add new courier
  Press 3 to update existing courier
  Press 4 to delete courier
[/]  """)
        courier_menu()
        rich.print("\n [#228B22] Would you like to go back to the main menu? [/]")
        go_back = int(input("""
Press 1 for Yes
Press 2 for No"""))
        if go_back == 1:
            main_menu()
        else: print("Bye, see you soon!")
    if main_selection == "D" or main_selection == "d":
        rich.print("""[#F6D55C]
  Press 0 to return to main menu
  Press 1 to view orders
  Press 2 to add order
  Press 3 to update order
  Press 4 to delete order
  Press 5 to check order status
[/] """)
        orders_menu()
        rich.print("\n [#228B22] Would you like to go back to the main menu? [/]")
        go_back = int(input("""
Press 1 for Yes
Press 2 for No"""))
        if go_back == 1:
            main_menu()
        else: print("Bye, see you soon!")
    if main_selection == "E" or main_selection == "e":
        export = int(rich.input("[#ED553B] Would you like to export orders, products and couriers as CSV, write 1 for yes or 2 for no [/]"))
        if export == 1:
            product_export_csv()
            courier_export_csv()
            orders_export_csv()
            print("Bye!")
        else: 
            print("Bye!")
    if main_selection == "A" or main_selection == "a":
        rich.print("[#228B22] Back to Home [/]")
        main_menu()

# back_or_no = input("Would you like to go back to the main menu? Yes or No?")
#         if back_or_no == "yes" or "Yes":
#             main_menu()
#         elif back_or_no == "no" or "No":
#             save_and_exit()
#             print("Bye! See you again soon!")

main_menu()