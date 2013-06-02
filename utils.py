import urllib
import urllib2
from tardis.tardis_portal.auth.authservice import AuthService

auth_key = 'aaf'


def authenticate(username):
    #todo take attr array
    user_dict = {'id': username}

    auth_service = AuthService()
    user = auth_service._get_or_create_user_from_dict(
        user_dict, auth_key)

    user.backend = 'django.contrib.auth.backends.ModelBackend'

    return user


def request_aaf_info(url, code, state):
    url_values = urllib.urlencode({'code': code, 'state': state})
    full_url = url + '?' + url_values
    response = urllib2.urlopen(full_url)
    aaf_attr_json = response.read()
    return aaf_attr_json
