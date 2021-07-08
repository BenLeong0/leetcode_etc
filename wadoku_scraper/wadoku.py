import re
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup

# Multithreading:
# https://stackoverflow.com/questions/11968689/python-multithreading-wait-till-all-threads-finished

words = [
    '眼鏡',
    '食べ物',
    '行く',
    '罵る',
    '綺麗',
    '面白い',
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
            writing = self.extract_kakikata(section)
            accents = self.extract_yomikata(section)
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
                sections.append(str(row))
            else:
                sections[-1] += str(row)

        return [BeautifulSoup(section, 'html.parser') for section in sections]



    def extract_kakikata(self, section: BeautifulSoup) -> str:
        midashi: str = section.find('th', class_='focalPhrase').text
        return midashi.strip()


    def extract_yomikata(self, section: BeautifulSoup) -> "list[str]":
        accent_sections: list[BeautifulSoup] = section.find_all('span', class_='accent')

        accents: list[str] = []
        for accent in accent_sections:
            spans: list[BeautifulSoup] = list(accent.children)

            # Initialise with first char
            curr = self.remove_punct(spans[0].text)
            if 't' in spans[0]['class']:
                if 'r' in spans[0]:
                    curr += "' "
                    H = 0
                H = 1
            else: H = 0

            # Iterate over alternating heights
            for (i, span) in enumerate(spans[1:], start=1):
                if 't' in span['class'] and H == 0:
                    if i != 1: curr += "* "
                    H = 1
                elif 'b' in span['class'] and H == 1:
                    curr += "' "
                    H = 0

                curr += self.remove_punct(span.text)

            # Final drop if 尾高
            if 'r' in spans[-1]['class'] and H == 1:
                curr += "'"

            accents.append(curr)

        return accents


    def remove_punct(self, s: str) -> str:
        return re.sub('[\￨･~]', '', s)





sol = Wadoku(words).get_accents()
print(sol)
