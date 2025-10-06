from starlette.middleware.base import BaseHTTPMiddleware
import time, uuid

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        response.headers['X-Response-Time-Ms'] = str(round(duration * 1000, 2))
        return response
