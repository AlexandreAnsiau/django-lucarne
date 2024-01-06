import re

from django.http import HttpResponseRedirect
from django.shortcuts import redirect


class WWWRedirectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()

        match = re.match(r"www\.(.*)", host)


        if match:
            return HttpResponseRedirect(f"http://{match.group(1)}{request.path}")

        return self.get_response(request)