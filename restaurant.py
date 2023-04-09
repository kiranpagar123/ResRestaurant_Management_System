class Restaurant:
    def __init__(self):
        self.menu = {
            "I001": {"name": "Pizza", "price": 9.99, "quantity": 10},
            "I002": {"name": "Burger", "price": 6.99, "quantity": 15},
            "I003": {"name": "Fries", "price": 3.99, "quantity": 20},
            "I004": {"name": "Hot Dog", "price": 5.99, "quantity": 12},
            "I005": {"name": "Chicken Wings", "price": 8.99, "quantity": 18},
        }
        self.total_price = 0
        self.order = {}



    def admin_login(self, username, password):
        if username == "admin" and password == "admin":
            return True
        return False    

    def display_menu(self):
        print("Here is our menu:")
        for item in self.menu:
            print(f"{item}: {self.menu[item]['name']} - ${self.menu[item]['price']}")

    def place_order(self, order_item, quantity):
        if order_item not in self.menu:
            print("Sorry, that item is not on our menu.")
            return
        if quantity > self.menu[order_item]["quantity"]:
            print("Sorry, we don't have enough of that item in stock.")
            return
        price = self.menu[order_item]["price"] * quantity
        self.total_price += price
        self.menu[order_item]["quantity"] -= quantity
        if order_item not in self.order:
            self.order[order_item] = quantity
        else:
            self.order[order_item] += quantity
        print(f"{quantity} {self.menu[order_item]['name']}(s) added to your order. Your total is now ${self.total_price:.2f}.\n")

    def view_order(self):
        print("Your order is:")
        for item in self.order:
            print(f"{self.order[item]} {self.menu[item]['name']} - ${self.menu[item]['price']} each")
        print(f"\nYour total bill is ${self.total_price:.2f}.")
