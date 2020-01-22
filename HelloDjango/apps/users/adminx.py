import xadmin
from users.models import User

class UserXadmin(object):
    list_display = ('username', 'nickname', 'email')

