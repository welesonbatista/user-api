from src.controllers.interfaces.user_finder import UserFinderInterface
from src.models.repositories.users_repository import UsersRepositoryInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    async def find_user_by_name(self, user_name: str) -> dict:
        users = await self.__users_repository.get_users_by_name(user_name)
        return self.__format_response(users)
    def __format_response(self, users: list[dict]) -> dict:
        return {
            "type": "USERS",
            "count": len(users),
            "attributes": users,
        }
