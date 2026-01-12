from __future__ import annotations

from src.scrapers.base import BaseScraper
from src.scrapers.followers.models import FollowersSummary
from src.utils.logger import get_logger
from src.utils.validation import validate_username

log = get_logger(__name__)


class FollowersScraper(BaseScraper):
    """
    Skeleton instagram follower scraper / instagram followers scraper module.

    Designed for workflows like scrape instagram followers and instagram scraper followers.
    """

    def scrape(self, username: str, limit: int = 50) -> dict:
        try:
            username = validate_username(username)
            limit = max(1, min(int(limit), 500))

            mock = FollowersSummary(
                username=username,
                followers_count=0,
                following_count=0,
                sample_followers=[],
            )

            return self.ok({"followers": mock.model_dump(), "limit": limit})
        except Exception as e:
            log.exception("Followers scraping failed")
            return self.fail(str(e), data={"followers": {"username": username, "sample_followers": []}})
