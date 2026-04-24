import pytest
from .database_connection_handler import DBConnectionHandler


@pytest.mark.asyncio
@pytest.mark.skip(reason="Requires a running database connection")
async def test_db_connection():
    async with DBConnectionHandler() as db_handler:
        print(db_handler.session)
        assert db_handler.session is not None