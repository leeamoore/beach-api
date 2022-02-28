from typing import List, Optional

import strawberry

from .comment import Comment


@strawberry.type
class Beach:
    id: strawberry.ID
    name: str
    rating: Optional[float]
    comments: List[Comment]
    image_urls: List[str]
