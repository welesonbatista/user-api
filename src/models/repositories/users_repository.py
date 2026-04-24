from typing import Any, Dict
from sqlalchemy import insert, select, update, delete
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler
from .interfaces.users_repository import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):

    async def insert_users(self, user_info: Dict [str, Any]) -> None:
        async with DBConnectionHandler() as db:
            assert db.session is not None

            query = insert(Users).values(**user_info)

            await db.session.execute(query)
            await db.session.commit()

    async def update_user(self, user_id: int, updated_info: Dict[str, Any]) -> Any:
        async with DBConnectionHandler() as db:
            assert db.session is not None
            query = (
                update(Users)
                .where(Users.c.id == user_id)
                .values(**updated_info)
                .returning(Users)
            )
            result = await db.session.execute(query)
            await db.session.commit()

            updated_user = result.one_or_none()
            return updated_user
    
    async def get_users_by_name(self, user_name: str) -> list[dict[str, Any]]:
        async with DBConnectionHandler() as db:
            assert db.session is not None

            query = (
                select(Users)
                .where(Users.c.user_name == user_name)
            )

            result = await db.session.execute(query)
            rows = result.fetchall()

            users_list = [dict(row.mapping) for row in rows]
            return users_list

    async def delete_user(self, user_id: int) -> None:
        async with DBConnectionHandler() as db:
            assert db.session is not None

            query = delete(Users).where(Users.c.id == user_id)

            await db.session.execute(query)
            await db.session.commit()