import strawberry
from strawberry.types import Info


async def delete_comment(info: Info, comment_id: strawberry.ID):
    return True
