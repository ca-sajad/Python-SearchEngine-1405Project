import pytest
from code.urls_to_crawl import FRUITS_TINY_URL
from code import crawler


@pytest.fixture(scope='package')
def run_crawler():
    crawler.crawl(FRUITS_TINY_URL)

