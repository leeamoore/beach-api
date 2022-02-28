import strawberry
from strawberry.types import Info


async def add_comment(info: Info, beach_id: strawberry.ID, comment: str):
    return True
