import logging
import time

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('default')


class ExceptionLoggingMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        import traceback
        logger.error(traceback.format_exc())


class ResponseTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.ctime = time.time()

    def process_response(self, request, response):
        if request.path != '/favicon.ico':
            logger.info(f'reponse time of {request.path}: {time.time() - request.ctime}')
        return response
