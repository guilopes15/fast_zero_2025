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
