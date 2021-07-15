# courier_list = ["Speedy delivery", "Zoom delivery", "Snail delivery"]

# with open("courier_list.txt", "w") as output:
#     output.write(str(courier_list))

my_file = open("courier_list.txt", "r")
content_list = my_file.readlines()
content_list = [content_list[3:-2] for content_list in content_list]
courier_list = content_list

# add to courier list
def add_courier():
    user_input = input("Which courier do you wish to add?")
    if user_input not in courier_list:
        courier_list.append(user_input)
        return print(f"{user_input.title()} added to courier list")
    else:
        return print("Error! Courier already on system.")


# delete courier
def delete_courier():    
    with open('courier_list.txt', 'w') as f:
            for i in range(len(courier_list)):
                print(f"{i+1}. {courier_list[i].title()} \n")
    user_index_selection = int(input("Which item do you wish to delete? (Select number)"))
    product_name = courier_list[user_index_selection-1]
    courier_list.pop(user_index_selection-1)
    print(f"{product_name.title()} removed from list")
    
# update courier

def update_courier():
    with open('courier_list.txt', 'w') as f:
            for i in range(len(courier_list)):
                print(f"{i+1}. {courier_list[i].title()}")
    user_index_selection = int(input("Which courier do you wish to update? (Select number)"))
    user_new_name = input("What is the new courier name?")
    courier_list[user_index_selection-1] = str(user_new_name)
    print("Courier updated")

# updateitem= update_item()
def save_and_exit():
    with open('courier_list.txt', 'w') as f:
            for i in range(len(courier_list)):
                f.write(f"{i+1}. {courier_list[i].title()} \n")