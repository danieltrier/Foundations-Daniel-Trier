from app.simple_pages.models import Task


def test_get_todo_renders(client):
    # Page loads and renders todo
    response = client.get('/todo')
    assert b'name' in response.data


def test_post_checkout_creates_task(client):
    # Creates an task record
    response = client.post('/todo', data={
        'name': 'Party',
        'date': '2024-12-04',
        'time': '12:34',
        'user_id': '2',

    })
    assert Task.query.first() is not None
