from db.crud import get_all
from db.db import Session
from db.models import Book, Category

with Session() as session:
    print("Категории:")
    for category in get_all(session, Category):
        print(f"{category.id}. {category.title}")

    print("\nКниги:")
    for book in get_all(session, Book):
        print(f"{book.id}. {book.title} | {book.category.title} | {book.price} руб.")
        print(f"   {book.description}")