from restaurant import Restaurant



print("************Welcome In Familly Restaurant***********")
    
restaurant= Restaurant()
username = input("enter your usename:")
password = input("enter your password:")
flag =restaurant.admin_login(username, password)
if flag:
    print("Logged In Successfully")



    print("Welcome to our restaurant!")
    restaurant.display_menu()

    while True:
        order_item = input("Enter item code or 'done' to finish: ")
        if order_item == "done":
            restaurant.view_order()
            break
        quantity = int(input("Enter quantity: "))
        restaurant.place_order(order_item, quantity)
        if all(item["quantity"] == 0 for item in restaurant.menu.values()):
            print("Sorry, we're all out of food!")
            break
else:
    print("Invalid credentials")        



