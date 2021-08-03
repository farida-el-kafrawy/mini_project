import csv
import mysql.connector
from rich.console import Console

rich = Console()

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE miniproject")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="miniproject"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price DECIMAL(4,2))")

# mycursor.execute("CREATE TABLE couriers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(20))")

def first_products():
    sql = "INSERT INTO products (name,price) VALUES (%s, %s)"
    val = [
("Coke Zero",0.8),
("Sprite",0.9),
("Fanta Lemon",0.8),
("Margharita Pizza",9.0)
]
    mycursor.executemany(sql, val)
    mydb.commit()

# first_products()

def first_couriers():
    sql = "INSERT INTO couriers (name,phone) VALUES (%s, %s)"
    val = [
("Mark", "0327592385"),
("Smith", "032895723"),
("Kale", "0325713523"),
]
    mycursor.executemany(sql, val)
    mydb.commit()
    
# first_couriers()

def add_product_db():
    product_name = input("Enter product name")
    product_price = input("Enter product price")
    if product_name == '' or product_price == '':
        rich.print("""
[#808080]Invalid input.
Try again.[/]
""")
        add_product_db()
    else:
        sql = "INSERT INTO products (name,price) VALUES (%s, %s)"
        val = [
    (product_name, product_price),
    ]
        mycursor.executemany(sql, val)
        mydb.commit()
        print(f"{product_name} added")

def add_courier_db():
    courier_name = input("Enter courier name")
    courier_phone = input("Enter courier phone number")
    if courier_name == '' or courier_phone == '':
        rich.print("""
[#808080]Invalid input.
Try again.[/]
""")
        add_courier_db()
    else:
        sql = "INSERT INTO couriers (name,phone) VALUES (%s, %s)"
        val = [
    (courier_name, courier_phone),
    ]
        mycursor.executemany(sql, val)
        mydb.commit()
        print(f"{courier_name} added")

def view_products():
    mycursor.execute("SELECT id, name FROM products")
    myresult = mycursor.fetchall()
    print("ID. Product Name:")
    for x in myresult:
        print(f"{x[0]}. {x[1]}")
        
def view_couriers():
    mycursor.execute("SELECT id, name FROM couriers")
    myresult = mycursor.fetchall()
    print("ID. Courier Name:")
    for x in myresult:
        print(f"{x[0]}. {x[1]}")
        
def delete_product_db():
    view_products()
    while True:
        try:
            product_name = int(input("Enter product number to delete"))
            sql = "DELETE FROM products WHERE EXISTS id = %s"
            val = (product_name, )
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"Product with id {product_name} removed from list")
        except:
            rich.print("""
[#808080]Invalid input.
Try again.[/]
""")
            delete_product_db()

def delete_courier_db():
    view_couriers()
    while True:
        try: 
            courier_name = int(input("Enter courier number to delete"))
            sql = "DELETE FROM couriers WHERE EXISTS id = %s"
            val = (courier_name, )
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"Courier with id {courier_name} removed from list")
        except:
            rich.print("""
[#808080]Invalid input.
Try again.[/]
""")
            delete_courier_db()

def update_courier_db():
    view_couriers()
    user_index_selection = int(input("""Which item do you wish to update? 
Enter number."""))
    name_or_phone = int(input("""
Enter 1 to update name
Enter 2 to update phone number
Enter 3 to update both
                    """))
    if name_or_phone == 1:
        user_new_name = input("What is the new name?")
        if user_new_name == '':
            print("Try again")
            update_courier_db()
        else:
            sql = '''UPDATE couriers
            SET name = %s
            WHERE id =  %s;'''
            val = (user_new_name, user_index_selection)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Courier updated")
    elif name_or_phone == 2:
        user_new_phone = input("What is the new phone number?")
        if user_new_phone == '':
            print("Try again")
            update_courier_db()
        else:
            sql = '''UPDATE couriers
            SET phone = %s
            WHERE id =  %s;'''
            val = (user_new_phone, user_index_selection)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Courier updated")
    elif name_or_phone ==3:
        user_new_name = input("What is the new name?")
        if user_new_name == '':
            print("Try again")
            update_courier_db()
        else:
            sql1 = '''UPDATE couriers
            SET name = %s
            WHERE id =  %s;'''
            val1 = (user_new_name, user_index_selection)
            mycursor.execute(sql1, val1)
            mydb.commit()
            print("Courier updated")
        user_new_phone = input("What is the new phone number?")
        if user_new_phone == '':
            print("Try again")
            update_courier_db()
        else:
            sql2 = '''UPDATE couriers
            SET phone = %s
            WHERE id =  %s;'''
            val2 = (user_new_phone, user_index_selection)
            mycursor.execute(sql2, val2)
            mydb.commit()
            print("Courier updated")
    else:
        rich.print("""[#808080]Invalid input.
Try again.[/]""")
        update_courier_db()


def update_product_db():
    view_products()
    user_index_selection = int(input("""Which item do you wish to update? 
    Enter number."""))
    name_or_price = int(input("""
    Enter 1 to update name
    Enter 2 to update price
    Enter 3 to update both
                    """))
    if name_or_price == 1:
        user_new_name = input("What is the new name?")
        sql = '''UPDATE products
        SET name = %s
        WHERE id =  %s;'''
        val = (user_new_name, user_index_selection)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Product updated")
    elif name_or_price == 2:
        user_new_price = input("What is the new price?")
        sql = '''UPDATE products
        SET price = %s
        WHERE id =  %s;'''
        val = (user_new_price, user_index_selection)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Product updated")
    elif name_or_price ==3:
        user_new_name = input("What is the new name?")
        sql1 = '''UPDATE products
        SET name = %s
        WHERE id =  %s;'''
        val1 = (user_new_name, user_index_selection)
        mycursor.execute(sql1, val1)
        user_new_phone = input("What is the new price?")
        sql2 = '''UPDATE products
        SET price = %s
        WHERE id =  %s;'''
        val2 = (user_new_phone, user_index_selection)
        mycursor.execute(sql2, val2)
        mydb.commit()
        print("Product updated")
    else:
        rich.print("""[#808080]Invalid input.
Try again.[/]""")
        update_product_db()

def product_export_csv():
    sql = 'select * from products'
    mycursor.execute(sql.encode('utf-8'))
    data = mycursor.fetchall()
    filename = 'products.csv'
    with open(filename,mode='w',encoding='utf-8') as f:
        write = csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)
            
def courier_export_csv():
    sql = 'select * from couriers'
    mycursor.execute(sql.encode('utf-8'))
    data = mycursor.fetchall()
    filename = 'couriers.csv'
    with open(filename,mode='w',encoding='utf-8') as f:
        write = csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)