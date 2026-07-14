from sqlalchemy.orm import Session

from app.models.user import User


def register(db: Session, phone: str):
    user = db.query(User).filter(
        User.phone == phone
    ).first()

    if user:
        return user

    user = User(phone=phone)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user