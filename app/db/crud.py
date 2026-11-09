from sqlalchemy import select


def create(session, obj):
    session.add(obj)
    session.commit()
    return obj


def get(session, model, obj_id):
    return session.get(model, obj_id)


def get_all(session, model):
    return session.scalars(select(model).order_by(model.id)).all()


def update(session, obj, **fields):
    for name, value in fields.items():
        setattr(obj, name, value)
    session.commit()
    return obj


def delete(session, obj):
    session.delete(obj)
    session.commit()