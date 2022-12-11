import jwt
from user.models.role.ca import CAUser
from user.models.role.startup import StartupUser
from user.models.role.student import StudentUser
from user.models.role.proff import ProffUser

secret = 'django-insecure-*+z5#+d&a@s^7)x^cez!r)mqq^iz8fld@rbo36nyke-%cp%o0i'

def auth(token):
    try:
        decoded = jwt.decode(token, secret, algorithms=['HS256'])
        email = decoded['email']
        password = decoded['password']
        if CAUser.objects.filter(email=email,password=password).exists():
            return CAUser.objects.get(email=email,password=password)
        elif StartupUser.objects.filter(email=email,password=password).exists():
            return StartupUser.objects.get(email=email,password=password)
        elif StudentUser.objects.filter(email=email,password=password).exists():
            return StudentUser.objects.get(email=email,password=password)
        elif ProffUser.objects.filter(email=email,password=password).exists():
            return ProffUser.objects.get(email=email,password=password)

    except:
        return False