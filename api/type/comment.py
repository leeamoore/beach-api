import strawberry


@strawberry.type
class Comment:
    id: strawberry.ID
    comment: str
    user_id: str
