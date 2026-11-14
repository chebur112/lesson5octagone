from db.crud import get_books, get_categories
from db.db import Session

with Session() as session:
    print("Категории:")
    for category in get_categories(session):
        print(f"{category.id}. {category.title} (книг: {len(category.books)})")

    print()
    print("Книги:")
    for book in get_books(session):
        category = book.category.title
        print(f"{book.id}. {book.title} | {category} | {book.price} руб.")
        print(f"   {book.description}")
