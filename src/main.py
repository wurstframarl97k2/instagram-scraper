import argparse
from pathlib import Path

from src.config.settings import Settings
from src.utils.io import write_json
from src.utils.logger import get_logger
from src.scrapers.profile.scraper import ProfileScraper
from src.scrapers.followers.scraper import FollowersScraper
from src.scrapers.posts.scraper import PostsScraper
from src.scrapers.comments.scraper import CommentsScraper

log = get_logger(__name__)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="instagram-scraper",
        description="Self-hosted Instagram scraping skeleton (public data only).",
    )
    p.add_argument("--profile", help="Instagram username (without @).")
    p.add_argument("--followers", help="Instagram username to fetch followers summary for.")
    p.add_argument("--posts", help="Instagram username to fetch posts for.")
    p.add_argument("--comments", help="Instagram post URL to fetch comments for.")
    p.add_argument("--out", default="output/result.json", help="Output JSON path.")
    return p


def main() -> int:
    args = build_parser().parse_args()
    settings = Settings()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    result = {"platform": "instagram", "scraper_type": "instagram scraper", "status": "no_op"}

    if args.profile:
        log.info("Scraping profile: %s", args.profile)
        result = ProfileScraper(settings).scrape(username=args.profile)

    if args.followers:
        log.info("Scraping followers: %s", args.followers)
        result = FollowersScraper(settings).scrape(username=args.followers)

    if args.posts:
        log.info("Scraping posts: %s", args.posts)
        result = PostsScraper(settings).scrape(username=args.posts)

    if args.comments:
        log.info("Scraping comments: %s", args.comments)
        result = CommentsScraper(settings).scrape(post_url=args.comments)

    write_json(out_path, result)
    log.info("Wrote output to %s", out_path.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
