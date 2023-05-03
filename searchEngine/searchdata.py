import json
import os
from constants import *

word_tf_idf_dict = {}           # key: URL, value: a dictionary of idf-tf values (key: word, value: tf-idf)


def get_outgoing_links(url):
    outgoing_links_dict = read_file(LINKS_OUT_FILE_NAME)
    return outgoing_links_dict.get(url, None)


def get_incoming_links(url):
    incoming_links_dict = read_file(LINKS_IN_FILE_NAME)
    return incoming_links_dict.get(url, None)


def get_tf(url, word):
    temp_dict = read_file(TF_FILE_NAME)
    if url in temp_dict:
        word_dict = temp_dict[url]
        if word_dict:
            return float(word_dict.get(word, 0))
    return 0


def get_idf(word):
    word_idf_dict = read_file(IDF_FILE_NAME)
    return word_idf_dict.get(word, 0)


def get_tf_idf(url, word):
    global word_tf_idf_dict
    if not word_tf_idf_dict:
        word_tf_idf_dict = read_file(TF_IDF_FILE_NAME)
    url_dict = word_tf_idf_dict.get(url, {})
    idf_tf = url_dict.get(word, 0)
    return idf_tf


def get_page_rank(url):
    urls_ranks_dict = read_file(PAGE_RANK_FILE_NAME)
    return urls_ranks_dict.get(url, -1)


'''
reads and returns contents of a json file with the name "file_name"
'''
def read_file(file_name):
    with open(os.path.join(BASE_DIR, file_name), "r") as file:
        return json.load(file)

