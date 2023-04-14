from app.extensions.database import db
from app.simple_pages.models import User


def test_user_update(client):
    # updates cookie's properties
    user = User(last_name='Trier', first_name='Daniel')
    db.session.add(user)
    db.session.commit()

    user.last_name = 'Mustermann'
    user.save()

    updated_user = User.query.filter_by(first_name='Daniel').first()
    assert updated_user.last_name == 'Mustermann'


def test_user_delete(client):
    # updates cookie's properties
    user = User(last_name='Trier', first_name='Daniel')
    db.session.add(user)
    db.session.commit()

    user.delete()

    deleted_user = User.query.filter_by(first_name='Daniel').first()
    assert deleted_user is None
