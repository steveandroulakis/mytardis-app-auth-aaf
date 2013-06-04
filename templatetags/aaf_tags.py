from django import template
import tardis.apps.aaf.aaf_settings as aaf_settings
import os

register = template.Library()


@register.tag(name="random_oauth_state")
def do_random_oauth_state(value, token):
    return RandomOAuthState()


class RandomOAuthState(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return os.urandom(16).encode('hex')


@register.tag(name="aaf_oauth2_authorize_url")
def do_authorize_url(value, token):
    return AuthorizeURL()


class AuthorizeURL(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return aaf_settings.AAF_OAUTH2_AUTHORIZE_URL


@register.tag(name="aaf_oauth2_client_id")
def do_client_id(value, token):
    return ClientID()


class ClientID(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return aaf_settings.AAF_OAUTH2_CLIENT_ID
