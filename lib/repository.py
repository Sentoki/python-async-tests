from asyncpg import Connection


async def get_name_by_id(connection: Connection, name_id: int) -> str | None:
    query = """SELECT * FROM names WHERE id = $1 LIMIT 1;"""

    row = await connection.fetchrow(query, name_id)
    if row:
        return row['name']
    return None
