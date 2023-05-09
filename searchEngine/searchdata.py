'''
retreives the parameters extracted, calculated, and saved during the crawling process
'''

from searchEngine.constants import PAGE_DATA, IDF_DATA
from searchEngine.db_initialize import database

tf_idf_list = None


def get_outgoing_links(url):
    links = database[PAGE_DATA].find_one({"url": url}, {"_id": 0, "outgoing_links": 1})
    if links:
        return links.get("outgoing_links")
    return None


def get_incoming_links(url):
    links = database[PAGE_DATA].find_one({"url": url}, {"_id": 0, "outgoing_links": 1})
    if links:
        return links.get("outgoing_links")
    return None


def get_tf(url, word):
    tf_dict = database[PAGE_DATA].find_one({"url": url}, {"_id": 0, "tf_list": 1})
    if tf_dict:
        return tf_dict.get("tf_list").get(word, 0)
    return 0


def get_idf(word):
    idf = database[IDF_DATA].find_one({"word": word}, {"_id": 0, "idf": 1})
    if idf:
        return idf.get("idf")
    return 0


def get_tf_idf(url, word):
    global tf_idf_list
    if not tf_idf_list:
        tf_idf_list = list(database[PAGE_DATA].find({}, {"_id": 0, "url": 1, "tf_idf": 1}))
    for item in tf_idf_list:
        if item["url"] == url:
            return item.get("tf_idf").get(word, 0)
    return 0


def get_page_rank(url):
    page_rank = database[PAGE_DATA].find_one({"url": url}, {"_id": 0, "page_rank": 1})
    if page_rank:
        return page_rank.get("page_rank")
    return -1

