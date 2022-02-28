import strawberry
from strawberry.types import Info


async def rate_beach(info: Info, beach_id: strawberry.ID, rating: int):
    return True
