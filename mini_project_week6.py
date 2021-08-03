from mini_project_week5 import view_couriers, view_products
import csv
import mysql.connector
import json
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="miniproject"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), phone VARCHAR(20), courier INT, status VARCHAR(50),  items VARCHAR(255))")

def first_orders():
    sql = "INSERT INTO orders (name,address,phone,courier,status,items) VALUES (%s, %s, %s, %s, %s, %s)"
    val = [
("Margie","SW19 4QT, Merton", "023471835",2,"Delivered", "3,6,5"),
("Margaret","Windermere Close Essex C4F 3QS","0783274234",4,"Delivered", "9,8,1,2"),
("Milly","Waterway Singapore","03257365326",2,"With courier", "3,4"),
("Michelle","Fiji Road","083275235",4,"Delivered", "5,5")
]
    mycursor.executemany(sql, val)
    mydb.commit()

# first_orders()   

def add_order():
    customer_name = input("Enter customer name")
    customer_address = input("Enter customer address")
    customer_phone = input("Enter customer phone number")
    view_products()
    items_str = str(input("Enter product ids separated by a comma: "))
    view_couriers()
    courier_number= input("Which courier is delivering this order. Select number please.")
    sql = "INSERT INTO orders (name,address,phone,courier,status,items) VALUES (%s, %s, %s, %s, %s, %s)"
    val = [
(customer_name, customer_address, customer_phone, courier_number, "Preparing", items_str),
]
    mycursor.executemany(sql, val)
    mydb.commit()
    print("Order added")
    
def view_orders():
    mycursor.execute("SELECT * FROM orders")
    myresult = mycursor.fetchall()
    print("Orders:")
    for x in myresult:
        print(f"{x[0]}. {x[1]}, {x[2]}, {x[3]}, {x[4]}, {x[5]}, {x[6]} ")
        

def update_order():
    view_orders()
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
        if update_name == '':
            print("Try again")
            update_order()
        else:
            sql = '''UPDATE orders
            SET name = %s
            WHERE id =  %s;'''
            val = (update_name, update_choice)
            mycursor.execute(sql, val)
            mydb.commit()
    elif update_property ==2:
        update_address= input("Enter new address")
        if update_address == '':
            print("Try again")
            update_order()
        else:
            sql = '''UPDATE orders
            SET address = %s
            WHERE id =  %s;'''
            val = (update_address, update_choice)
            mycursor.execute(sql, val)
            mydb.commit()
    elif update_property ==3:
        update_phone = input("Enter new phone number")
        if update_property == '':
            print("Try again")
            update_order()
        else:
            sql = '''UPDATE orders
            SET phone = %s
            WHERE id =  %s;'''
            val = (update_phone, update_choice)
            mycursor.execute(sql, val)
            mydb.commit()
    elif update_property ==4:
        view_couriers()
        update_courier= input("Which courier is delivering this order. Select number please.")
        if update_courier == '':
            print("Try again")
            update_order()
        else:
            sql = '''UPDATE orders
            SET address = %s
            WHERE id =  %s;'''
            val = (update_courier, update_choice)
            mycursor.execute(sql, val)
            mydb.commit()
    elif update_property ==5:
        update_status = int(input("""
Enter new status
1. Preparing
2. With courier
3. Delivered
    """))
        if update_status ==3:
            sql = '''UPDATE orders
            SET status = 'Delivered'
            WHERE id =  %s;'''
            val = (update_choice,)
            mycursor.execute(sql, val)
            mydb.commit()
        elif update_status ==2:
            sql = '''UPDATE orders
            SET status = 'With courier'
            WHERE id =  %s;'''
            val = (update_choice,)
            mycursor.execute(sql, val)
            mydb.commit()
        elif update_status ==1:
            sql = '''UPDATE orders
            SET status = 'Preparing'
            WHERE id =  %s;'''
            val = (update_choice,)
            mycursor.execute(sql, val)
            mydb.commit()
        print("Order delivery status updated")
    else:
        print("Please try again")
        update_order()
    

def delete_order():
    view_orders()
    order_to_delete = int(input("Which order do you wish to delete? (Select number)"))
    sql = "DELETE FROM orders WHERE id = %s"
    val = (order_to_delete, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Product with id {order_to_delete} removed from list")

def orders_export_csv():
    sql = 'select * from orders'
    mycursor.execute(sql.encode('utf-8'))
    data = mycursor.fetchall()
    def get_filename_datetime():
        return "orders-" + str(date.today()) + ".csv"
    name = get_filename_datetime()
    path = "C:/Users/farid/Documents/Data Engineering/Mini_project/" + name
    with open(path,mode='w',encoding='utf-8') as f:
        write = csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)
            
def check_order_status():
    mycursor.execute("SELECT * FROM orders ORDER BY status DESC")
    myresult = mycursor.fetchall()
    print("Orders:")
    for x in myresult:
        print(f"{x[0]}. {x[1]}, {x[2]}, {x[3]}, {x[4]}, {x[5]}, {x[6]} ")
        
def check_courier():
    mycursor.execute("SELECT * FROM orders ORDER BY courier")
    myresult = mycursor.fetchall()
    print("Orders:")
    for x in myresult:
        print(f"{x[0]}. {x[1]}, {x[2]}, {x[3]}, COURIER: {x[4]}, {x[5]}, {x[6]} ")
        