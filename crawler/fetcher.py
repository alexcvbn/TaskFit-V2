import httpx
import feedparser

from crawler.sources import SOURCES

def fetch_feed(rss_url: str) -> list[dict]:
    response = httpx.get(rss_url, follow_redirects=True)
    feed = feedparser.parse(response.text)

    posts = []
    for entry in feed.entries:
        posts.append({
            "title": entry.get("title", ""),
            "url": entry.get("link", ""),
            "summary": entry.get("summary", ""),
        })

    return posts

