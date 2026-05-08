from crawler.fetcher import fetch_feed
from crawler.sources import SOURCES


def main():
    for source in SOURCES:
        posts = fetch_feed(source.rss_url)
        print(f"[{source.company}] {len(posts)}개 수집")
        for post in posts[:2]:
            print(f"  - {post['title']}")
        print()


if __name__ == "__main__":
    main()