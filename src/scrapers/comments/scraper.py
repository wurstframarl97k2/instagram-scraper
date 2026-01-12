from __future__ import annotations

from src.scrapers.base import BaseScraper
from src.scrapers.comments.models import CommentData
from src.utils.logger import get_logger
from src.utils.validation import validate_url

log = get_logger(__name__)


class CommentsScraper(BaseScraper):
    """
    Skeleton instagram comment scraper module for scrape instagram comments workflows.
    """

    def scrape(self, post_url: str, limit: int = 50) -> dict:
        try:
            post_url = validate_url(post_url)
            limit = max(1, min(int(limit), 500))

            comments = [
                CommentData(
                    comment_id="cmt_001",
                    text="Captured using an instagram comment scraper",
                    likes=0,
                    posted_at=None,
                ).model_dump()
            ]

            return self.ok({"post_url": post_url, "comments": comments[:limit], "limit": limit})
        except Exception as e:
            log.exception("Comments scraping failed")
            return self.fail(str(e), data={"post_url": post_url, "comments": []})
