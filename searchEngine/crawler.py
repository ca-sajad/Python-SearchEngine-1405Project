from searchEngine import webdev
from searchEngine.constants import *
from searchEngine.matmult import *
from collections import deque
from searchEngine.db_initialize import database

'''
receives a url as seed and calculates tf, idf, tf-idf, and page rank values of the seed and all connected urls 
'''
def crawl(seed):
    url_stack = deque()
    url_stack.append(seed)
    processed_urls = []
    words_count_dict = {}  # key: word, value: occurrences of the word per page
    words_rel_freq_dict = {}  # key: URL, value: dictionary of rel freq of words in the URL (key: word, value: tf)
    links_dict = {}  # key: URL, value: outgoing links in the URL
    titles = []

    while len(url_stack) > 0:
        url = url_stack.pop()
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
            if link not in url_stack and link not in processed_urls:
                url_stack.append(link)
        words_count_dict, words_rel_freq_dict[url] = calculate_word_freq(words_count_dict, word_list)
        links_dict[url] = link_list
        processed_urls.append(url)
    write_tf_data(words_rel_freq_dict)
    write_idf_data(words_count_dict, len(processed_urls))
    write_tf_idf_data(processed_urls, words_rel_freq_dict)
    write_inout_links(links_dict)
    write_urls(processed_urls, titles)
    write_page_rank(processed_urls, links_dict)
    return len(processed_urls)


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
writes a url and tf values to the mongoDB collection PAGE_DATA
"url": url, "tf_list": dictionary of tf values
example:
{
    "url": "http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html",
    "tf_list":{
        "kiwi": 0.8,
        "banana": 0.2
        }
}
'''
def write_tf_data(words_dict):
    items = []
    for key, value in zip(words_dict.keys(), words_dict.values()):
        items.append({"url": key, "tf_list": value})
    database[PAGE_DATA].insert_many(items)


'''
calculates idf values and writes them to the mongoDB collection IDF_DATA
"word": word, "idf": value
'''
def write_idf_data(word_count_dict, page_counter):
    word_idf_dict = {word: math.log2(page_counter / (1 + word_count_dict[word]))
                     for word in word_count_dict.keys()}
    items = []
    for key, value in zip(word_count_dict.keys(), word_idf_dict.values()):
        items.append({"word": key, "idf": value})
    database[IDF_DATA].insert_many(items)


'''
reads idf values from the database, get tf values as input (words_rel_freq_dict)
calculates idf-tf values and adds them to the mongoDB collection PAGE_DATA
"url": url, "tf_idf": dictionary of tf-idf values
example for updating the collection:
{
    "url": "http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html",
    "tf_idf_list":{
        "kiwi": 0.038726093486678055,
        "apple": 0.07447019235682993
        }
}
'''
def write_tf_idf_data(urls, words_rel_freq_dict):
    word_idf_dict = list(database.idf_data.find())
    for url in urls:
        temp_dict = {}
        for item in word_idf_dict:
            idf = item["idf"]
            word = item["word"]
            tf_dict = words_rel_freq_dict.get(url, None)
            if tf_dict:
                tf = float(tf_dict.get(word, 0))
                idf_tf = math.log2(1 + tf) * idf
                temp_dict[word] = idf_tf
        database[PAGE_DATA].update_one({"url": url}, {"$set": {"tf_idf_list": temp_dict}})


'''
adds incoming/outgoing links to the mongoDB collection PAGE_DATA 
"url": url, "incoming_list"/"outgoing_list": linked URLs
'''
def write_inout_links(links_dict):
    # finding incoming links
    incoming_links_dict = {}
    for url_1, url_link_list in links_dict.items():
        database.page_data.update_one({"url": url_1}, {"$set": {"outgoing_links": url_link_list}})
        for url_2 in url_link_list:
            if not incoming_links_dict.get(url_2, None):
                incoming_links_dict[url_2] = []
            incoming_links_dict[url_2].append(url_1)

    for url, url_list in incoming_links_dict.items():
        database[PAGE_DATA].update_one({"url": url}, {"$set": {"incoming_links": url_list}})


'''
adds a url's relative link and title to the mongoDB collection PAGE_DATA 
example:
{
    "url": "http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html",
    "relative_link": "N-0.html",
    "title": "N-0"
}
'''
def write_urls(urls, titles):
    for i, url in enumerate(urls):
        last_dash = url.rfind(SLASH)
        link_rel = url[last_dash + 1:]
        database[PAGE_DATA].update_one({"url": url},
                                       {"$set": {"url": url, "relative_link": link_rel, "title": titles[i]}})


'''
calculates page rank of crawled pages, based on Random Surfer Model
adds page rank to the mongoDB collection PAGE_DATA 
"url": url, "page_rank": page rank
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
        array_2 = matrix_mult(array_1, adjacency_matrix)
        error = euclidean_dist(array_1, array_2)
        array_1 = array_2

    for i in range(len(urls)):
        database[PAGE_DATA].update_one({"url": urls[i]}, {"$set": {"page_rank": array_1[0][i]}})
