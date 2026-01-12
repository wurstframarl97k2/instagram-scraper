from src.config.settings import Settings
from src.scrapers.profile.scraper import ProfileScraper
from src.scrapers.followers.scraper import FollowersScraper
from src.scrapers.posts.scraper import PostsScraper
from src.scrapers.comments.scraper import CommentsScraper


def test_smoke_profile():
    out = ProfileScraper(Settings()).scrape("example_account")
    assert out["platform"] == "instagram"
    assert out["status"] in ("success", "error")


def test_smoke_followers():
    out = FollowersScraper(Settings()).scrape("example_account")
    assert out["platform"] == "instagram"
    assert out["status"] in ("success", "error")


def test_smoke_posts():
    out = PostsScraper(Settings()).scrape("example_account")
    assert out["platform"] == "instagram"
    assert out["status"] in ("success", "error")


def test_smoke_comments():
    out = CommentsScraper(Settings()).scrape("https://www.instagram.com/p/ABC123/")
    assert out["platform"] == "instagram"
    assert out["status"] in ("success", "error")
