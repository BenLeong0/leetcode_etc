from bs4 import BeautifulSoup
import requests


def get_accents(words):
    words_with_particles = [word + 'は' for word in words]

    url = 'http://www.gavo.t.u-tokyo.ac.jp/ojad/phrasing/index'

    formdata = {
        "data[Phrasing][text]": "\n".join(words_with_particles),
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

    r = requests.post(url, formdata).text
    soup = BeautifulSoup(r, 'html.parser')

    mora_sections = soup.findAll('div', class_='phrasing_text')
    morae = [[char[0] for char in str(word).split('<span class="char">')[1:]][:-2] for word in mora_sections]

    resp = [x.split('\n')[0].split(';')[0] for x in r.split('set_accent_curve_phrase')[1:]]
    accent_patterns = [eval(args)[2] for args in resp]

    return list(zip(words, morae, accent_patterns))


def apply_accent_pattern(word, morae, pattern):
    accented_word = ''
    H = pattern[0]
    for (i, height) in enumerate(pattern[1:]):
        if H == 0 and height == 1 and i != 0:
            accented_word += f"{morae[i]}* "
        elif H == 1 and height == 0:
            accented_word += f"{morae[i]}' "
        else:
            accented_word += morae[i]
        H = height
    return f"<div class=\"word-container\"><div class=\"word\">{word}:</div> <div class=\"reading\">{accented_word}</div></div>"


words = [
    "行きます",
    "読みます",
    "尻尾",
    "時間",
]


def print_all_accents(words):
    data = get_accents(words)
    with open("suzuki_scraper/suzuki.html", "w", encoding="utf8") as f:
        f.write('<link rel="stylesheet" href="suzuki.css">')
        f.write('<div class="page-container">')
        for word in data:
            f.write(apply_accent_pattern(*word))
        f.write("</div>")


print_all_accents(words)
