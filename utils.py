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
