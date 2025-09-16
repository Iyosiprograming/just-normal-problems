
books = {
    1: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 3},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 2},
    3: {"title": "1984", "author": "George Orwell", "copies": 4},
    4: {"title": "Pride and Prejudice", "author": "Jane Austen", "copies": 5},
    5: {"title": "The Hobbit", "author": "J.R.R. Tolkien", "copies": 3},
    6: {"title": "Moby Dick", "author": "Herman Melville", "copies": 2},
    7: {"title": "War and Peace", "author": "Leo Tolstoy", "copies": 1},
    8: {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "copies": 3},
    9: {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "copies": 2},
    10: {"title": "Brave New World", "author": "Aldous Huxley", "copies": 4}
}


members = {
    1: {"name": "Alice Johnson", "borrowed_books": [], "fine": 0},
    2: {"name": "Bob Smith", "borrowed_books": [], "fine": 0},
    3: {"name": "Carol Davis", "borrowed_books": [], "fine": 0},
    4: {"name": "David Lee", "borrowed_books": [], "fine": 0},
    5: {"name": "Eva Martinez", "borrowed_books": [], "fine": 0},
    6: {"name": "Frank Wilson", "borrowed_books": [], "fine": 0},
    7: {"name": "Grace Taylor", "borrowed_books": [], "fine": 0}
}

print("📚 Library Management System")
Member_Check = input("Enter Your Name: ")

found_member = None
for member_id, member_details in members.items():
    if member_details["name"].lower() == Member_Check.lower():
        found_member = (member_id, member_details)
        break

if found_member:
    member_id, member_details = found_member
    print(f"✅ Welcome {member_details['name']}! (Member ID: {member_id})")

    howmanybooks = int(input("Enter How Many Books You Want to Borrow: "))
    if howmanybooks > 3:
        print("You Can't Borrow More Than 3 Books")
    else:

        for i in range(howmanybooks):
            bookname = input(f"Enter Book Name ({i+1}/{howmanybooks}): ")
            found_book = None
            for book_id, book_details in books.items():
                if book_details["title"].lower() == bookname.lower():
                    found_book = (book_id, book_details)
                    break
            
            if found_book:
                book_id, book_details = found_book
                if book_details["copies"] > 0:
                    print(f"📖 Book Found: {book_details['title']} (Book ID: {book_id})")
                    members[member_id]["borrowed_books"].append(book_details["title"])
                    books[book_id]["copies"] -= 1  
                else:
                    print(f"❌ Sorry, {book_details['title']} is out of stock.")
            else:
                print(f"❌ Book '{bookname}' Not Found In The Library")

    print(f"\n📌 {member_details['name']}, you borrowed: {members[member_id]['borrowed_books']}")
else:
    print("❌ Member not found.")
