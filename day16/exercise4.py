# Exercise 4: Book Class
# Create a class called Book to represent a basic book.
# The book should have attributes like title, author, and genre. Add a method to display the book's information
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    def __str__(self):
        return "Tilte:{}\nAuthor:{}\nGenre:{}".format(self.title, self.author, self.genre)
book = Book("Diego Go Go GO","Raquel Alarint", "CUENTO")
print(book)