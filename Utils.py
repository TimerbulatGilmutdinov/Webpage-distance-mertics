import re
import requests
from collections import Counter
from bs4 import BeautifulSoup


def remove_stop_words(stop_words, topic_words_list):
    for i in topic_words_list:
        if i in stop_words:
            topic_words_list.remove(i)


def get_page_text(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.get_text()


def text_to_vector(raw_text):
    regex = re.compile(r"\w+")
    words = regex.findall(raw_text)
    return Counter(words)


