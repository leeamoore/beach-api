import strawberry
from strawberry.types import Info


async def edit_comment(info: Info, comment_id: strawberry.ID, comment: str):
    return True
