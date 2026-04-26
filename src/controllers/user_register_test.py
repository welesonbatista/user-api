# pylint: disable = C1803
import pytest
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from .user_register import UserRegister


class UserRepositoryMock(UsersRepositoryInterface):

    def __init__(self):
        self.insert_users_att = {}

    async def insert_users(self, user_info: dict) -> None:
        self.insert_users_att["user_data"] = user_info

    async def get_users_by_name(self, user_name: str):
        return []

    async def update_user(self, user_id: int, updated_info: dict):
        return None

    async def delete_user(self, user_id: int) -> None:
        pass

@pytest.mark.asyncio
async def test_register_user():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    user_data = {
        "username": "Joao Silva",
        "age": 30,
        "uf": "SC",
    }

    response = await user_register.register_user(user_data)
    print(response)

    assert response["type"] == "USERS"
    assert response["count"] == 1
    assert response["attributes"] == user_data

@pytest.mark.asyncio
async def test_register_user_error_uf():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_uf_user_data = {
        "username": "Maria Silva",
        "age": 30,
        "uf": "AC",
    }
    with pytest.raises(HttpBadRequestError) as excinfo:
        await user_register.register_user(invalid_uf_user_data)
    assert "UF must be one of" in str(excinfo.value)
    assert user_repository.insert_users_att == {}

@pytest.mark.asyncio
async def test_register_user_error_age():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_age_user_data = {
        "username": "Maria Silva",
        "age": -1,
        "uf": "SC",
    }
    with pytest.raises(HttpBadRequestError) as excinfo:
        await user_register.register_user(invalid_age_user_data)
    assert "Age must be between 0 and 120." in str(excinfo.value)
    assert user_repository.insert_users_att == {}