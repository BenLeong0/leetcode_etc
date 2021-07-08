import re
from bs4.element import ResultSet
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
    '眼鏡',
    '気',
    '木',
    '尻尾',
    'する'
]


class Wadoku:

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
        search_param = '%20'.join(self.words)
        return f"https://www.wadoku.de/search/{search_param}"


    def get_html_sections(self) -> BeautifulSoup:
        url = self.get_url()
        html = requests.post(url).text
        soup = BeautifulSoup(html, 'html.parser')
        self.sections = self.extract_sections(soup)


    def extract_sections(self, soup: BeautifulSoup) -> "list[BeautifulSoup]":
        table_rows: ResultSet = soup.findAll('tr')
        curr: str = None
        sections: list[BeautifulSoup] = []
        for row in table_rows:
            if not row.has_attr('class'):
                if curr:
                    sections.append(BeautifulSoup(curr, 'html.parser'))
                curr = str(row)
            else:
                curr += str(row)
        return sections



    def extract_kakikata(self, section: BeautifulSoup) -> "list[str]":
        midashi = section.find('th', class_='focalPhrase').text
        return midashi


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





sol = Wadoku(words).get_accents()
print(sol)
