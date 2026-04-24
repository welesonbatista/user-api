from abc import ABC, abstractmethod
from typing import Any, Dict


class UsersRepositoryInterface(ABC):
  
    @abstractmethod
    async def insert_users(self, user_info: Dict [str, Any]) -> None: pass
        

    @abstractmethod
    async def update_user(self, user_id: int, updated_info: Dict[str, Any]) -> Any: pass

    @abstractmethod
    async def get_users_by_name(self, user_name: str) -> list[dict[str, Any]]: pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None: pass
