from dataclasses import dataclass

@dataclass

class BolgSource:
    company: str
    rss_url: str

SOURCES: list[BolgSource] = [
    BolgSource(company = "kakao", rss_url = "https://tech.kakao.com/feed"),
    BolgSource(company = "toss", rss_url = "https://toss.tech/rss.xml"),
    BolgSource(company = "daangn", rss_url = "https://medium.com/feed/daangn"),
    BolgSource(company = "coupang", rss_url = "https://medium.com/feed/coupang-engineering"),
]

