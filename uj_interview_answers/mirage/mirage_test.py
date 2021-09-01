"""
IN 2019 WE CREATED OUR OWN USER MANAGEMENT SYSTEM CALLED MIRAGE.

MIRAGE IS WRITTEN IN PYTHON USING THE DJANGO FRAMEWORK, BUT YOU ARE NOT EXPECTED
TO BE ABLE TO UNDERSTAND IT FULLY.

WE TALK TO MIRAGE FROM OUR ANGULAR FRONT-END, BUT YOU CAN MAKE QUERIES TO IT
FROM A PYTHON SCRIPT! THIS IS AN OPEN-ENDED, EXPLORATORY SESSION FOR YOU TO
SEE HOW FAR YOU CAN GET INTERACTING WITH MIRAGE.

READ THROUGH THE FILE, BUT IF YOU FEEL LIKE GOING OFF-PISTE, THAT'S FINE. THIS
ISN'T A TEST OF YOUR PYTHON SKILLS (MUCH LESS YOUR DJANGO SKILLS!) BUT AN
EXERCISE TO SEE HOW YOU THINK AND ADAPT.

YOU ARE FREE TO GOOGLE ANYTHING, ASK ANY QUESTIONS OR USE ANY
LIBRARIES YOU FEEL COMFORTABLE WITH (WITHOUT BREAKING MIRAGE!)
"""

################################################################################


"""
THESE FUNCTIONS ARE PROVIDED TO MAKE HTTP REQUESTS
"""

import requests, json
from typing import Dict
from uuid import uuid1

import urllib


def make_get_request(url):
    print('making get request to {}'.format(url))
    response = requests.get(url)
    return json.loads(response.text)


def make_post_request(url, data, content_type="application/json"):
    print('making post request to {} with data {}'.format(url, data))
    response = requests.post(
        url,
    	data=data,
    	headers={
            "content-type": 'application/x-www-form-urlencoded',
        }
    )
    return response.text

    # try:
    #     result = json.loads(response.text)
    # except:
    #     result = response.text
    # return result


################################################################################


"""
THESE ARE THE API ENDPOINTS TO CONTACT MIRAGE
SEE IF YOU CAN FIND THE URLS IN the 'urls.py' file in MIRAGE, AND THE FUNCTIONS
THEY CORRESPOND TO IN THE 'views.py' FILE
"""
URL_GET_TOKEN = "https://mirage.dev.myurbanjungle.com:443/get_token/"
URL_CREATE_USER = 'https://mirage.dev.myurbanjungle.com:443/create_user/'
URL_GET_USER = 'https://mirage.dev.myurbanjungle.com:443/get_user/'
URL_GENERATE_RESET_TOKEN = 'https://mirage.dev.myurbanjungle.com:443/generate_reset_token/'
URL_RESET_PASSWORD = 'https://mirage.dev.myurbanjungle.com:443/reset_password/'

SECRET_CREATE_USER = "It was all a dream, I used to read Word Up! magazine"
SECRET_GENERATE_RESET_TOKEN = "Salt-n-Pepa and Heavy D up in the limousine"

################################################################################


# FIRSTLY, LET'S SEE IF WE CAN LOG IN USING MY EMAIL AND SUPER-SECURE PASSWORD

def login(email: str, password: str) -> None:
    print("logging in")
    encoded_email = urllib.parse.quote(email, safe='')
    encoded_password = urllib.parse.quote(password, safe='')

    data = f"email={encoded_email}&password={encoded_password}"

    token = make_post_request(
        URL_GET_TOKEN,
        data
    )

    return token


def test_login():
    assert login('adam@myurbanjungle.com', 'testing123') is not None
    assert login('adam@myurbanjungle.com', 'testing1234') is None

"""
CAN YOU FOLLOW THROUGH THE FUNCTION CALLED IN MIRAGE WHEN THIS HTTP CALL IS
MADE?

CAN YOU ADAPT THIS FUNCTION TO ALLOW US TO LOG IN AS OTHER USERS?

WHAT IF A USER HAS A PASSWORD LIKE "&testing="?
OR AN EMAIL LIKE "adam+123@myurbanjungle.com"?
"""

