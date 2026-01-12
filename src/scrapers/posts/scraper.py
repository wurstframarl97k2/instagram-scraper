from __future__ import annotations

from src.scrapers.base import BaseScraper
from src.scrapers.posts.models import PostData
from src.utils.logger import get_logger
from src.utils.validation import validate_username

log = get_logger(__name__)


class PostsScraper(BaseScraper):
    """
    Skeleton instagram post scraper module for workflows like scrape instagram posts and scrape instagram photos.
    """

    def scrape(self, username: str, limit: int = 12) -> dict:
        try:
            username = validate_username(username)
            limit = max(1, min(int(limit), 100))

            # Placeholder post list so pipelines can be wired immediately.
            posts = [
                PostData(
                    post_id="unknown",
                    caption="Sample content collected using instagram scrape workflow",
                    likes=0,
                    comments=0,
                    media_type="image",
                    posted_at=None,
                    post_url=f"https://www.instagram.com/{username}/",
                    media_urls=[],
                ).model_dump()
            ]

            return self.ok({"username": username, "posts": posts[:limit], "limit": limit})
        except Exception as e:
            log.exception("Posts scraping failed")
            return self.fail(str(e), data={"username": username, "posts": []})
