import csv
import hashlib
from typing import Literal


def get_variant(postcode: str) -> Literal['control', 'variant_a']:

    normalised_postcode = postcode.lower().replace(" ", "")

    hashed_postcode = hashlib.md5(normalised_postcode.encode('utf-8'))
    hashed_value = int(hashed_postcode.hexdigest(), 16) % 1000

    if hashed_value < 500:
        return "control"
    else:
        return "variant_a"


def main():
    file = open("feature_flags.csv")
    reader = csv.reader(file)
    next(reader, None)  # skip the headers

    for line in reader:
        postcode, bucket = line[3], line[-1]
        print(postcode, bucket)
        assert get_variant(postcode) == bucket
    print("all passed!")


if __name__ == "__main__":
    main()
