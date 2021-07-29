import csv
import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Noorsis4"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mini_project")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Noorsis4",
  database="mini_project"
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
    print("Products:")
    for x in myresult:
        print(f"{x[0]}. {x[1]}")
        
def view_couriers():
    mycursor.execute("SELECT id, name FROM couuriers")
    myresult = mycursor.fetchall()
    print("Couriers:")
    for x in myresult:
        print(f"{x[0]}. {x[1]}")
        
def delete_product_db():
    view_products()
    product_name = int(input("Enter product number to delete"))
    sql = "DELETE FROM products WHERE id = %s"
    val = (product_name, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Product with id {product_name} removed from list")

def delete_courier_db():
    view_couriers()
    courier_name = int(input("Enter courier number to delete"))
    sql = "DELETE FROM couriers WHERE id = %s"
    val = (courier_name, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Courier with id {courier_name} removed from list")

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
        sql = '''UPDATE couriers
        SET name = %s
        WHERE id =  %s;'''
        val = (user_new_name, user_index_selection)
        mycursor.execute(sql, val)
        mydb.commit()
    elif name_or_phone == 2:
        user_new_phone = input("What is the new phone number?")
        sql = '''UPDATE couriers
        SET phone = %s
        WHERE id =  %s;'''
        val = (user_new_phone, user_index_selection)
        mycursor.execute(sql, val)
        mydb.commit()
    elif name_or_phone ==3:
        user_new_name = input("What is the new name?")
        sql1 = '''UPDATE couriers
        SET name = %s
        WHERE id =  %s;'''
        val1 = (user_new_name, user_index_selection)
        mycursor.execute(sql1, val1)
        user_new_phone = input("What is the new phone number?")
        sql2 = '''UPDATE couriers
        SET phone = %s
        WHERE id =  %s;'''
        val2 = (user_new_phone, user_index_selection)
        mycursor.execute(sql2, val2)
        mydb.commit()
    print("Courier updated")
    

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
    elif name_or_price == 2:
        user_new_price = input("What is the new price?")
        sql = '''UPDATE products
        SET price = %s
        WHERE id =  %s;'''
        val = (user_new_price, user_index_selection)
        mycursor.execute(sql, val)
        mydb.commit()
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
    
def product_export_csv():
    SQLview = 'SELECT * FROM products;'
    mycursor.execute(SQLview)
    with open('products.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ i[0] for i in mycursor.description ]) 
            
view_couriers()
view_products()