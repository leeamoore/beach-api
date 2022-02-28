from typing import Optional

import strawberry
from strawberry.types import Info

from ..type import Beach
from ..type.comment import Comment


async def beach(info: Info, id: strawberry.ID) -> Optional[Beach]:

    # get beach page based on count and starting index
    query = """
        SELECT 
            beach.id, 
            beach.name,
            array(
                SELECT
                    (
                        beach_comment.id, 
                        beach_comment.comment, 
                        beach_comment.user_id
                    )
                FROM 
                    beach_comment 
                WHERE 
                    beach_comment.beach_id = beach.id
            ) AS comments,
            array(
                SELECT
                    beach_image.url
                FROM
                    beach_image
                WHERE
                    beach_image.beach_id = beach.id
            ) AS image_urls,
            AVG(beach_rating.rating) AS rating 
        FROM
            beach
        LEFT JOIN
            beach_rating
        ON
            beach.id = beach_rating.beach_id
        WHERE
            beach.id = $1
        GROUP BY
            beach.id
    """
    pool = info.context["request"].app.state.asyncpg_pool
    beach = await pool.fetchrow(query, int(id))

    # format beach as graphql response type
    return (
        Beach(
            id=beach["id"],
            name=beach["name"],
            rating=beach["rating"],
            comments=[
                Comment(id=comment[0], comment=comment[1], user_id=comment[2])
                for comment in beach["comments"]
            ],
            image_urls=beach["image_urls"],
        )
        if beach
        else None
    )
