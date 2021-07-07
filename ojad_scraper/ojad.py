import re
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup


words = [
    '食べ物',
    '行く',
    '罵る',
    '綺麗',
    '面白い',
    '眼鏡',
    '気',
    '木',
    '尻尾'
]


class OJAD:

    accent_dict = {}
    sections: ResultSet

    def __init__(self, words: "list[str]"):
        self.words = words
        self.get_html_sections()

        self.populate_accent_dict()


    def get_accents(self) -> "list[tuple[str, list[str]]]":
        accent_pairs = [(word, self.accent_dict[word]) for word in self.words]
        return accent_pairs


    def populate_accent_dict(self) -> None:
        for section in self.sections:
            writings = self.extract_kakikata(section)
            accents = self.extract_yomikata(section)
            for writing in writings:
                self.accent_dict[writing] = accents


    def get_url(self) -> str:
        query_param = '%20'.join(self.words)
        return f"http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/word:{query_param}"


    def get_html_sections(self) -> BeautifulSoup:
        url = self.get_url()
        html = requests.post(url).text
        soup = BeautifulSoup(html, 'html.parser')

        self.sections = soup.findAll('tr', id=lambda x: x and x.startswith('word_'))


    def extract_kakikata(self, section: BeautifulSoup) -> "list[str]":
        midashi = section.findNext('p', class_='midashi_word').text
        writings = midashi.split('・')
        filtered = [re.search('[^\[]*', writing).group() for writing in writings]
        return filtered


    def extract_yomikata(self, section: BeautifulSoup) -> "list[str]":
        jisho_section: BeautifulSoup = section.find('td', class_='katsuyo_jisho_js')
        accent_patterns: list[BeautifulSoup] = jisho_section.find_all('span', class_='accented_word')

        accents = []
        for accent in accent_patterns:
            contents = accent.contents
            chars = [span.text for span in contents]
            classes = [span['class'] for span in contents]

            curr = ''
            for (char, class_list) in zip(chars, classes):
                curr += char
                if 'accent_top' in class_list:
                    curr += "' "
            accents.append(curr)

        return accents





sol = OJAD(words).get_accents()
print(sol)
