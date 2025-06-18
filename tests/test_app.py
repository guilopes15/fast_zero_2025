from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero_2025.app import app

client = TestClient(app)


def test_root_deve_retornar_ola_mundo():
    response = client.get('/')
    assert response.json() == {'message': 'Ola mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_ola_mundo_deve_retornar_html():
    response = client.get('/ola')
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
