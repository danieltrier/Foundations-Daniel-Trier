from app.app import create_app
from app.simple_pages.models import User
from app.extensions.database import db


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()


users = [
    {
        'last_name': 'Müller',
        'first_name': 'Max',
        'e_mail': 'max.mueller@example.com',
        'password': 'secure_password1'
    },
    {
        'last_name': 'Schmidt',
        'first_name': 'Anna',
        'e_mail': 'anna.schmidt@example.com',
        'password': 'secure_password2'
    },
    {
        'last_name': 'Schneider',
        'first_name': 'Marie',
        'e_mail': 'marie.schneider@example.com',
        'password': 'secure_password3'
    }
]

for user_data in users:
    new_user = User(
        last_name=user_data['last_name'],
        first_name=user_data['first_name'],
        e_mail=user_data['e_mail'],
        password=user_data['password']
    )
    db.session.add(new_user)

db.session.commit()
