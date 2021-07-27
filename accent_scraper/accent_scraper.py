import collections
from threading import Thread

from ojad_scraper.ojad import OJAD
from suzuki_scraper.suzuki import Suzuki
from wadoku_scraper.wadoku import Wadoku





def get_full_accent_dict(words):
    accent_dict = collections.defaultdict(dict)

    def call_script(src):
        if src == "ojad":
            for (word, accents) in OJAD(words).get_accents():
                accent_dict[src][word] = accents
        elif src == "suzuki":
            for (word, accents) in Suzuki(words).get_accents():
                accent_dict[src][word] = accents
        elif src == "wadoku":
            for (word, accents) in Wadoku(words).get_accents():
                accent_dict[src][word] = accents

    t1 = Thread(target=call_script, args=['ojad'])
    t2 = Thread(target=call_script, args=['suzuki'])
    t3 = Thread(target=call_script, args=['wadoku'])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print(accent_dict)


if __name__ == '__main__':
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
    get_full_accent_dict(words)
