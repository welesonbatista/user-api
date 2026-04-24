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