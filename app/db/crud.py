from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db.models import Category, Book


def get_category_by_title(session, title):
    query = select(Category).where(Category.title == title)
    return session.scalar(query)


def get_category(session, category_id):
    return session.get(Category, category_id)


def get_categories(session):
    return session.scalars(select(Category).order_by(Category.id)).all()


def create_category(session, title):
    if get_category_by_title(session, title) is not None:
        raise ValueError(f"Категория {title} уже существует")
    
    category = Category(title=title)
    session.add(category)
    session.commit()
    return category


def update_category(session, category_id, new_title):
    category = get_category(session, category_id)
    if category is None:
        raise ValueError(f"Категория с id {category_id} не найдена")

    same_title = get_category_by_title(session, new_title)
    if same_title is not None and same_title.id != category_id:
        raise ValueError(f"Категория {new_title} уже существует")

    category.title = new_title
    session.commit()
    return category


def delete_category(session, category_id):
    category = get_category(session, category_id)
    if category is None:
        raise ValueError(f"Категория с id {category_id} не найдена")

    session.delete(category)
    session.commit()


def get_book(session, book_id):
    query = select(Book).options(selectinload(Book.category)).where(Book.id == book_id)
    return session.scalar(query)


def get_book_by_title(session, title):
    query = select(Book).where(Book.title == title)
    return session.scalar(query)


def get_books(session):
    query = select(Book).options(selectinload(Book.category)).order_by(Book.id)
    return session.scalars(query).all()


def get_books_by_category(session, category_id):
    query = select(Book).where(Book.category_id == category_id).order_by(Book.id)
    return session.scalars(query).all()


def create_book(session, title, description, price, category_id):
    category = get_category(session, category_id)
    
    if category is None:
        raise ValueError(f"Категория с id {category_id} не найдена")
    
    same_title = get_book_by_title(session, title)
    if same_title is not None:
        raise ValueError(f"Книга с названием {title} уже существует")
    
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")

    book = Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
    )
    session.add(book)
    session.commit()
    return book


def update_book(session, book_id, new_title, new_description, new_price, new_category_id):
    book = get_book(session, book_id)
    if book is None:
        raise ValueError(f"Книга с id {book_id} не найдена")

    category = get_category(session, new_category_id)
    if category is None:
        raise ValueError(f"Категория {new_category_id} не найдена")

    same_title = get_book_by_title(session, new_title)
    if same_title is not None and same_title.id != book_id:
        raise ValueError(f"Название {new_title} уже существует")

    if new_price < 0:
        raise ValueError("Цена не может быть отрицательной")

    book.title = new_title
    book.description = new_description
    book.price = new_price
    book.category_id = new_category_id

    session.commit()
    return book


def delete_book(session, book_id):
    book = get_book(session, book_id)
    if book is None:
        raise ValueError(f"Книга с id {book_id} не найдена")
    session.delete(book)
    session.commit()
