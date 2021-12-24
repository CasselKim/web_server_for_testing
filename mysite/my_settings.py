import sys
import json
import os

#BASE_DIR = ...
#print(BASE_DIR)
#ROOT_DIR = os.path.dirname(BASE_DIR)
#SECRETS_PATH = os.path.join(ROOT_DIR, 'secret.join')
secrets = json.loads(open('secret.json').read())

for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'django_table',
        'USER' : 'root',
        'PASSWORD' : PASSWORD,
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}