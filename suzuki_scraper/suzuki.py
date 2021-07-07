from bs4 import BeautifulSoup
import re
import requests


class Suzuki:

    accent_dict: "dict[str, list[str]]" = {}
    up_to_ha_regex = '.*?(?=は)'

    url = 'http://www.gavo.t.u-tokyo.ac.jp/ojad/phrasing/index'
    formdata = {
        "data[Phrasing][curve]": "advanced",
        "data[Phrasing][accent]": "advanced",
        "data[Phrasing][accent_mark]": "all",
        "data[Phrasing][estimation]": "crf",
        "data[Phrasing][analyze]": "true",
        "data[Phrasing][phrase_component]": "invisible",
        "data[Phrasing][param]": "invisible",
        "data[Phrasing][subscript]": "visible",
        "data[Phrasing][jeita]": "invisible",
    }

    def __init__(self, words: "list[str]"):
        self.words = words
        words_with_particles = [word + 'は' for word in words]
        self.formdata["data[Phrasing][text]"] = "\n".join(words_with_particles)
        self.get_html_sections()
        self.populate_accent_dict()


    def get_accents(self) -> "list[tuple[str, list[str]]]":
        accent_pairs = [(word, self.accent_dict[word]) for word in self.words]
        return accent_pairs


    def get_html_sections(self) -> None:
        r = requests.post(self.url, self.formdata).text
        soup = BeautifulSoup(r, 'html.parser')
        all_sections = soup.find_all('div', class_='phrasing_row_wrapper')
        self.sections: list[BeautifulSoup] = [sect for sect in all_sections if 'は' in sect.text]


    def populate_accent_dict(self) -> None:
        for section in self.sections:
            writing = self.extract_kakikata(section)
            reading = self.extract_yomikata(section)
            self.accent_dict[writing] = reading


    def extract_kakikata(self, section: BeautifulSoup) -> str:
        kakikata_div: BeautifulSoup = section.find('div', class_='phrasing_subscript')
        word_up_to_ha = re.search(self.up_to_ha_regex, kakikata_div.text).group()
        return word_up_to_ha


    def extract_yomikata(self, section: BeautifulSoup) -> str:
        chars = self.extract_chars(section)
        accent_pattern = self.extract_accent_pattern(section)
        return self.construct_yomikata(chars, accent_pattern)


    def extract_chars(self, section: BeautifulSoup) -> str:
        chars_div: BeautifulSoup = section.find('div', class_='phrasing_text')
        chars_up_to_ha = re.search(self.up_to_ha_regex, chars_div.text).group()
        return chars_up_to_ha


    def extract_accent_pattern(self, section: BeautifulSoup) -> "list[int]":
        get_array_regex = '\[.*?\]'
        function_div = str(section.find('script'))
        accent_pattern = eval(re.search(get_array_regex, function_div).group())
        return accent_pattern


    def construct_yomikata(self, chars: str, accent_pattern: "list[int]") -> str:
        accented_word: str = ''
        H = accent_pattern[0]
        for (i, height) in enumerate(accent_pattern[1:]):
            accented_word += chars[i]
            if H == 0 and height == 1 and i != 0:
                accented_word += "* "
            elif H == 1 and height == 0:
                accented_word += "' "
            H = height
        return accented_word


words = [
    "行きます",
    "読みます",
    "尻尾",
    "時間"
]


print(Suzuki(words).get_accents())


# with open("suzuki_scraper/suzuki.html", "w", encoding="utf8") as f:
#     f.write('<link rel="stylesheet" href="suzuki.css">')
#     f.write('<div class="page-container">')
#     for word in data:
#         f.write(f"<div class=\"word-container\"><div class=\"word\">{word}:</div> <div class=\"reading\">{accented_word}</div></div>")
#     f.write("</div>")
