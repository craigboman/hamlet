# This file is designed for use with `heroku local`.
from .heroku import *  # noqa

ALLOWED_HOSTS = ['0.0.0.0']

SECRET_KEY = 'f=fqwc&$zt_6rf8y45j1l7w!^e*%a_c)4sf+v*_uf%hwf5_*16'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
