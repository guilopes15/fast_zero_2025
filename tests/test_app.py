from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')
    assert response.json() == {'message': 'Ola mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_ola_mundo_deve_retornar_html(client):
    response = client.get('/ola/')
    assert (
        response.text
        == """
    <html>
      <head>
        <title>Nosso ola mundo!</title>
      </head>
      <body>
        <h1>Ola mundo!</h1>
      </body>
    </html>"""
    )


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@test.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@test.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@test.com',
        'id': 1,
    }


def test_update_user_with_invalid_id(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'bob',
            'email': 'bob@test.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_read_user_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@test.com',
        'id': 1,
    }


def test_read_user_by_id_with_invalid_id(client):
    response = client.get('/users/99')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@test.com',
        'id': 1,
    }


def test_delete_user_with_invalid_id(client):
    response = client.delete('/users/99')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
