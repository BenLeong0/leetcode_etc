import itertools
import json
import re
import string

area_ratings = {
    "AB1": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB10": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB11": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB12": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB13": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB14": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB15": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB16": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB2": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB21": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB22": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB23": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB24": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB25": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB3": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB30": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB31": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB32": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB33": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB34": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB35": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB36": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB37": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB38": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB39": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB4": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB41": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB42": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB43": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB44": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB45": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB5": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB51": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB52": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB53": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB54": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB55": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB56": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB9": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AB99": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "AL1": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL10": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL2": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL3": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL4": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL5": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL6": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL7": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL8": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "AL9": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "B1": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B10": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B11": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B12": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B13": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B14": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B15": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B16": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B17": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B18": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B19": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B2": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B20": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B21": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B22": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B23": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B24": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B25": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B26": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B27": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B28": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B29": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B3": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B30": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B31": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B32": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B33": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B34": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B35": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B36": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B37": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B38": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B4": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B40": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B42": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B43": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B44": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B45": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B46": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B47": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B48": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B49": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B5": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B50": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B6": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B60": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B61": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B62": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B63": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B64": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B65": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B66": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B67": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B68": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B69": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B7": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B70": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B71": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B72": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B73": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B74": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B75": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B76": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B77": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B78": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B79": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B8": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B80": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B9": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B90": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B91": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B92": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B93": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B94": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B95": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B96": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B97": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B98": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "B99": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "BA1": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA10": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA11": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA12": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA13": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA14": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA15": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA16": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA2": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA20": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA21": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA22": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA3": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA4": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA5": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA6": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA7": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA8": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BA9": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "BB0": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB1": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB10": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB11": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB12": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB18": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB2": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB3": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB4": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB5": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB6": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB7": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB8": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB9": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BB94": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BD1": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD10": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD11": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD12": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD13": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD14": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD15": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD16": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD17": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD18": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD19": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD2": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD20": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD21": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD22": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD23": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD24": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD3": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD4": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD5": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD6": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD7": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD8": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD9": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD97": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD98": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BD99": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "BF1": {
        "area_code": "8",
        "area_name": "British Forces"
    },
    "BH1": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH10": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH11": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH12": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH13": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH14": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH15": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH16": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH17": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH18": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH19": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH2": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH20": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH21": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH22": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH23": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH24": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH25": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH3": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH31": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH4": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH5": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH6": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH7": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH8": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BH9": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "BL0": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL1": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL11": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL2": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL3": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL4": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL5": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL6": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL7": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL78": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL8": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BL9": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "BN1": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN10": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN11": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN12": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN13": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN14": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN15": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN16": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN17": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN18": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN2": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN20": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN21": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN22": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN23": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN24": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN25": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN26": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN27": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN3": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN4": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN41": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN42": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN43": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN44": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN45": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN5": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN50": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN51": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN52": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN6": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN7": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN8": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN88": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN9": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN91": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN95": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BN99": {
        "area_code": "3",
        "area_name": "East Sussex"
    },
    "BR1": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BR2": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BR3": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BR4": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BR5": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BR6": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BR7": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BR8": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BR98": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "BS0": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS1": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS10": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS11": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS12": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS13": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS14": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS15": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS16": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS17": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS18": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS19": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS2": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS20": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS21": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS22": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS23": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS24": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS25": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS26": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS27": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS28": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS29": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS3": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS30": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS31": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS32": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS34": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS35": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS36": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS37": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS38": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS39": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS4": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS40": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS41": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS48": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS49": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS5": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS6": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS7": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS77": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS8": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS80": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS9": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS98": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BS99": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "BT1": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT10": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT11": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT12": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT13": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT14": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT15": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT16": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT17": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT18": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT19": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT2": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT20": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT21": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT22": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT23": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT24": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT25": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT26": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT27": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT28": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT29": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT3": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT30": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT31": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT32": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT33": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT34": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT35": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT36": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT37": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT38": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT39": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT4": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT40": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT41": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT42": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT43": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT44": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT45": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT46": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT47": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT48": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT49": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT5": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT51": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT52": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT53": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT54": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT55": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT56": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT57": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT58": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT6": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT60": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT61": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT62": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT63": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT64": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT65": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT66": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT67": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT68": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT69": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT7": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT70": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT71": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT74": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT75": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT76": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT77": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT78": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT79": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT8": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT80": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT81": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT82": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT9": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT92": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT93": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT94": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "BT99": {
        "area_code": "6",
        "area_name": "N Ireland"
    },
    "CA1": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA10": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA11": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA12": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA13": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA14": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA15": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA16": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA17": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA18": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA19": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA2": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA20": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA21": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA22": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA23": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA24": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA25": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA26": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA27": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA28": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA3": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA4": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA5": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA6": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA7": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA8": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA9": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA95": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CA99": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "CB1": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB10": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB11": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB2": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB21": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB22": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB23": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB24": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB25": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB3": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB4": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB5": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB6": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB7": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB8": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CB9": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "CF1": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF10": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF11": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF14": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF15": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF2": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF21": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF23": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF24": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF3": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF30": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF31": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF32": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF33": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF34": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF35": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF36": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF37": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF38": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF39": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF4": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF40": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF41": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF42": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF43": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF44": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF45": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF46": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF47": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF48": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF5": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF6": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF61": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF62": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF63": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF64": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF7": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF71": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF72": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF8": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF81": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF82": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF83": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF91": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF95": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CF99": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "CH1": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH2": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH25": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH26": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH27": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH28": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH29": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH3": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH30": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH31": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH32": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH33": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH34": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH4": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH41": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH42": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH43": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH44": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH45": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH46": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH47": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH48": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH49": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH5": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH6": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH60": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH61": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH62": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH63": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH64": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH65": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH66": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH7": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH70": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH8": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH88": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CH99": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CM0": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM1": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM11": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM12": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM13": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM14": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM15": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM16": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM17": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM18": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM19": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM2": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM20": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM21": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM22": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM23": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM24": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM3": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM4": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM5": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM6": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM7": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM77": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM8": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM9": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM92": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM98": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CM99": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO1": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO10": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO11": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO12": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO13": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO14": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO15": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO16": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO2": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO3": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO4": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO5": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO6": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO7": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO8": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CO9": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "CR0": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR2": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR3": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR4": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR44": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR5": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR6": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR7": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR8": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR9": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CR90": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "CT1": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT10": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT11": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT12": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT13": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT14": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT15": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT16": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT17": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT18": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT19": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT2": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT20": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT21": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT3": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT4": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT5": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT50": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT6": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT7": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT8": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CT9": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "CV1": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV10": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV11": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV12": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV13": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV2": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV21": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV22": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV23": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV3": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV31": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV32": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV33": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV34": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV35": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV36": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV37": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV4": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV47": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV5": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV6": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV7": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV8": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CV9": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "CW1": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW10": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW11": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW12": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW2": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW3": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW4": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW5": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW6": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW7": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW8": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW9": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "CW98": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "DA1": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA10": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA11": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA12": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA13": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA14": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA15": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA16": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA17": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA18": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA2": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA3": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA4": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA5": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA6": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA7": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA8": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DA9": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "DD1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DD9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "DE1": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE11": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE12": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE13": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE14": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE15": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE2": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE21": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE22": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE23": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE24": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE3": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE4": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE45": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE5": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE55": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE56": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE6": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE65": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE7": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE72": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE73": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE74": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE75": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DE99": {
        "area_code": "6",
        "area_name": "Derbyshire"
    },
    "DG1": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG10": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG11": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG12": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG13": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG14": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG16": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG2": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG3": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG4": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG5": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG6": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG7": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG8": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DG9": {
        "area_code": "6",
        "area_name": "Cumbria"
    },
    "DH1": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH2": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH3": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH4": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH5": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH6": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH7": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH8": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH9": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH97": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH98": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DH99": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL1": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL10": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL11": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL12": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL13": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL14": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL15": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL16": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL17": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL2": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL3": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL4": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL5": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL6": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL7": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL8": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL9": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DL98": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "DN1": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN10": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN11": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN12": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN14": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN15": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN16": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN17": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN18": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN19": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN2": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN20": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN21": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN22": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN3": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN31": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN32": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN33": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN34": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN35": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN36": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN37": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN38": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN39": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN4": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN40": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN41": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN5": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN55": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN6": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN7": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN8": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DN9": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "DT1": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT10": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT11": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT2": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT3": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT4": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT5": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT6": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT7": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT8": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DT9": {
        "area_code": "4",
        "area_name": "Dorset"
    },
    "DY1": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY10": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY11": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY12": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY13": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY14": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY2": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY3": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY4": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY5": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY6": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY7": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY8": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "DY9": {
        "area_code": "5",
        "area_name": "Warwickshire"
    },
    "E1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E10": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E11": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E12": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E13": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E14": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E15": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E16": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E17": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E18": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E1W": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E20": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E5": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E6": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E7": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E77": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E8": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E9": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "E98": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC1A": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC1N": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC1R": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC1V": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC1Y": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC2A": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC2Y": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC3M": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC3N": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC3R": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC4A": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC4V": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC4Y": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC50": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EC88": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "EH1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH13": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH14": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH15": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH16": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH17": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH18": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH19": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH20": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH21": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH22": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH23": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH24": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH25": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH26": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH27": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH28": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH29": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH30": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH31": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH32": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH33": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH34": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH35": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH36": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH37": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH38": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH39": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH40": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH41": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH42": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH43": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH44": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH45": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH46": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH47": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH48": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH49": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH51": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH52": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH53": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH54": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH55": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH77": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH91": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH95": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EH99": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "EN1": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN10": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN11": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN2": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN3": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN4": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN5": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN6": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN7": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN77": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN8": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EN9": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "EX1": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX10": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX11": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX12": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX13": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX14": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX15": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX16": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX17": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX18": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX19": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX2": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX20": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX21": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX22": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX23": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX24": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX3": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX31": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX32": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX33": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX34": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX35": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX36": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX37": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX38": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX39": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX4": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX5": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX6": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX7": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX8": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "EX9": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "FK1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK13": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK14": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK15": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK16": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK17": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK18": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK19": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK20": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK21": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FK9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "FY0": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "FY1": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "FY2": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "FY3": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "FY4": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "FY5": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "FY6": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "FY7": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "FY8": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "G1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G13": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G14": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G15": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G20": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G21": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G22": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G23": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G31": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G32": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G33": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G34": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G40": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G41": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G42": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G43": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G44": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G45": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G46": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G51": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G52": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G53": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G58": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G59": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G60": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G61": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G62": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G63": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G64": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G65": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G66": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G67": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G68": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G69": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G70": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G71": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G72": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G73": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G74": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G75": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G76": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G77": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G78": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G79": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G80": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G81": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G82": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G83": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G84": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "G90": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "GIR": {
        "area_code": "8",
        "area_name": "Merseyside"
    },
    "GL1": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL10": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL11": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL12": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL13": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL14": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL15": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL16": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL17": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL18": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL19": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL2": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL20": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL3": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL4": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL5": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL50": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL51": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL52": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL53": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL54": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL55": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL56": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL6": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL7": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL8": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GL9": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "GU1": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU10": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU11": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU12": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU13": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU14": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU15": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU16": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU17": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU18": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU19": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU2": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU20": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU21": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU22": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU23": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU24": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU25": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU26": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU27": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU28": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU29": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU3": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU30": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU31": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU32": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU33": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU34": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU35": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU4": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU46": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU47": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU5": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU51": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU52": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU6": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU7": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU8": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU9": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GU95": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "GY1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY10": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY5": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY6": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY7": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY8": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "GY9": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "HA0": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA1": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA2": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA3": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA4": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA5": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA6": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA7": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA8": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HA9": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "HD1": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HD2": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HD3": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HD4": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HD5": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HD6": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HD7": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HD8": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HD9": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HG1": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "HG2": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "HG3": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "HG4": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "HG5": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "HP1": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP10": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP11": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP12": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP13": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP14": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP15": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP16": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP17": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP18": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP19": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP2": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP20": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP21": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP22": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP23": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP27": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP3": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP4": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP5": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP6": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP7": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP8": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HP9": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "HR1": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HR2": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HR3": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HR4": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HR5": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HR6": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HR7": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HR8": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HR9": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "HS1": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HS2": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HS3": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HS4": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HS5": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HS6": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HS7": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HS8": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HS9": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "HU1": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU10": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU11": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU12": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU13": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU14": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU15": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU16": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU17": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU18": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU19": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU2": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU20": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU3": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU4": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU5": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU55": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU6": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU7": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU8": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HU9": {
        "area_code": "7",
        "area_name": "E Riding & N Lincs"
    },
    "HX1": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HX2": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HX3": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HX4": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HX5": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HX6": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "HX7": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "IG1": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG10": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG11": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG2": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG3": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG4": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG5": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG6": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG7": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG8": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IG9": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "IM1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IM2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IM3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IM4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IM5": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IM6": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IM7": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IM8": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IM9": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "IP1": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP10": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP11": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP12": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP13": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP14": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP15": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP16": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP17": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP18": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP19": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP2": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP20": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP21": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP22": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP23": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP24": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP25": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP26": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP27": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP28": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP29": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP3": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP30": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP31": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP32": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP33": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP4": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP5": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP6": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP7": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP8": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP9": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IP98": {
        "area_code": "5",
        "area_name": "Suffolk"
    },
    "IV1": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV10": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV11": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV12": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV13": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV14": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV15": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV16": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV17": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV18": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV19": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV2": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV20": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV21": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV22": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV23": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV24": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV25": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV26": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV27": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV28": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV3": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV30": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV31": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV32": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV33": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV34": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV35": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV36": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV4": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV40": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV41": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV42": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV43": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV44": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV45": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV46": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV47": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV48": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV49": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV5": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV51": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV52": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV53": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV54": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV55": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV56": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV6": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV63": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV7": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV8": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV9": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "IV99": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "JE2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "JE3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "KA1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA13": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA14": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA15": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA16": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA17": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA18": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA19": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA20": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA21": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA22": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA23": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA24": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA25": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA26": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA27": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA28": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA29": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA30": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KA9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KT1": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT10": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT11": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT12": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT13": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT14": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT15": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT16": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT17": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT18": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT19": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT2": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT20": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT21": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT22": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT23": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT24": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT3": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT4": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT5": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT6": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT7": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT8": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KT9": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "KW1": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW10": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW11": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW12": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW13": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW14": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW15": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW16": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW17": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW2": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW3": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW5": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW6": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW7": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW8": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KW9": {
        "area_code": "8",
        "area_name": "NE Scotland"
    },
    "KY1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY13": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY14": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY15": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY16": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "KY99": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "L1": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L10": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L11": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L12": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L13": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L14": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L15": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L16": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L17": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L18": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L19": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L2": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L20": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L21": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L22": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L23": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L24": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L25": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L26": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L27": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L28": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L29": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L3": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L30": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L31": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L32": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L33": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L34": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L35": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L36": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L37": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L38": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L39": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L4": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L40": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L41": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L42": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L43": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L44": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L45": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L46": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L47": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L48": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L49": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L5": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L6": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L60": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L61": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L62": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L63": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L64": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L65": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L66": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L67": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L68": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L69": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L7": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L70": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L71": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L72": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L73": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L74": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L75": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L8": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L80": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "L9": {
        "area_code": "6",
        "area_name": "Merseyside"
    },
    "LA1": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA10": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA11": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA12": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA13": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA14": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA15": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA16": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA17": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA18": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA19": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA2": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA20": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA21": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA22": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA23": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA3": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA4": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA5": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA6": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA7": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA8": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LA9": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "LD1": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "LD2": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "LD3": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "LD4": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "LD5": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "LD6": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "LD7": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "LD8": {
        "area_code": "6",
        "area_name": "Herefordshire"
    },
    "LE1": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE10": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE11": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE12": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE13": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE14": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE15": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE16": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE17": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE18": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE19": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE2": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE21": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE3": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE4": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE41": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE5": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE55": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE6": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE65": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE67": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE7": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE8": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE87": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE9": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE94": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE95": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LE99": {
        "area_code": "6",
        "area_name": "Leicestershire"
    },
    "LL11": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL12": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL13": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL14": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL15": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL16": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL17": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL18": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL19": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL20": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL21": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL22": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL23": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL24": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL25": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL26": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL27": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL28": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL29": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL30": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL31": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL32": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL33": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL34": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL35": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL36": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL37": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL38": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL39": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL40": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL41": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL42": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL43": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL44": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL45": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL46": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL47": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL48": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL49": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL51": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL52": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL53": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL54": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL55": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL56": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL57": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL58": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL59": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL60": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL61": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL62": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL63": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL64": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL65": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL66": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL67": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL68": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL69": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL70": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL71": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL72": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL73": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL74": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL75": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL76": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL77": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LL78": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "LN1": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN10": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN11": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN12": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN13": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN2": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN3": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN4": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN5": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN6": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN7": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN8": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LN9": {
        "area_code": "6",
        "area_name": "Lincolnshire"
    },
    "LS1": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS10": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS11": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS12": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS13": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS14": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS15": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS16": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS17": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS18": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS19": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS2": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS20": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS21": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS22": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS23": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS24": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS25": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS26": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS27": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS28": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS29": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS3": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS4": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS5": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS6": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS7": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS8": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS88": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS9": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS98": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LS99": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "LU1": {
        "area_code": "4",
        "area_name": "Bedfordshire"
    },
    "LU2": {
        "area_code": "4",
        "area_name": "Bedfordshire"
    },
    "LU3": {
        "area_code": "4",
        "area_name": "Bedfordshire"
    },
    "LU4": {
        "area_code": "4",
        "area_name": "Bedfordshire"
    },
    "LU5": {
        "area_code": "4",
        "area_name": "Bedfordshire"
    },
    "LU6": {
        "area_code": "4",
        "area_name": "Bedfordshire"
    },
    "LU7": {
        "area_code": "4",
        "area_name": "Bedfordshire"
    },
    "LU95": {
        "area_code": "4",
        "area_name": "Bedfordshire"
    },
    "M1": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M10": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M11": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M12": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M13": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M14": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M15": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M16": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M17": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M18": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M19": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M2": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M20": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M21": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M22": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M23": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M24": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M25": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M26": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M27": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M28": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M29": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M3": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M30": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M31": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M32": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M33": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M34": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M35": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M38": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M4": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M40": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M41": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M43": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M44": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M45": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M46": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M5": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M50": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M52": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M6": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M60": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M61": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M7": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M8": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M9": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M90": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "M99": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "ME1": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME10": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME11": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME12": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME13": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME14": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME15": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME16": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME17": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME18": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME19": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME2": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME20": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME3": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME4": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME5": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME6": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME7": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME8": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME9": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "ME99": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "MK1": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK10": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK11": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK12": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK13": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK14": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK15": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK16": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK17": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK18": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK19": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK2": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK3": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK4": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK40": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK41": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK42": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK43": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK44": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK45": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK46": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK5": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK6": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK7": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK77": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK8": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK9": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "MK98": {
        "area_code": "3",
        "area_name": "Buckinghamshire"
    },
    "ML1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "ML9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "N1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N10": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N11": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N12": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N13": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N14": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N15": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N16": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N17": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N18": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N19": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N1C": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N1P": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N20": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N21": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N22": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N5": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N6": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N7": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N8": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N81": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "N9": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NE1": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE10": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE11": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE12": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE13": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE15": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE16": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE17": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE18": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE19": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE2": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE20": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE21": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE22": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE23": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE24": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE25": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE26": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE27": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE28": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE29": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE3": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE30": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE31": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE32": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE33": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE34": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE35": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE36": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE37": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE38": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE39": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE4": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE40": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE41": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE42": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE43": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE44": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE45": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE46": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE47": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE48": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE49": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE5": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE6": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE61": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE62": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE63": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE64": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE65": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE66": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE67": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE68": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE69": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE7": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE70": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE71": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE8": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE82": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE83": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE85": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE88": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE89": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE9": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE92": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE98": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NE99": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "NG1": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG10": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG11": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG12": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG13": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG14": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG15": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG16": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG17": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG18": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG19": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG2": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG20": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG21": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG22": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG23": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG24": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG25": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG3": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG31": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG32": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG33": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG34": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG4": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG5": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG6": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG7": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG70": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG8": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG80": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG9": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NG90": {
        "area_code": "6",
        "area_name": "Nottinghamshire"
    },
    "NN1": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN10": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN11": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN12": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN13": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN14": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN15": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN16": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN17": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN18": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN2": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN29": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN3": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN4": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN5": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN6": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN7": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN8": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN9": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NN99": {
        "area_code": "5",
        "area_name": "Northamptonshire"
    },
    "NP1": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP10": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP11": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP12": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP13": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP15": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP16": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP18": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP19": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP2": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP20": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP22": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP23": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP24": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP25": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP26": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP3": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP4": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP44": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP5": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP6": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP7": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP8": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NP9": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "NPT": {
        "area_code": "8",
        "area_name": "East Wales"
    },
    "NR1": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR10": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR11": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR12": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR13": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR14": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR15": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR16": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR17": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR18": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR19": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR2": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR20": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR21": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR22": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR23": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR24": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR25": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR26": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR27": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR28": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR29": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR3": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR30": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR31": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR32": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR33": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR34": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR35": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR4": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR5": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR6": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR7": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR8": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR9": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NR99": {
        "area_code": "6",
        "area_name": "Norfolk"
    },
    "NW1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW10": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW11": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW26": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW5": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW6": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW7": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW8": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "NW9": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "OL1": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL10": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL11": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL12": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL13": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL14": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL15": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL16": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL2": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL3": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL4": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL5": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL6": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL7": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL8": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL9": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OL95": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "OX1": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX10": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX11": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX12": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX13": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX14": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX15": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX16": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX17": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX18": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX2": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX20": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX25": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX26": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX27": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX28": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX29": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX3": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX33": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX39": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX4": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX44": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX49": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX5": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX6": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX7": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX8": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "OX9": {
        "area_code": "4",
        "area_name": "Oxfordshire"
    },
    "PA1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA13": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA14": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA15": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA16": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA17": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA18": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA19": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA20": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA21": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA22": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA23": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA24": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA25": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA26": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA27": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA28": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA29": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA30": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA31": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA32": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA33": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA34": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA35": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA36": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA37": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA38": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA39": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA40": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA41": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA42": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA43": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA44": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA45": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA46": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA47": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA48": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA49": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA60": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA61": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA62": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA63": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA64": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA65": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA66": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA67": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA68": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA69": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA70": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA71": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA72": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA73": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA74": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA75": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA76": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA77": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA78": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA80": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA81": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA82": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA83": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA84": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA85": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA86": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA87": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA88": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PA98": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PE1": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE10": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE11": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE12": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE13": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE14": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE15": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE16": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE17": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE18": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE19": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE2": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE20": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE21": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE22": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE23": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE24": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE25": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE26": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE27": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE28": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE29": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE3": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE30": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE31": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE32": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE33": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE34": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE35": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE36": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE37": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE38": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE4": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE5": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE6": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE7": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE8": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE9": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PE99": {
        "area_code": "4",
        "area_name": "Cambridgeshire"
    },
    "PH1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH13": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH14": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH15": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH16": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH17": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH18": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH19": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH20": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH21": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH22": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH23": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH24": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH25": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH26": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH30": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH31": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH32": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH33": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH34": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH35": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH36": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH37": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH38": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH39": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH40": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH41": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH42": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH43": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH44": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH49": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH50": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PH9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "PL1": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL10": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL11": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL12": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL13": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL14": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL15": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL16": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL17": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL18": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL19": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL2": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL20": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL21": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL22": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL23": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL24": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL25": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL26": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL27": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL28": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL29": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL3": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL30": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL31": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL32": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL33": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL34": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL35": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL4": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL5": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL6": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL7": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL8": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL9": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PL95": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "PO1": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO10": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO11": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO12": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO13": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO14": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO15": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO16": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO17": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO18": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO19": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO2": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO20": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO21": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO22": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO24": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO3": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO30": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO31": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO32": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO33": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO34": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO35": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO36": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO37": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO38": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO39": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO4": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO40": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO41": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO5": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO6": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO7": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO8": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PO9": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "PR0": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR1": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR11": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR2": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR25": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR26": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR3": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR4": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR5": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR6": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR7": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR8": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "PR9": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "RG1": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG10": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG11": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG12": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG13": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG14": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG15": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG16": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG17": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG18": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG19": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG2": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG20": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG21": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG22": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG23": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG24": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG25": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG26": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG27": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG28": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG29": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG3": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG30": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG31": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG4": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG40": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG41": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG42": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG45": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG5": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG6": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG7": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG8": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RG9": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "RH1": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH10": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH11": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH12": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH13": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH14": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH15": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH16": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH17": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH18": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH19": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH2": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH20": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH3": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH4": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH5": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH6": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH7": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH77": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH8": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RH9": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "RM1": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM10": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM11": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM12": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM13": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM14": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM15": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM16": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM17": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM18": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM19": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM2": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM20": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM3": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM4": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM5": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM50": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM6": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM7": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM8": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "RM9": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "S1": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S10": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S11": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S12": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S13": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S14": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S17": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S18": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S19": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S2": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S20": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S21": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S25": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S26": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S3": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S30": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S31": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S32": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S33": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S35": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S36": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S4": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S40": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S41": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S42": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S43": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S44": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S45": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S49": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S5": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S6": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S60": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S61": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S62": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S63": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S64": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S65": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S66": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S69": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S7": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S70": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S71": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S72": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S73": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S74": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S75": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S8": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S80": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S81": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S9": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S94": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S95": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S96": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S97": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S98": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "S99": {
        "area_code": "7",
        "area_name": "South Yorkshire"
    },
    "SA1": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA10": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA11": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA12": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA13": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA14": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA15": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA16": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA17": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA18": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA19": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA2": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA20": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA3": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA31": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA32": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA33": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA34": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA35": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA36": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA37": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA38": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA39": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA4": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA40": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA41": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA42": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA43": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA44": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA45": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA46": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA47": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA48": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA5": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA6": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA61": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA62": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA63": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA64": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA65": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA66": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA67": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA68": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA69": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA7": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA70": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA71": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA72": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA73": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA8": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA80": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA9": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SA99": {
        "area_code": "7",
        "area_name": "East Wales"
    },
    "SE1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE10": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE11": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE12": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE13": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE14": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE15": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE16": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE17": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE18": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE19": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE1P": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE20": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE21": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE22": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE23": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE24": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE25": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE26": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE27": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE28": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE5": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE6": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE7": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE8": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE9": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SE99": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SG1": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG10": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG11": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG12": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG13": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG14": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG15": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG16": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG17": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG18": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG19": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG2": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG3": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG4": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG5": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG6": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG7": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG8": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SG9": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "SK1": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK10": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK11": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK12": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK13": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK14": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK15": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK16": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK17": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK2": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK22": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK23": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK3": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK4": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK5": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK6": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK7": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK8": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SK9": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "SL0": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL1": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL2": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL3": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL4": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL5": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL6": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL60": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL7": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL8": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL9": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SL95": {
        "area_code": "3",
        "area_name": "Berkshire"
    },
    "SM1": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "SM2": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "SM3": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "SM4": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "SM5": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "SM6": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "SM7": {
        "area_code": "2",
        "area_name": "Surrey"
    },
    "SN1": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN10": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN11": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN12": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN13": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN14": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN15": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN16": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN17": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN2": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN25": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN26": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN3": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN38": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN4": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN42": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN5": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN6": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN7": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN8": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN86": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN9": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SN99": {
        "area_code": "5",
        "area_name": "Wiltshire"
    },
    "SO1": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO14": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO15": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO16": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO17": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO18": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO19": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO2": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO20": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO21": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO22": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO23": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO24": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO25": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO3": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO30": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO31": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO32": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO4": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO40": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO41": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO42": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO43": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO45": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO5": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO50": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO51": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO52": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO53": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO9": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SO97": {
        "area_code": "4",
        "area_name": "Hampshire"
    },
    "SP1": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP10": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP11": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP2": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP3": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP4": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP5": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP6": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP7": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP8": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SP9": {
        "area_code": "6",
        "area_name": "Worcestershire"
    },
    "SR1": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR2": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR3": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR4": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR43": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR5": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR6": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR7": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR8": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR88": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SR9": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "SS0": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS1": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS11": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS12": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS13": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS14": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS15": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS16": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS17": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS2": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS22": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS3": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS4": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS5": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS6": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS7": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS8": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS9": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "SS99": {
        "area_code": "3",
        "area_name": "Essex"
    },
    "ST1": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST10": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST11": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST12": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST13": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST14": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST15": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST16": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST17": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST18": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST19": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST2": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST20": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST21": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST3": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST4": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST5": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST55": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST6": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST7": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST8": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "ST9": {
        "area_code": "6",
        "area_name": "Staffordshire"
    },
    "SW1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW10": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW11": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW12": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW13": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW14": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW15": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW16": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW17": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW18": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW19": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW1A": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW1H": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW1P": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW1V": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW1W": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW1X": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW1Y": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW20": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW5": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW6": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW7": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW8": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW9": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW95": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SW99": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "SY1": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY10": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY11": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY12": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY13": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY14": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY15": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY16": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY17": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY18": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY19": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY2": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY20": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY21": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY22": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY23": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY24": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY25": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY3": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY4": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY5": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY6": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY7": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY8": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY9": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "SY99": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TA1": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA10": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA11": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA12": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA13": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA14": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA15": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA16": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA17": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA18": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA19": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA2": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA20": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA21": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA22": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA23": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA24": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA3": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA4": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA5": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA6": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA7": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA8": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TA9": {
        "area_code": "6",
        "area_name": "Somerset"
    },
    "TD1": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD10": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD11": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD12": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD13": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD14": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD15": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD2": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD3": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD4": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD5": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD6": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD7": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD8": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TD9": {
        "area_code": "6",
        "area_name": "E Scotland"
    },
    "TF1": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF10": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF11": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF12": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF13": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF2": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF3": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF4": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF5": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF6": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF7": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF8": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TF9": {
        "area_code": "6",
        "area_name": "Shropshire"
    },
    "TN1": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN10": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN11": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN12": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN13": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN14": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN15": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN16": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN17": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN18": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN19": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN2": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN20": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN21": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN22": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN23": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN24": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN25": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN26": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN27": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN28": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN29": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN3": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN30": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN31": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN32": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN33": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN34": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN35": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN36": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN37": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN38": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN39": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN4": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN40": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN5": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN6": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN7": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN8": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TN9": {
        "area_code": "3",
        "area_name": "Kent"
    },
    "TQ1": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ10": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ11": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ12": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ13": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ14": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ2": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ3": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ4": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ5": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ6": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ7": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ8": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TQ9": {
        "area_code": "5",
        "area_name": "Devon"
    },
    "TR1": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR10": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR11": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR12": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR13": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR14": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR15": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR16": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR17": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR18": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR19": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR2": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR20": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR21": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR22": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR23": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR24": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR25": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR26": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR27": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR3": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR4": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR5": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR6": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR7": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR8": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR9": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TR93": {
        "area_code": "6",
        "area_name": "Cornwall"
    },
    "TS1": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS10": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS11": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS12": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS13": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS14": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS15": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS16": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS17": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS18": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS19": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS2": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS20": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS21": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS22": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS23": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS24": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS25": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS26": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS27": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS28": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS29": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS3": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS4": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS5": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS6": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS7": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS8": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS9": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TS90": {
        "area_code": "7",
        "area_name": "Durham"
    },
    "TW1": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW10": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW11": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW12": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW13": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW14": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW15": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW16": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW17": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW18": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW19": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW2": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW20": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW3": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW4": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW5": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW6": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW7": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW8": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "TW9": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB1": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB10": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB11": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB18": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB2": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB3": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB4": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB5": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB6": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB7": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB8": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "UB9": {
        "area_code": "2",
        "area_name": "Outer London"
    },
    "W1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W10": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W11": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W12": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W13": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W14": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1B": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1D": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1F": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1G": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1H": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1K": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1T": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1U": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W1W": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W3": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W4": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W5": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W6": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W7": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W8": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "W9": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WA1": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA10": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA11": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA12": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA13": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA14": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA15": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA16": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA2": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA3": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA4": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA5": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA55": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA6": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA7": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA8": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA88": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WA9": {
        "area_code": "6",
        "area_name": "Cheshire"
    },
    "WC1": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC1A": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC1B": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC1E": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC1H": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC1N": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC1X": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC2": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC2B": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC2E": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC2H": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC2N": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC2R": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WC99": {
        "area_code": "1",
        "area_name": "Inner London"
    },
    "WD1": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD17": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD18": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD19": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD2": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD23": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD24": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD25": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD3": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD4": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD5": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD6": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD7": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WD99": {
        "area_code": "3",
        "area_name": "Hertfordshire"
    },
    "WF1": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF10": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF11": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF12": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF13": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF14": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF15": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF16": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF17": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF2": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF3": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF4": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF5": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF6": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF7": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF8": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF9": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WF90": {
        "area_code": "7",
        "area_name": "West Yorkshire"
    },
    "WN1": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "WN2": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "WN3": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "WN4": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "WN5": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "WN6": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "WN7": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "WN8": {
        "area_code": "6",
        "area_name": "Lancashire"
    },
    "WR1": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR10": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR11": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR12": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR13": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR14": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR15": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR2": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR3": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR4": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR5": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR6": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR7": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR78": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR8": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR9": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WR99": {
        "area_code": "5",
        "area_name": "Gloucestershire"
    },
    "WS1": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS10": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS11": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS12": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS13": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS14": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS15": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS2": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS3": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS4": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS5": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS6": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS7": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS8": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WS9": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV1": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV10": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV11": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV12": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV13": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV14": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV15": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV16": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV2": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV3": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV4": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV5": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV6": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV7": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV8": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV9": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV98": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "WV99": {
        "area_code": "6",
        "area_name": "West Midlands"
    },
    "YO1": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO10": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO11": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO12": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO13": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO14": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO15": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO16": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO17": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO18": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO19": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO21": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO22": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO23": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO24": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO25": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO26": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO30": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO31": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO32": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO41": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO42": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO43": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO51": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO60": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO61": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO62": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO7": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "YO8": {
        "area_code": "6",
        "area_name": "North Yorkshire"
    },
    "ZE1": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "ZE2": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
    "ZE3": {
        "area_code": "5",
        "area_name": "High & Islands"
    },
}

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

rating_area_map = {}
for code in map(str, range(1, 9)):
    prefixes = [prefix for prefix in area_ratings if area_ratings[prefix]['area_code'] == code]
    current = []
    for prefix in prefixes:
        if re.match(r"^\D+\d$", prefix) is None:
            continue
        chars_indices = [i for i, char in enumerate(prefix) if char in string.ascii_uppercase]
        for combination in powerset(chars_indices):
            current.append(''.join([char.lower() if i in combination else char for i, char in enumerate(prefix)]))
    rating_area_map[code] = current

print(rating_area_map)
with open("testareas", "w") as f:
    f.write(json.dumps(rating_area_map, indent=4))
