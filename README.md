mytardis-app-auth-aaf
=====================

OAuth2 based MyTardis authorize (used to authenticate with the Australian Access Federation)

## Note
This is made to work with a custom server (yet to be released) that's composed of:
* A shibboleth Service Provider (see [Australian Access Federation Service Provider Guide](http://wiki.aaf.edu.au/tech-info/sp-install-guide))
* My custom implementation of this OAuth 2 server [oauth2-server-php](https://github.com/bshaffer/oauth2-server-php). This code is not yet released publicly.

## Installing

`git clone <url> aaf` tardis/apps (with the custom name `aaf`)

Example: `/opt/mytardis/current/tardis/apps/aaf/..`

Add to tardis/settings.py
```python
INSTALLED_APPS = ("tardis.apps.aaf",) + INSTALLED_APPS

# For both localdb and aaf auth.
AUTH_PROVIDERS = (
    ('localdb', 'Local DB', 'tardis.tardis_portal.auth.localdb_auth.DjangoAuthBackend'),
    ('aaf', 'Australian Access Federation', 'tardis.apps.aaf.auth.aaf_auth.DjangoAuthBackend'),
)

AAF_OAUTH2_AUTHORIZE_URL = 'https://my-oauth2-server/oauth-aaf/authorize.php'
AAF_OAUTH2_CLIENT_ID = 'my-oauth2-client-id'

# url used to retrieve user credentials from auth server using auth code
AAF_OAUTH2_CODE_URL = 'http://bdp-aaf-dev.dyndns.org/code.php'
