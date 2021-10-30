import pytest

@pytest.fixture
def fruit1():
    return "apple"

@pytest.fixture
def fruit2():
    return "banana"

@pytest.fixture()
def fruitbowl(fruit1):
    return [fruit1]

@pytest.fixture(autouse=True)
def add_banana(fruitbowl, fruit2):
    fruitbowl.append(fruit2)



def test_fruit1_apple(fruit1):
    assert fruit1 == "apple"


def test_fruit2_not_apple(fruit2):
    assert fruit2 != "apple"


def test_fruit2_banana(fruit2):
    assert fruit2 == "banana"


def test_fruit1_not_banana(fruit1):
    assert fruit1 != "banana"



def test_full_fruit_bowl(fruitbowl):
    assert "apple" in fruitbowl
    assert "banana" in fruitbowl


def test_full_fruit_bowl(fruitbowl, fruit1, fruit2):
    assert fruit1 in fruitbowl
    assert fruit2 in fruitbowl

a = {
    "id": "hi",
    "ape": True,
}

b = {
    "id": "yo",
    "ape": False,
}


@pytest.fixture(params=[a,b], ids=lambda d:d['id'])
def d(request):
    return request.param

# @pytest.mark.parametrize("d", [a,b], )
def test_param_dict_id(d):
    assert True
