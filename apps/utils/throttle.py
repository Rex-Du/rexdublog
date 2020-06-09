"""
throttle: 
"""
# Author     : root
# FileName   : throttle.py
# CreateDate : 2019-09-04 19:23
from rest_framework.throttling import SimpleRateThrottle


class IPThrottle(SimpleRateThrottle):
    scope = 'anonymous'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


