# main menu
from section_menus import products_menu, courier_menu, orders_menu, save_everything

def main_menu():
    print("Main Menu")
    main_selection = input("""
  A. Home
  B. Products
  C. Couriers
  D. Orders
  E. Save and Exit

Please make a selection A, B, C or D:
""")
    if main_selection =="B" or main_selection == "b":
        print("""
  Press 0 to return to main menu
  Press 1 to view product list
  Press 2 to add new product
  Press 3 to update existing product
  Press 4 to delete product
    """)
        products_menu()
    if main_selection == "C" or main_selection == "c":
        print("""
  Press 0 to return to main menu
  Press 1 to view courier list
  Press 2 to add new courier
  Press 3 to update existing courier
  Press 4 to delete courier
    """)
        courier_menu()
    if main_selection == "D" or main_selection == "d":
        print("""
  Press 0 to return to main menu
  Press 1 to view orders
  Press 2 to add order
  Press 3 to update order
  Press 4 to delete order
    """)
        orders_menu()
    if main_selection == "E" or main_selection == "e":
        save_everything()
        print("Bye!")
    if main_selection == "A" or main_selection == "a":
        save_everything()
        print("Back to Home")
        main_menu()

# back_or_no = input("Would you like to go back to the main menu? Yes or No?")
#         if back_or_no == "yes" or "Yes":
#             main_menu()
#         elif back_or_no == "no" or "No":
#             save_and_exit()
#             print("Bye! See you again soon!")

main_menu()