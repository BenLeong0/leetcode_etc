import re
import requests
from bs4 import BeautifulSoup

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
    soup = BeautifulSoup(html, 'html.parser')

    sections = soup.findAll('tr', id=lambda x: x and x.startswith('word_'))
    return sections


def get_writings(section):
    # soup = BeautifulSoup(section, 'html.parser')
    midashi = section.findNext('p', class_='midashi_word').text
    writings = midashi.split('・')
    filtered = [re.search('[^\[]*', writing).group() for writing in writings]
    print(filtered)


def get_accents(section):
    data = section.find('td', class_='katsuyo_jisho_js').find('span', class_='accented_word')
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
