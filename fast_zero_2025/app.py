from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero_2025.routers import auth, todos, users
from fast_zero_2025.schemas import Message

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'Ola mundo!'}


@app.get('/ola/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
async def ola_mundo():
    return """
    <html>
      <head>
        <title>Nosso ola mundo!</title>
      </head>
      <body>
        <h1>Ola mundo!</h1>
      </body>
    </html>"""
