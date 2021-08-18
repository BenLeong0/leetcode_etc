def get_date_suffix(day):
    if (
        day % 10 not in (1, 2, 3) or
        day in (11, 12, 13)
    ):
        return "th"
    elif day % 10 == 1:
        return "st"
    elif day % 10 == 2:
        return "nd"
    elif day % 10 == 3:
        return "rd"
    else:
        raise ValueError("not base 10!!")


def test_get_date_suffix():
    return_value = get_date_suffix(12)
    assert return_value == "th"
    return_value = get_date_suffix(11)
    assert return_value == "th"
    return_value = get_date_suffix(2)
    assert return_value == "nd"
    return_value = get_date_suffix(1)
    assert return_value == "st"
    return_value = get_date_suffix(3)
    assert return_value == "rd"
    return_value = get_date_suffix(17)
    assert return_value == "th"
    return_value = get_date_suffix(18)
    assert return_value == "th"
    return_value = get_date_suffix(22)
    assert return_value == "nd"
    return_value = get_date_suffix(21)
    assert return_value == "st"
    return_value = get_date_suffix(23)
    assert return_value == "rd"
    return_value = get_date_suffix(30)
    assert return_value == "th"
    return_value = get_date_suffix(31)
    assert return_value == "st"

test_get_date_suffix()
