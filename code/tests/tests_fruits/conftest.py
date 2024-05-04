import pytest
from code.search_code.urls_to_crawl import FRUITS_URL
from code.search_code import crawler


@pytest.fixture(scope='package')
def run_crawler():
    crawler.crawl(FRUITS_URL)

