from db.crud import create_book, create_category, get_categories
from db.db import Base, Session, engine

Base.metadata.create_all(engine)

with Session() as session:
    if get_categories(session):
        print("База данных уже заполнена")
    else:
        fiction = create_category(session, "Фантастика")

        create_book(
            session,
            "Дюна",
            "Борьба за власть на пустынной планете Арракис",
            890,
            fiction.id,
        )
        create_book(
            session,
            "Солярис",
            "Контакт с разумным океаном далёкой планеты",
            540,
            fiction.id,
        )
        create_book(
            session,
            "451 градус по Фаренгейту",
            "Мир, в котором книги находятся под запретом",
            490,
            fiction.id,
        )

        programming = create_category(session, "Программирование")

        create_book(
            session,
            "Изучаем Python",
            "Подробное введение в язык Python",
            2100,
            programming.id,
        )
        create_book(
            session,
            "Чистый код",
            "Приёмы написания понятного и поддерживаемого кода",
            1350,
            programming.id,
        )
        create_book(
            session,
            "Грокаем алгоритмы",
            "Иллюстрированное введение в алгоритмы",
            990,
            programming.id,
        )

        print("База данных заполнена")
