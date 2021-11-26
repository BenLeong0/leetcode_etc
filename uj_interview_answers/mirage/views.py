import datetime
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_http_methods
import json
from jose import jwt

JWT_SECRET = settings.JWT_SECRET
USER_CREATION_SECRET = settings.USER_CREATION_SECRET
TOKEN_GENERATION_SECRET = settings.TOKEN_GENERATION_SECRET
USER = get_user_model()

def index(request):
    return HttpResponse("Why don't we just wait here for a little while, see what happens?")

@sensitive_post_parameters("password",)
@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def auth_and_get_token(request):
    if request.method == "OPTIONS":
        return HttpResponse(status=204)
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    if not (email and pwd):
        return HttpResponse(status=401)

    # If user doesn't exist, 401 straight away
    normalised_email = email.lower()
    try:
        x = USER.objects.get(email=normalised_email)
    except USER.DoesNotExist:
        return HttpResponse(status=401)

    user = authenticate(username=normalised_email, password=pwd)
    if user is not None:
        token = make_user_token(user)
        response = '{"tok": "' + token + '"}'
        logins = json.loads(user.last_logins)
        logins.pop()
        logins.insert(0,str(timezone.now()))
        user.last_logins = json.dumps(logins)
        user.failed_logins = 0
        user.save()
        return HttpResponse(response)
    else:
        x.failed_logins += 1
        if x.failed_logins >= 10:
            x.is_active = 0
        x.save()
        return HttpResponse(status=401)


@sensitive_post_parameters("password", "secret",)
@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def create_user(request):
    if request.method == "OPTIONS":
        return HttpResponse(status=204)

    secret = request.POST.get("secret")
    user_email = request.POST.get("email")
    user_pwd = request.POST.get("password")
    user_roles = request.POST.get("roles")
    if not (secret and user_email):
        return HttpResponse(status=401)
    if not (secret == USER_CREATION_SECRET):
        return HttpResponse(status=401)
    try:
        user = USER.objects.create_user(email=user_email, password=user_pwd, roles=user_roles)
        response = '{"user_id":"'+ user.user_id+'","email":"'+user.email+'"}'
        return HttpResponse(response)
    except IntegrityError:
        response = 'USER_ALREADY_EXISTS'
        return HttpResponse(response, status=403)


@sensitive_post_parameters("secret",)
@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def get_user(request):
    if request.method == "OPTIONS":
        return HttpResponse(status=204)

    secret = request.POST.get("secret")
    user_email = request.POST.get("email")
    if not (secret and user_email):
        return HttpResponse(status=401)
    if not (secret == USER_CREATION_SECRET):
        return HttpResponse(status=401)

    normalised_email = user_email.lower()
    try:
        x = USER.objects.get(email=normalised_email)
        response = '{"user_id":"'+ x.user_id+'","email":"'+x.email+'"}'
        return HttpResponse(response)
    except USER.DoesNotExist:
        response = 'USER_DOES_NOT_EXIST'
        return HttpResponse(response, status=401)


@sensitive_post_parameters("secret",)
@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def generate_reset_token(request):
    if request.method == "OPTIONS":
        return HttpResponse(status=204)

    user_email = request.POST.get("email")
    secret = request.POST.get("secret")
    if not (secret and user_email):
        return HttpResponse(status=401)
    if not (secret == TOKEN_GENERATION_SECRET):
        return HttpResponse(status=401)
    normalised_email = user_email.lower()
    try:
        user = USER.objects.get(email=normalised_email)
        token = make_pwd_reset_token(user)
        response = '{"tok": "' + token + '"}'
        return HttpResponse(response)
    except USER.DoesNotExist:
        return HttpResponse(status=401)


@sensitive_post_parameters("new_password",)
@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def reset_password(request):
    if request.method == "OPTIONS":
        return HttpResponse(status=204)

    user_email = request.POST.get("email")
    new_pwd = request.POST.get("new_password")
    reset_token = request.POST.get("reset_token")
    if not (user_email and new_pwd and reset_token):
        return HttpResponse(status=401)
    try:
        token_dict = jwt.decode(reset_token, JWT_SECRET, algorithms='HS512')
    except:
        return HttpResponse(status=401)
    normalised_email = user_email.lower()
    if not (normalised_email == token_dict["pwd_reset"].lower()):
        return HttpResponse(status=401)
    try:
        user = USER.objects.get(email=normalised_email)
        user.set_password(new_pwd)
        user.failed_logins = 0
        user.is_active = True
        user.save()
        return HttpResponse("OK")
    except USER.DoesNotExist:
        return HttpResponse(status=401)


def make_user_token(user):
    exp_ts = make_expiry_timestamp()
    data = {'user_id': user.user_id,
            'email': user.email,
            'roles': user.roles,
            'iat': timezone.now(),
            'exp': exp_ts,
           }
    token = jwt.encode(data, JWT_SECRET, algorithm='HS512')
    return token


def make_pwd_reset_token(user):
    exp_ts = make_expiry_timestamp(3600)
    data = {'exp': exp_ts,
            'iat': timezone.now(),
            'pwd_reset': user.email,
           }
    token = jwt.encode(data, JWT_SECRET, algorithm='HS512')
    return token


def make_expiry_timestamp(fut_secs=86400):
    exp_ts = timezone.now()+datetime.timedelta(seconds=fut_secs)
    return exp_ts
