from pydantic import BaseModel
from typing import Optional, List


class PostData(BaseModel):
    post_id: str
    caption: str = ""
    likes: int = 0
    comments: int = 0
    media_type: str = "unknown"
    posted_at: Optional[str] = None
    post_url: str = ""
    media_urls: List[str] = []
