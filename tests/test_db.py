from dataclasses import asdict

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fast_zero_2025.models import Todo, User


@pytest.mark.asyncio
async def test_create_user(session: AsyncSession, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='test', email='test@test.com', password='secret'
        )

        session.add(new_user)
        await session.commit()

        user = await session.scalar(
            select(User).where(User.username == 'test')
        )

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@test.com',
        'password': 'secret',
        'created_at': time,
        'updated_at': time,
        'todos': [],
    }


@pytest.mark.asyncio
async def test_create_todo_wrong_state(session, user):
    new_todo = Todo(
        user_id=user.id,
        title='Test',
        description='desc',
        state='error',
    )
    session.add(new_todo)

    await session.commit()

    with pytest.raises(LookupError) as ex:
        await session.scalar(select(Todo).where(Todo.title == 'Test'))

    assert ex.value.args[0] == (
        "'error' is not among the defined enum values. Enum name: todostate. "
        "Possible values: draft, todo, doing, ..., trash"
    )
