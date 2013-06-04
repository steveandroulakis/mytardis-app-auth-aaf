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
```
INSTALLED_APPS = ("tardis.apps.aaf",) + INSTALLED_APPS

AUTH_PROVIDERS = (
    ('localdb', 'Local DB', 'tardis.tardis_portal.auth.localdb_auth.DjangoAuthBackend'),
    ('aaf', 'Australian Access Federation', 'tardis.apps.aaf.auth.aaf_auth.DjangoAuthBackend'),
)

.. for both localdb and aaf auth.
