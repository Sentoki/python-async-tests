import asyncio

from lib.database_pool import DatabasePool
from lib.repository import get_name_by_id
from dotenv import load_dotenv

load_dotenv()

async def main():
    await DatabasePool.init_pool()
    connection = await DatabasePool.get_pool().acquire()
    name = await get_name_by_id(connection, 1)

    print(name)


asyncio.run(main())
