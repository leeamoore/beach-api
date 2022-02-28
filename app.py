import os

import asyncpg
import uvicorn
from starlette.applications import Starlette
from strawberry.asgi import GraphQL

from api.schema import schema

graphql_app = GraphQL(schema)


async def startup():
    app.state.asyncpg_pool = await asyncpg.create_pool(os.environ["PG_DSN"])


app = Starlette(on_startup=[startup])
app.add_route("/graphql", graphql_app)

if __name__ == "__main__":
    os.environ["PG_DSN"] = "postgres://postgres:password@127.0.0.1/beaches"
    uvicorn.run("app:app", host="0.0.0.0", port=8000, workers=2)
