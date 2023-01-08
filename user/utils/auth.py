import jwt
from user.models.role.ca import CAUser
from user.models.role.startup import StartupUser
from user.models.role.student import StudentUser
from user.models.role.proff import ProffUser

secret = 'django-insecure-*+z5#+d&a@s^7)x^cez!r)mqq^iz8fld@rbo36nyke-%cp%o0i'

def auth(token):
    secret = 'django-insecure-*+z5#+d&a@s^7)x^cez!r)mqq^iz8fld@rbo36nyke-%cp%o0i'
    try:
        decoded = jwt.decode(token, secret, algorithms=['HS256'])
        email = decoded['email']
        password = decoded['password']
        if CAUser.objects.filter(email=email ).exists():
            return CAUser.objects.get(email=email )
        elif StartupUser.objects.filter(email=email ).exists():
            return StartupUser.objects.get(email=email )
        elif StudentUser.objects.filter(email=email ).exists():
            return StudentUser.objects.get(email=email )
        elif ProffUser.objects.filter(email=email ).exists():
            return ProffUser.objects.get(email=email )

    except:
        return False