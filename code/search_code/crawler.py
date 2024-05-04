import json
import math
import os
from code.search_code import webdev
from code.search_code import matmult
from code.search_code.constants import *
from code.search_code.searchdata import clear_word_tf_idf_dict


def crawl(seed):
    clear_word_tf_idf_dict()
    delete_files(BASE_DIR)
    if not os.path.isdir(BASE_DIR):
        os.makedirs(BASE_DIR)

    queue_urls = [seed]
    processed_urls = []
    words_count_dict = {}           # key: word, value: occurrences of the word per page
    words_rel_freq_dict = {}        # key: URL, value: dictionary of rel freq of words in the URL (key: word, value: tf)
    links_dict = {}                 # key: URL, value: outgoing links in the URL
    titles = []

    while queue_urls:
        url = queue_urls[0]
        # finding base URL
        url_list = url.split(SLASH)
        url_name_index = url.find(url_list[-1])
        base_url = url[:url_name_index]
        # reading webpage html
        page_content = webdev.read_url(url)

        title = extract_title(page_content)
        titles.append(title)

        word_list = extract_words(page_content)

        link_list = extract_links(base_url, page_content)
        for link in link_list:
            if link not in queue_urls and link not in processed_urls:
                queue_urls.append(link)
        words_count_dict, words_rel_freq_dict[url] = calculate_word_freq(words_count_dict, word_list)
        links_dict[url] = link_list
        processed_urls.append(queue_urls.pop(0))
    write_tf_data(words_rel_freq_dict)
    write_idf_data(words_count_dict, len(processed_urls))
    write_tf_idf_data(processed_urls, words_rel_freq_dict)
    write_inout_links(links_dict)
    write_urls(processed_urls, titles)
    write_page_rank(processed_urls, links_dict)
    return len(processed_urls)


'''
deletes files in the "path" directory and the directory itself
'''
def delete_files(path):
    if os.path.exists(path):
        list_files = os.listdir(path)
        for file in list_files:
            os.remove(os.path.join(path, file))
        os.rmdir(path)


'''
finds and returns title of the webpage
'''
def extract_title(text):
    title_index_start = text.find(TITLE_TAG_START) + len(TITLE_TAG_START)
    title_index_end = text.find(TITLE_TAG_END)
    return text[title_index_start: title_index_end]


'''
finds words in a webpage html (text) if the words are separated by a new line or space
returns them as a list
'''
def extract_words(text):
    words = []
    text_list = text.split(LINK_TAG_START)
    for item_1 in text_list:
        if PARA_TAG_END in item_1:
            item_list = item_1.split(NEW_LINE)
            for item_2 in item_list:
                if item_2:
                    if item_2[0] != LT_SIGN or \
                            (item_2[0] == LT_SIGN and item_2[-1] != GT_SIGN):
                        word_list = item_2.split(SPACE)
                        for word in word_list:
                            if word and (LT_SIGN not in word) and (GT_SIGN not in word):
                                words.append(word)
    return words


'''
finds links in a webpage html and returns them as a list
'''
def extract_links(base_url, text):
    link_list = []
    text = text.replace(SPACE, "")
    text_list = text.split(HREF_START)
    for item in text_list:
        if LINK_TAG_END in item:
            gt_sign_index = item.index(GT_SIGN)
            if item[1] == DOT and item[2] == SLASH:
                link_rel = item[3: gt_sign_index - 1]
                link_abs = base_url + link_rel
            else:
                link_abs = item[1: gt_sign_index - 1]
            link_list.append(link_abs)
    return link_list


'''
calculates relative frequencies of list of input words and write them to a dictionary (word_dict)
calculates number of unique words and add them to a dictionary (words_count_dict)   
'''
def calculate_word_freq(words_count_dict, word_list):
    word_count = len(word_list)
    word_dict = {}
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    for key, value in word_dict.items():
        words_count_dict[key] = words_count_dict.get(key, 0) + 1
        word_dict[key] = value / word_count
    return words_count_dict, word_dict


'''
writes a dictionary tf values to a json file
key: URL, value: dictionary of tf values
example:
"http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html": {
        "kiwi": 0.8,
        "banana": 0.2,
    }
'''
def write_tf_data(words_dict):
    write_file(TF_FILE_NAME, words_dict)


