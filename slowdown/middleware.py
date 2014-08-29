import time

from django.conf import settings


class SlowDownMiddleware(object):
    def process_request(self, request):
        slowdown = getattr(settings, "SLOWDOWN", 1000)
        time.sleep(slowdown / 1000)
