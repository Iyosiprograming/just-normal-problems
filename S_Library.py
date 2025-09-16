# Simple Library Search Management System

books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851},
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "year": 1847},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

print("********** Library Search Management **********")

bookname = input("Enter the book name: ").lower()
found = False

for book in books:
    if bookname in book['title'].lower():
        print(f"{book['title']} by {book['author']} ({book['year']})")
        found = True

if not found:
    print("Book Not Found")
