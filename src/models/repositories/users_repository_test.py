import pytest
from .users_repository import UsersRepository


@pytest.mark.asyncio
@pytest.mark.skip(reason="This test is only for testing the insert_users method.")
async def test_insert_user():
    new_user = {
        "user_name": "testuser",
        "age": 99,
        "uf": "SC"
    }

    repo = UsersRepository()
    await repo.insert_users(new_user)


@pytest.mark.asyncio
async def test_get_users_by_name():
    repo = UsersRepository()
    response = await repo.get_users_by_name("testuser")

    print(response)


@pytest.mark.asyncio
async def test_update_user():
    repo = UsersRepository()

    new_user = {
        "user_name": "update_test_user",
        "age": 20,
        "uf": "MG"
    }

    await repo.insert_users(new_user)

    users = await repo.get_users_by_name("update_test_user")
    user_id = users[0]["id"]

    updated_data = {
        "age": 50,
        "uf": "SP"
    }

    response = await repo.update_user(user_id, updated_data)

    assert response is not None
    assert response.age == 50
    assert response.uf == "SP"


@pytest.mark.asyncio
async def test_delete_user():
    repo = UsersRepository()

    new_user = {
        "user_name": "delete_test_user",
        "age": 40,
        "uf": "PR"
    }

    await repo.insert_users(new_user)

    users = await repo.get_users_by_name("delete_test_user")
    user_id = users[0]["id"]

    await repo.delete_user(user_id)

    response = await repo.get_users_by_name("delete_test_user")

    assert response == []