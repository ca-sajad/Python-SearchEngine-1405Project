import math
import searchdata
from constants import *


def search(phrase, boost):
    urls, titles = read_urls_titles()
    if boost:
        page_ranks = read_page_ranks()
    else:
        page_ranks = [1 for _ in range(len(urls))]
    top_10 = calculate_top_similarities(urls, titles, phrase, page_ranks)
    return top_10


'''
reads and returns lists of URLs and their titles from a json file
'''
def read_urls_titles():
    json_data = searchdata.read_file(URLS_FILE_NAME)
    urls = [_dict[URL] for _dict in json_data]
    titles = [_dict[TITLE] for _dict in json_data]
    return urls, titles


'''
reads and returns a list of page rank values from a json file
'''
def read_page_ranks():
    urls_ranks_dic = searchdata.read_file(PAGE_RANK_FILE_NAME)
    page_ranks = list(urls_ranks_dic.values())
    return page_ranks


'''
reads a search phrase, finds unique words
creates and returns vectors of tf-idf values for each input URL
also return number of unique words in the search phrase
'''
def create_vectors(urls, phrase):
    url_count = len(urls)

    phrase = phrase.split(SPACE)
    phrase_size = len(phrase)
    phrase_list = list(set(phrase))         # list of unique words in the phrase
    phrase_list_size = len(phrase_list)     # number of unique words in the phrase

    vectors = [[0] * phrase_list_size for _ in range(url_count)]
    for i, url in enumerate(urls):
        for j in range(phrase_list_size):
            word = phrase_list[j]
            tf_idf = searchdata.get_tf_idf(url, word)
            vectors[i][j] = tf_idf

    query_vector = [[0] for _ in range(phrase_list_size)]
    for i, word in enumerate(phrase_list):
        idf = searchdata.get_idf(word)
        tf = phrase.count(word) / phrase_size
        query_vector[i] = math.log2(1 + tf) * idf

    return vectors, query_vector, phrase_list_size


'''
calculates cosine similarity of webpages and a search query Vector Space Model
returns top 10 similar webpages (or other number, based on the constant in the constants module) as a list
each item in the list is a dictionary 
example:
{
    'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 
    title': 'N-0', 
    'score': 0.2369063892398991
}
'''
def calculate_top_similarities(urls, titles, phrase, page_ranks):
    vectors, query_vector, phrase_list_size = create_vectors(urls, phrase)
    url_count = len(urls)

    similarity = [0 for _ in range(url_count)]
    for i in range(url_count):
        numerator = sum([query_vector[j] * vectors[i][j] for j in range(phrase_list_size)])
        left_denom = math.sqrt(sum([query_vector[j] * query_vector[j] for j in range(phrase_list_size)]))
        right_denom = math.sqrt(sum([vectors[i][j] * vectors[i][j] for j in range(phrase_list_size)]))
        if left_denom == 0 or right_denom == 0:
            similarity[i] = 0
        else:
            similarity[i] = numerator / (left_denom * right_denom) * page_ranks[i]

    top_10 = []
    for i in range(TOP_SIMILARITIES):
        max_sim = max(similarity)
        index_max_sim = similarity.index(max_sim)
        top_10.append({URL: urls[index_max_sim], TITLE: titles[index_max_sim], SCORE: max_sim})
        similarity[index_max_sim] = -1

    return top_10

