import json
import logging

from django.http import HttpResponse
from django.template import Context

from tardis.tardis_portal.shortcuts import render_response_index,\
    return_response_error
import tardis.apps.aaf.aaf_settings as aaf_settings
from tardis.apps.aaf.utils import authenticate, request_aaf_info
from django.contrib.auth import login

logger = logging.getLogger(__name__)


def authorize(request):

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

    if response is None:
        return return_response_error(request)

    response_dict = json.loads(response)

    # check if response contains error or none
    if 'error' in response_dict:
        return return_response_error(request)

    # check if response doesn't contain mail or cn attributes
    if 'mail' not in response_dict or 'cn' not in response_dict:
        return return_response_error(request)

    username = '__'.join(response_dict['mail'].split("@"))
    first_name = response_dict['cn'].split(" ")[:1][0]
    last_name = ' '.join(response_dict['cn'].split(" ")[1:])
    mail = response_dict['mail']

    c['first_name'] = first_name

    user = authenticate(username, first_name, last_name, mail)

    login(request, user)

    return HttpResponse(render_response_index(
        request, 'aaf/aaf.html', c))
