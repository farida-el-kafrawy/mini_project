from mini_project_week2 import courier_list

# # products list
# original_product_list = ["mozarella and pesto panini", "goat's cheese salad",
# "feta and watermelon salad", "iced coffee", "cheese toastie", "mocha"]

my_file = open("product_list.txt", "r")
content_list = my_file.readlines()
content_list = [content_list[3:-2] for content_list in content_list]
product_list = content_list

def add_item():
    user_input = input("What products do you wish to add?")
    if user_input not in product_list:
        product_list.append(user_input)
        return print(f"{user_input.title()} added to products list")
    else:
        return print("Error! Product already on menu.")

# additem= add_item()

def delete_item():
    with open('product_list.txt', 'w') as f:
            for i in range(len(product_list)):
                print(f"{i+1}. {product_list[i].title()} \n")
    user_index_selection = int(input("Which item do you wish to delete? (Select number)"))
    product_name = product_list[user_index_selection-1]
    product_list.pop(user_index_selection-1)
    print(f"{product_name.title()} removed from list")

# deleteitem= delete_item()

def update_item():
    with open('product_list.txt', 'w') as f:
            for i in range(len(product_list)):
                print(f"{i+1}. {product_list[i].title()}")
    user_index_selection = int(input("Which item do you wish to update? (Select number)"))
    user_new_name = input("What is the new product name?")
    product_list[user_index_selection-1] = str(user_new_name)
    print("Product updated")

# updateitem= update_item()
def save_and_exit():
    with open('product_list.txt', 'w') as f:
            for i in range(len(product_list)):
                f.write(f"{i+1}. {product_list[i].title()} \n")
    with open('courier_list.txt', 'w') as f:
            for i in range(len(courier_list)):
                f.write(f"{i+1}. {courier_list[i].title()} \n")
save_and_exit()