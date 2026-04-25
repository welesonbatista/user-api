from typing import Any, Dict

import pytest

from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from .user_finder import UserFinder

class UserRepositoryMock(UsersRepositoryInterface):
    def __init__(self) -> None:
        self.get_users_by_name_att = {}    
    async def get_users_by_name(self, user_name : str) -> list[dict]:
        self.get_users_by_name_att["user_name"] = user_name
        return [{"user_name": "Ola0"}, {"user_name": "Mundo"}]

    async def insert_users(self, user_info: Dict[str, Any]) -> None:
        raise NotImplementedError

    async def update_user(self, user_id: int, updated_info: Dict[str, Any]) -> Any:
        raise NotImplementedError

    async def delete_user(self, user_id: int) -> None:
        raise NotImplementedError


@pytest.mark.asyncio
async def test_find_user_by_name():
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)
    user_name = "weleson"

    response = await user_finder.find_user_by_name(user_name)

    assert user_repo.get_users_by_name_att["user_name"] == user_name
    
    assert response["type"] == "USERS"
    assert response["count"] == 2
    assert "attributes" in response
    assert isinstance(response["attributes"], list)
    assert isinstance(response["attributes"][0], dict)
