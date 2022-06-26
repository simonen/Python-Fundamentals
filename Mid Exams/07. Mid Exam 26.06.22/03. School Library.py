books = list(input().split("&"))
command = input()

while command != "Done":
    command_list = command.split(" | ")
    action = command_list[0]
    book = command_list[1]
    if action == "Add Book" and book not in books:
        books.insert(0, book)
    elif action == "Take Book" and book in books:
        books.remove(book)
    elif action == "Insert Book" and book not in books:
        books.append(book)
    elif action == "Check Book":
        if 0 <= int(book) < len(books):
            print(books[int(book)])
    elif action == "Swap Books" and book in books:
        book2 = command_list[2]
        if book2 in books:
            book_index = books.index(book)
            book2_index = books.index(book2)
            books[book_index], books[book2_index] = books[book2_index], books[book_index]

    command = input()

books = ", ".join(books)
print(books)