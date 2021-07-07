import re
import requests
from bs4 import BeautifulSoup

# Multithreading:
# https://stackoverflow.com/questions/11968689/python-multithreading-wait-till-all-threads-finished

words = [
    '食べ物',
    '行く',
    '罵る',
    '綺麗',
    '面白い',
    '眼鏡'
]

midashi_word = '<p class="midashi_word">.*?</p>'


def get_html_sections(words):
    query_param = '%20'.join(words)
    url = f"http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/word:{query_param}"
    html = requests.post(url).text

    get_section_regex = '<tr id="word.*?<\/tr>'
    return re.findall(get_section_regex, html, re.S)


def get_writings(section):
    get_midashi_regex = '<p class="midashi_word">.*?</p>'
    midashi = re.search(get_midashi_regex, section)[0]
    writings = re.search('>.*?<', midashi)[0][1:-1].split('・')
    filtered = [re.match('[^\[]*', writing)[0] for writing in writings]
    print(filtered)


def get_accents(section):
    soup = BeautifulSoup(section, 'html.parser')
    data = soup.find('td', class_='katsuyo_jisho_js').find('span', class_='accented_word')
    if data:
        contents = data.contents
        classes = [span['class'] for span in contents]
        chars = [span.text for span in contents]
        print(chars)
        print(classes)
    else:
        print('no results!')



def get_ojad_data(words):
    accent_dict = {}
    sections = get_html_sections(words)

    for section in sections:
        writings = get_writings(section)
        get_accents(section)
        print('===')


get_ojad_data(words)
