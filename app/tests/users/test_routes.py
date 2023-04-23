from app.simple_pages.models import User


def test_cookies_renders_users(client):
    # Page loads and renders users
    new_user = User(last_name='Max', first_name='Trier')
    new_user.save()
    response = client.get('/users')

    assert b'Max' in response.data
