# Advanced Exercise 1: Online Ticket Booking System
Create classes to represent an online ticket booking system. You should have classes for User, Movie, Theater, Showtime, and Booking. Users can search for movies, view available showtimes, and book tickets.

# class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

# class Theater:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.showtimes = []

    def add_showtime(self, showtime):
        self.showtimes.append(showtime)

# class Showtime:
    def __init__(self, movie, time):
        self.movie = movie
        self.time = time

# class User:
    def __init__(self, name):
        self.name = name

# class Booking:
    def __init__(self, user, showtime):
        self.user = user
        self.showtime = showtime

    def display_booking_info(self):
        print(f"Booking for {self.user.name}: {self.showtime.movie.title} at {self.showtime.time}")

# Usage:
movie1 = Movie("Inception", "Sci-Fi")
movie2 = Movie("The Dark Knight", "Action")

showtime1 = Showtime(movie1, "2023-07-15 14:00")
showtime2 = Showtime(movie2, "2023-07-15 16:30")

theater = Theater("CinemaPlex", "City Center")
theater.add_showtime(showtime1)
theater.add_showtime(showtime2)

user1 = User("Alice")
user2 = User("Bob")

booking1 = Booking(user1, showtime1)
booking2 = Booking(user2, showtime2)

booking1.display_booking_info()
booking2.display_booking_info()

# Advanced Exercise 2: Bank Transaction System
Create classes to represent a bank transaction system. You should have classes for Bank, Account, Transaction, and Customer. Customers can open accounts, perform transactions, and view their account balances.

# class Transaction:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

# class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(amount, "Deposit"))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(Transaction(amount, "Withdrawal"))
        else:
            print("Insufficient balance!")

# class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def view_accounts(self):
        print(f"Accounts for {self.name}:")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: {account.balance}")

# Usage:
account1 = Account("12345", 1000)
account2 = Account("67890", 500)

customer1 = Customer("Alice")
customer1.open_account(account1)
customer1.open_account(account2)

account1.deposit(500)
account1.withdraw(200)

customer1.view_accounts()
