from db.crud import create
from db.db import Base, Session, engine
from db.models import Book, Category

Base.metadata.create_all(engine)

with Session() as session:
    fiction = create(session, Category(title="Фантастика"))
    programming = create(session, Category(title="Программирование"))

    books = [
        Book(title="Дюна", description="Борьба за власть на пустынной планете Арракис", price=890, category=fiction),
        Book(title="Солярис", description="Контакт с разумным океаном далёкой планеты", price=540, category=fiction),
        Book(title="451 градус по Фаренгейту", description="Мир, в котором книги находятся под запретом", price=490, category=fiction),
        Book(title="Изучаем Python", description="Подробное введение в язык Python", price=2100, category=programming),
        Book(title="Чистый код", description="Приёмы написания понятного и поддерживаемого кода", price=1350, category=programming),
        Book(title="Грокаем алгоритмы", description="Иллюстрированное введение в алгоритмы", price=990, category=programming),
    ]
    for book in books:
        create(session, book)

print("База данных заполнена")