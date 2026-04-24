from src.models.repositories.users_repository import UsersRepositoryInterface

class UserRegister:
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    async def register_user(self, user_data: dict) -> dict:
        self.__validate_user_data(user_data)
        await self.__registry_user(user_data)
        return self.__format_response(user_data)

    def __validate_user_data(self, user_data: dict) -> None:
        age = user_data.get("age")
        uf = user_data.get("uf", "").upper()

        if uf not in ["SC", "RS", "PR"]:
            raise Exception("UF must be one of 'SC', 'RS', or 'PR'.")

        if age is None:
            raise ValueError("Age is required")

        if age < 0 or age > 120:
            raise Exception("Age must be between 0 and 120.")

    async def __registry_user(self, user_data: dict) -> None:
        await self.__users_repository.insert_users(user_data)

    def __format_response(self, user_data: dict) -> dict:
        return {
            "type": "USERS",
            "count": 1,
            "attributes": user_data,
        }