import asyncpg
from os import getenv

class DatabasePool:
    _pool = None

    @classmethod
    async def init_pool(cls):
        if cls._pool is None:
            cls._pool = await asyncpg.create_pool(getenv('DATABASE_URL'))

    @classmethod
    async def close_pool(cls):
        if cls._pool:
            await cls._pool.close()
            cls._pool = None

    @classmethod
    def get_pool(cls):
        return cls._pool