import json
import logging

from django.http import HttpResponse
from django.template import Context

from tardis.tardis_portal.shortcuts import render_response_index
import tardis.apps.aaf.aaf_settings as aaf_settings
from tardis.apps.aaf.utils import authenticate
from django.contrib.auth import login

logger = logging.getLogger(__name__)


def authorize(request):

    # c = Context({'authorization_code': authorization_code,
    #              })

    c = Context({})

    if 'code' in request.GET:
        c['authorization_code'] = request.GET['code']
    if 'state' in request.GET:
        c['state'] = request.GET['state']

    user = authenticate('steve.androulakis')

    login(request, user)

    return HttpResponse(render_response_index(
        request, 'aaf/aaf.html', c))
