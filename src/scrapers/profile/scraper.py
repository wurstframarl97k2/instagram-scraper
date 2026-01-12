from __future__ import annotations

from src.scrapers.base import BaseScraper
from src.scrapers.profile.models import ProfileData
from src.utils.logger import get_logger
from src.utils.validation import validate_username

log = get_logger(__name__)


class ProfileScraper(BaseScraper):
    """
    Skeleton instagram profile scraper / instagram account scraper module.

    This intentionally avoids platform-circumvention logic.
    Replace the placeholder sections with compliant data sources.
    """

    def scrape(self, username: str) -> dict:
        try:
            username = validate_username(username)
            profile_url = f"https://www.instagram.com/{username}/"

            mock = ProfileData(
                username=username,
                profile_url=profile_url,
                followers_count=0,
                following_count=0,
                posts_count=0,
                is_verified=False,
            )

            return self.ok({"profile": mock.model_dump()})
        except Exception as e:
            log.exception("Profile scraping failed")
            return self.fail(str(e), data={"profile": {"username": username}})
