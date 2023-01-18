import jwt
from user.models.role.ca import CAUser
from user.models.role.startup import StartupUser
from user.models.role.student import StudentUser
from user.models.role.proff import ProffUser

secret = '7o9d=)+(f-chzvhcr#*(dc6k!#8&q2=)w5m4a+d$-$m&)hr4gh'

def auth(token):
    secret = '7o9d=)+(f-chzvhcr#*(dc6k!#8&q2=)w5m4a+d$-$m&)hr4gh'
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
        return None
def get_cap(esummit_id,point):
        if CAUser.objects.filter(esummit_id=esummit_id ).exists():
             CAUser.objects.get(esummit_id=esummit_id).points  = point + CAUser.objects.get(esummit_id=esummit_id).points
        else:
            return False