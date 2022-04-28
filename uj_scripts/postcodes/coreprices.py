import json

CORE_PRICES = [
    ("1",   "Decimal('8.54')",   "Decimal('9.83')",   "Decimal('12.81')",  "Decimal('17.41')",  "Decimal('22.74')"),
    ("2",   "Decimal('9.60')",   "Decimal('11.09')",  "Decimal('14.26')",  "Decimal('21.65')",  "Decimal('28.97')"),
    ("3",   "Decimal('9.80')",   "Decimal('11.97')",  "Decimal('14.70')",  "Decimal('20.16')",  "Decimal('26.74')"),
    ("4",   "Decimal('10.02')",  "Decimal('11.57')",  "Decimal('16.96')",  "Decimal('25.00')",  "Decimal('33.66')"),
    ("5",   "Decimal('10.10')",  "Decimal('12.34')",  "Decimal('15.15')",  "Decimal('20.79')",  "Decimal('27.57')"),
    ("6",   "Decimal('10.38')",  "Decimal('12.23')",  "Decimal('14.98')",  "Decimal('23.28')",  "Decimal('31.02')"),
    ("7",   "Decimal('10.66')",  "Decimal('12.34')",  "Decimal('15.71')",  "Decimal('21.82')",  "Decimal('29.87')"),
    ("8",   "Decimal('10.89')",  "Decimal('12.96')",  "Decimal('16.20')",  "Decimal('21.31')",  "Decimal('28.71')"),
    ("9",   "Decimal('11.22')",  "Decimal('13.46')",  "Decimal('15.71')",  "Decimal('22.87')",  "Decimal('31.01')"),
    ("10",  "Decimal('11.42')",  "Decimal('13.18')",  "Decimal('19.33')",  "Decimal('27.14')",  "Decimal('37.03')"),
    ("11",  "Decimal('11.48')",  "Decimal('13.67')",  "Decimal('16.92')",  "Decimal('23.90')",  "Decimal('33.88')"),
    ("12",  "Decimal('11.72')",  "Decimal('13.86')",  "Decimal('18.12')",  "Decimal('23.70')",  "Decimal('34.92')"),
    ("13",  "Decimal('12.26')",  "Decimal('14.40')",  "Decimal('18.66')",  "Decimal('24.68')",  "Decimal('36.00')"),
    ("14",  "Decimal('12.43')",  "Decimal('14.69')",  "Decimal('19.21')",  "Decimal('25.12')",  "Decimal('37.01')"),
    ("15",  "Decimal('13.46')",  "Decimal('15.71')",  "Decimal('20.20')",  "Decimal('27.02')",  "Decimal('39.05')"),
    ("16",  "Decimal('13.50')",  "Decimal('15.57')",  "Decimal('22.84')",  "Decimal('30.29')",  "Decimal('43.76')"),
    ("17",  "Decimal('13.59')",  "Decimal('15.76')",  "Decimal('21.70')",  "Decimal('29.17')",  "Decimal('42.64')"),
    ("18",  "Decimal('21.48')",  "Decimal('24.40')",  "Decimal('29.28')",  "Decimal('41.97')",  "Decimal('63.45')"),
]

core_cover = {}

for level in CORE_PRICES:
    core_cover[level[0]] = {
        '1': level[1],
        '2': level[2],
        '3': level[3],
        '4': level[4],
        '5': level[5],
    }

print(core_cover)
with open("new_core", "w") as f:
    f.write(json.dumps(core_cover, indent=4))
