import json
import logging

from django.http import HttpResponse
from django.template import Context

from tardis.tardis_portal.shortcuts import render_response_index
import tardis.apps.aaf.aaf_settings as aaf_settings
from tardis.apps.aaf.utils import authenticate, request_aaf_info
from django.contrib.auth import login

logger = logging.getLogger(__name__)


def authorize(request):

    # c = Context({'authorization_code': authorization_code,
    #              })

    # TODO real state randomly generated, URL in settings
    url = 'http://bdp-aaf-dev.dyndns.org/oauth-aaf-insecure/code.php'
    code = ''
    state = ''

    c = Context({})

    if 'code' in request.GET:
        c['authorization_code'] = request.GET['code']
        code = request.GET['code']
    if 'state' in request.GET:
        c['state'] = request.GET['state']
        state = request.GET['state']

    response = request_aaf_info(url=url, code=code, state=state)
    c['response'] = response

    #user = authenticate('steve.androulakis')

    #login(request, user)

    return HttpResponse(render_response_index(
        request, 'aaf/aaf.html', c))
