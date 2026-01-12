from pydantic import BaseModel
from typing import List


class FollowersSummary(BaseModel):
    username: str
    followers_count: int = 0
    following_count: int = 0
    sample_followers: List[str] = []
