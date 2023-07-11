# Example 1: Library Management System
Create a Library class that manages a collection of books. The Library class should allow users to add new books, lend books, return books, and display the available books. Each Book should have attributes like title, author, and availability status.

# class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

# class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"{title} is now lent.")
                else:
                    print(f"{title} is not available.")
                return
        print(f"{title} is not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"{title} has been returned.")
                else:
                    print(f"{title} is already available.")
                return
        print(f"{title} is not found in the library.")

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} by {book.author}")

# Usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_available_books()
library.lend_book("The Great Gatsby")
library.lend_book("To Kill a Mockingbird")
library.display_available_books()
library.return_book("To Kill a Mockingbird")
library.display_available_books()

# Example 2: Restaurant Management System
Create classes to represent a restaurant management system. You should have classes for Restaurant, Menu, MenuItem, and Order. The Restaurant class should allow users to add menus, create orders, and display the available menus and items. The Order class should calculate the total price of the order.

# class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

# class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

# class Restaurant:
    def __init__(self):
        self.menus = []

    def add_menu(self, menu):
        self.menus.append(menu)

    def display_available_menus(self):
        print("Available Menus:")
        for menu in self.menus:
            print(f"- {menu.name}")

    def display_menu_items(self, menu_name):
        for menu in self.menus:
            if menu.name == menu_name:
                print(f"Items in {menu_name}:")
                for item in menu.items:
                    print(f"- {item.name} (${item.price})")
                return
        print(f"{menu_name} is not found.")

# Usage:
item1 = MenuItem("Burger", 8.99)
item2 = MenuItem("Pizza", 12.99)
item3 = MenuItem("Salad", 6.99)

menu1 = Menu("Lunch")
menu1.add_item(item1)
menu1.add_item(item2)

menu2 = Menu("Dinner")
menu2.add_item(item2)
menu2.add_item(item3)

restaurant = Restaurant()
restaurant.add_menu(menu1)
restaurant.add_menu(menu2)

restaurant.display_available_menus()
restaurant.display_menu_items("Lunch")
restaurant.display_menu_items("Breakfast")