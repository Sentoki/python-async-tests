import pytest

from lib.database_pool import DatabasePool
from lib.repository import get_name_by_id
from dotenv import load_dotenv

load_dotenv()

def test_simple():
    assert True

@pytest.mark.asyncio
async def test_async_database_method():
    await DatabasePool.init_pool()
    connection = await DatabasePool.get_pool().acquire()
    name = await get_name_by_id(connection, 1)

    assert name == 'john'