import typing

import strawberry

import api.mutation as mutation
import api.query as query

from .type import Beach


@strawberry.type
class Query:
    beach: typing.Optional[Beach] = strawberry.field(resolver=query.beach)
    beaches: typing.List[Beach] = strawberry.field(resolver=query.beaches)


@strawberry.type
class Mutation:
    add_comment: bool = strawberry.field(resolver=mutation.add_comment)
    delete_comment: bool = strawberry.field(resolver=mutation.delete_comment)
    edit_comment: bool = strawberry.field(resolver=mutation.edit_comment)
    rate_beach: bool = strawberry.field(resolver=mutation.rate_beach)


schema = strawberry.Schema(query=Query, mutation=Mutation)
