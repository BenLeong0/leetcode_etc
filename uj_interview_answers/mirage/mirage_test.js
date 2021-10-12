/*
IN 2019 WE CREATED OUR OWN USER MANAGEMENT SYSTEM CALLED MIRAGE.

MIRAGE IS WRITTEN IN PYTHON USING THE DJANGO FRAMEWORK, BUT YOU ARE NOT EXPECTED
TO BE ABLE TO UNDERSTAND IT FULLY.

YOU SHOULD HAVE THREE FILES:
    - mirage_test.txt   :: THIS SCRIPT, FOR YOU TO SEND REQUESTS TO DEV MIRAGE
    - urls.py           :: SOURCE CODE OF MIRAGE API ENDPOINTS
    - view.py           :: SOURCE CODE OF MIRAGE FUNCTIONS

WE TALK TO MIRAGE FROM OUR ANGULAR FRONT-END, BUT YOU CAN MAKE QUERIES TO IT
FROM THE CHROME CONSOLE! THIS IS AN OPEN-ENDED, EXPLORATORY SESSION FOR YOU TO
SEE HOW FAR YOU CAN GET INTERACTING WITH MIRAGE.

READ THROUGH THIS FILE, BUT IF YOU FEEL LIKE GOING OFF-PISTE, THAT'S FINE. THIS
ISN'T A TEST OF YOUR JAVASCRIPT SKILLS (MUCH LESS YOUR PYTHON SKILLS!) BUT AN
EXERCISE TO SEE HOW YOU THINK AND ADAPT.

YOU ARE FREE TO GOOGLE ANYTHING, ASK ANY QUESTIONS OR USE ANY
LIBRARIES YOU FEEL COMFORTABLE WITH (WITHOUT BREAKING MY COMPUTER)
*/

////////////////////////////////////////////////////////////////////////////////


/*
THESE FUNCTIONS ARE PROVIDED TO MAKE HTTP REQUESTS

TO USE, RUN COMMAND
npm install node-fetch@2.6.5

FETCH API DOCS
https://developers.google.com/web/ilt/pwa/working-with-the-fetch-api
*/

const fetch = require('node-fetch');

async function makeGetRequest(url) {
    return fetch(url)
        .then(res => res.json());
}

async function makePostRequest(url, data, callback_fn) {
    return fetch(
        url,
        {
            method: 'POST',
            body: data,
            headers: {
                'Content-type': 'application/x-www-form-urlencoded',
            }
        }
    )
    .then(res => res.json());
}

////////////////////////////////////////////////////////////////////////////////


/*
THESE ARE THE API ENDPOINTS TO CONTACT MIRAGE
SEE IF YOU CAN FIND THE URLS IN the 'urls.py' file in MIRAGE, AND THE FUNCTIONS
THEY CORRESPOND TO IN THE 'views.py' FILE
*/
URL_GET_TOKEN = "https://mirage.dev.myurbanjungle.com:443/get_token/";
URL_CREATE_USER = 'https://mirage.dev.myurbanjungle.com:443/create_user/';
URL_GET_USER = 'https://mirage.dev.myurbanjungle.com:443/get_user/';
URL_GENERATE_RESET_TOKEN = 'https://mirage.dev.myurbanjungle.com:443/generate_reset_token/';
URL_RESET_PASSWORD = 'https://mirage.dev.myurbanjungle.com:443/reset_password/';

SECRET_CREATE_USER = "It was all a dream, I used to read Word Up! magazine"
SECRET_GENERATE_RESET_TOKEN = "Salt-n-Pepa and Heavy D up in the limousine"

//console.clear()

////////////////////////////////////////////////////////////////////////////////


// FIRSTLY, LET'S SEE IF WE CAN LOG IN USING MY EMAIL AND SUPER-SECURE PASSWORD

async function login(email, password) {
    const encoded_email = encodeURI(email)
    const encoded_password = encodeURI(password)

    const data = `email=${encoded_email}&password=${encoded_password}`;

    let token = await makePostRequest(
        URL_GET_TOKEN,
        data
    );

    console.log(token);

}

login("adam@myurbanjungle.com", "testing123")

// CAN YOU FOLLOW THROUGH THE FUNCTION CALLED IN MIRAGE WHEN THIS HTTP CALL IS
// MADE?

// CAN YOU ADAPT THIS FUNCTION TO ALLOW US TO LOG IN AS OTHER USERS?

// WHAT IF A USER HAS A PASSWORD LIKE "&testing="? (weirdpassword@myurbanjungle.com)
// OR AN EMAIL LIKE "adam+123@myurbanjungle.com"? (password: testing123)

// REMEMBER - YOU CAN GOOGLE ANYTHING YOU NEED!


////////////////////////////////////////////////////////////////////////////////

// THE FOLLOWING ARE SUGGESTED DIRECTIONS FOR FURTHER EXPLORATION //

////////////////////////////////////////////////////////////////////////////////


// WHY DON'T WE SEE IF WE CAN GET THE USER ID FOR 'adam@myurbanjungle.com'?
// UNCOMMENT THIS TEST TO CHECK YOU HAVE THE RIGHT ANSWER

async function getUserID(email) {
    const encoded_email = encodeURI(email)
    const encoded_secret = encodeURI(SECRET_CREATE_USER)

    const data = `email=${encoded_email}&secret=${encoded_secret}`

    let user = await makePostRequest(
        URL_GET_USER,
        data
    );
    console.log(user)

    const userID = user.user_id

    console.assert(
        userID === 'ujauth|62ce8c6f-605d-49c7-b3de-b70b0467520f',
        "TEST getUserID fails"
    )

}

getUserID("adam@myurbanjungle.com")


////////////////////////////////////////////////////////////////////////////////

// CREATE A USER FOR YOURSELF AND WRITE A TEST TO CHECK YOUR USER ID


////////////////////////////////////////////////////////////////////////////////

// CHANGE YOUR PASSWORD AND WRITE A TEST TO SHOW THAT IT HAS CHANGED


////////////////////////////////////////////////////////////////////////////////

// HOW SECURE IS THIS LOGIN SYSTEM? WHAT CHANGES WOULD YOU MAKE TO IMPROVE IT?


////////////////////////////////////////////////////////////////////////////////