'''
calculates idf values and writes them as a dictionary to a json file
key: word, value: idf
'''
def write_idf_data(word_count_dict, page_counter):
    word_idf_dict = {word: math.log2(page_counter / (1 + word_count_dict[word]))
                     for word in word_count_dict.keys()}
    write_file(IDF_FILE_NAME, word_idf_dict)


'''
reads idf values from a file, get tf values as input (words_rel_freq_dict)
calculates idf-tf values and writes them as a dictionary to a json file
key: URL, value: dictionary of tf-idf values
example:
"http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html": {
        "kiwi": 0.038726093486678055,
        "apple": 0.07447019235682993,
    }
'''
def write_tf_idf_data(urls, words_rel_freq_dict):
    with open(os.path.join(BASE_DIR, IDF_FILE_NAME), "r") as idf_file:
        word_idf_dict = json.load(idf_file)
    idf_tf_dict = {}
    for url in urls:
        temp_dict = {}
        for word in word_idf_dict:
            idf = word_idf_dict.get(word, 0)
            tf_dict = words_rel_freq_dict.get(url, None)
            if tf_dict:
                tf = float(tf_dict.get(word, 0))
                idf_tf = math.log2(1 + tf) * idf
                temp_dict[word] = idf_tf
        idf_tf_dict[url] = temp_dict

    write_file(TF_IDF_FILE_NAME, idf_tf_dict)


'''
writes a dictionary of incoming/outgoing links to a json file, 
key: URL, value: linked URLs
'''
def write_inout_links(links_dict):
    # finding incoming links
    incoming_links_dict = {}
    for url_1, url_link_list in links_dict.items():
        for url_2 in url_link_list:
            if not incoming_links_dict.get(url_2, None):
                incoming_links_dict[url_2] = []
            incoming_links_dict[url_2].append(url_1)

    write_file(LINKS_OUT_FILE_NAME, links_dict)
    write_file(LINKS_IN_FILE_NAME, incoming_links_dict)


'''
writes a list of dictionaries of URLs to a json file, with keys and values
example:
{
    "url": "http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html",
    "link_rel": "N-0.html",
    "title": "N-0"
}
'''
def write_urls(urls, titles):
    list_urls = []
    for i, url in enumerate(urls):
        last_dash = url.rfind(SLASH)
        link_rel = url[last_dash + 1:]
        temp_dict = {URL: url, LINK_REL: link_rel, TITLE: titles[i]}
        list_urls.append(temp_dict)
    write_file(URLS_FILE_NAME, list_urls)


'''
calculates page rank of crawled pages, based on Random Surfer Model
writes a dictionary of page rank values to a json file
key: URL, value: page rank
'''
def write_page_rank(urls, links_dict):
    url_count = len(urls)
    adjacency_matrix = [[0] * len(urls) for _ in range(url_count)]
    outgoing_links_dict = links_dict
    # creating adjacency matrix
    for i, url in enumerate(urls):
        outgoing_links = outgoing_links_dict[url]
        for j, outgoing_link in enumerate(outgoing_links):
            index = urls.index(outgoing_link)
            adjacency_matrix[i][index] = 1
    for i, row in enumerate(adjacency_matrix):
        sum_row = sum(row)
        adjacency_matrix[i] = [item / sum_row * (1 - ALPHA) + ALPHA / url_count for item in row]
    # page rank calculations
    array_1 = [[1 / url_count] * url_count]
    error = 1
    while error > THRESHOLD:
        array_2 = matmult.matrix_mult(array_1, adjacency_matrix)
        error = matmult.euclidean_dist(array_1, array_2)
        array_1 = array_2
    temp_dict = {urls[i]: rank for i, rank in enumerate(array_1[0])}
    # write to a json file
    write_file(PAGE_RANK_FILE_NAME, temp_dict)


'''
write input data to a file with the name "file_name" in the base directory
'''
def write_file(file_name, data):
    with open(os.path.join(BASE_DIR, file_name), "w") as file:
        json.dump(data, file, indent=4)


