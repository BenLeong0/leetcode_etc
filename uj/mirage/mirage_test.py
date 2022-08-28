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

import requests, json, urllib


def make_get_request(url):
    print("making get request to {}".format(url))
    response = requests.get(url)
    return json.loads(response.text)


def make_post_request(url, data, content_type="application/json"):
    print("making post request to {} with data {}".format(url, data))
    response = requests.post(
        url,
        data=data,
        headers={
            "content-type": "application/x-www-form-urlencoded",
        },
    )
    return json.loads(response.text)


################################################################################


"""
THESE ARE THE API ENDPOINTS TO CONTACT MIRAGE
SEE IF YOU CAN FIND THE URLS IN the 'urls.py' file in MIRAGE, AND THE FUNCTIONS
THEY CORRESPOND TO IN THE 'views.py' FILE
"""
URL_GET_TOKEN = "https://mirage.dev.myurbanjungle.com:443/get_token/"
URL_CREATE_USER = "https://mirage.dev.myurbanjungle.com:443/create_user/"
URL_GET_USER = "https://mirage.dev.myurbanjungle.com:443/get_user/"
URL_GENERATE_RESET_TOKEN = (
    "https://mirage.dev.myurbanjungle.com:443/generate_reset_token/"
)
URL_RESET_PASSWORD = "https://mirage.dev.myurbanjungle.com:443/reset_password/"

SECRET_CREATE_USER = "It was all a dream, I used to read Word Up! magazine"
SECRET_GENERATE_RESET_TOKEN = "Salt-n-Pepa and Heavy D up in the limousine"

################################################################################


# FIRSTLY, LET'S SEE IF WE CAN LOG IN USING MY EMAIL AND SUPER-SECURE PASSWORD


def login(email, password):
    encoded_password = urllib.parse.quote(password)
    encoded_email = urllib.parse.quote(email)
    data = "email={}&password={}".format(encoded_email, encoded_password)

    token = make_post_request(URL_GET_TOKEN, data)

    print(token)


# login("adam+123@myurbanjungle.com", "testing123")

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
# SECRET_CREATE_USER
def get_user_id(email):
    encoded_email = urllib.parse.quote(email)

    data = "email={}&secret={}".format(encoded_email, SECRET_CREATE_USER)

    user = make_post_request(URL_GET_USER, data)

    return user["user_id"]


def test_get_user_id():

    user_id = get_user_id("adam@myurbanjungle.com")

    assert user_id == "ujauth|62ce8c6f-605d-49c7-b3de-b70b0467520f"

    print("yay")


# test_get_user_id()


################################################################################

"""
CREATE A USER FOR YOURSELF AND WRITE A TEST TO CHECK YOUR USER ID
"""

# SECRET_CREATE_USER
def create_user(email, password):
    encoded_email = urllib.parse.quote(email)
    encoded_password = urllib.parse.quote(password)
    roles = ""

    data = "secret={}&email={}&password={}&roles={}".format(
        SECRET_CREATE_USER, encoded_email, encoded_password, roles
    )

    user = make_post_request(URL_CREATE_USER, data)

    return user["user_id"]


# my_id = create_user("test@test.com", "verygoodpassword")


def check_id(email, id):
    assert id == get_user_id(email)
    print("all good")


# check_id("test@test.com", my_id)


################################################################################

"""
CHANGE YOUR PASSWORD AND WRITE A TEST TO SHOW THAT IT HAS CHANGED
"""

# URL_RESET_PASSWORD
# SECRET_GENERATE_RESET_TOKEN
def get_reset_token(email):
    encoded_email = urllib.parse.quote(email)

    data = "email={}&secret={}".format(
        encoded_email, urllib.parse.quote(SECRET_GENERATE_RESET_TOKEN)
    )

    reset_token = make_post_request(URL_GENERATE_RESET_TOKEN, data)["tok"]
    print("token:", reset_token)
    return reset_token


def reset_password(email, new_password):
    encoded_email = urllib.parse.quote(email)
    encoded_new_password = urllib.parse.quote(new_password)
    reset_token = urllib.parse.quote(get_reset_token(email))

    data = "email={}&new_password={}&reset_token={}".format(
        encoded_email, encoded_new_password, reset_token
    )
    print("data:", data)

    response = make_post_request(URL_RESET_PASSWORD, data)
    return response


# reset_password("test@test.com", "brandnewpassword")

# login("test@test.com", "brandnewpassword")


################################################################################

"""
HOW SECURE IS THIS LOGIN SYSTEM? WHAT CHANGES WOULD YOU MAKE TO IMPROVE IT?
"""




################################################################################