################################################################################

# THE FOLLOWING ARE SUGGESTED DIRECTIONS FOR FURTHER EXPLORATION #

################################################################################

"""
WHY DON'T WE SEE IF WE CAN GET THE USER ID FOR 'adam@myurbanjungle.com'?
UNCOMMENT THIS TEST TO CHECK YOU HAVE THE RIGHT ANSWER
"""

def get_user_id(email: str) -> str:
    encoded_email = urllib.parse.quote(email, safe='')
    encoded_secret = urllib.parse.quote(SECRET_CREATE_USER, safe='')

    data = f"email={encoded_email}&secret={encoded_secret}"
    user_data = json.loads(make_post_request(URL_GET_USER, data))

    user_id = user_data['user_id']
    return user_id


def test_get_user_id():

    user_id = get_user_id("adam@myurbanjungle.com")

    assert user_id == 'ujauth|62ce8c6f-605d-49c7-b3de-b70b0467520f'


test_get_user_id()


################################################################################

"""
CREATE A USER FOR YOURSELF AND WRITE A TEST TO CHECK YOUR USER ID
"""

def create_user(email: str, password: str) -> Dict[str, str]:
    encoded_email = urllib.parse.quote(email, safe='')
    encoded_password = urllib.parse.quote(password, safe='')
    encoded_secret = urllib.parse.quote(SECRET_CREATE_USER, safe='')

    data = f"email={encoded_email}&password={encoded_password}&secret={encoded_secret}&roles=user"
    resp = json.loads(make_post_request(URL_CREATE_USER, data))

    return resp


def test_create_user():
    email = f"{uuid1()}@gmail.com"
    password = "&@testing=%"

    user_data = create_user(email, password)
    user_id = user_data['user_id']

    assert user_id == get_user_id(email)

test_create_user()



################################################################################

"""
CHANGE YOUR PASSWORD AND WRITE A TEST TO SHOW THAT IT HAS CHANGED
"""

# def change_password(email: str, old_password: str, new_password: str) -> None:
def change_password(email: str, new_password: str) -> None:
    encoded_email = urllib.parse.quote(email, safe='')
    # encoded_old_password = urllib.parse.quote(old_password, safe='')
    encoded_new_password = urllib.parse.quote(new_password, safe='')
    encoded_secret = urllib.parse.quote(SECRET_GENERATE_RESET_TOKEN, safe='')

    get_token_data = f"email={encoded_email}&secret={encoded_secret}"
    resp = json.loads(make_post_request(
        URL_GENERATE_RESET_TOKEN,
        get_token_data
    ))

    print("YO")

    encoded_reset_token = urllib.parse.quote(resp['tok'], safe='')
    change_pwd_data = "email={}&new_password={}&reset_token={}".format(
        encoded_email,
        encoded_new_password,
        encoded_reset_token
    )
    resp = make_post_request(
        URL_RESET_PASSWORD,
        change_pwd_data
    )
    return resp


def test_change_password():
    email = 'adam@myurbanjungle.com'

    change_password(email, 'new password!')
    change_password(email, 'testing123')

test_change_password()





def test_whole_flow():
    email = f"{uuid1()}@gmail.com"
    password = "%&testing123="

    user_data = create_user(email, password)
    assert 'tok' in login(email, password)
    assert login(email, "wrong password") == ''

    user_id = user_data['user_id']
    assert user_id == get_user_id(email)

    new_password = "tested321%$&^"
    change_pwd_resp = change_password(email, new_password)
    assert change_pwd_resp == "OK"
    assert 'tok' in login(email, new_password)
    assert login(email, password) == ''

test_whole_flow()



################################################################################

"""
HOW SECURE IS THIS LOGIN SYSTEM? WHAT CHANGES WOULD YOU MAKE TO IMPROVE IT?
"""


################################################################################
