import time
from collections import defaultdict
from starlette.middleware.base import BaseHTTPMiddleware

_requests = defaultdict(list)
WINDOW_SECONDS = 60
MAX_REQUESTS = 120


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        client_ip = request.client.host
        now = time.time()
        _requests[client_ip] = [t for t in _requests[client_ip] if now - t < WINDOW_SECONDS]
        if len(_requests[client_ip]) >= MAX_REQUESTS:
            from starlette.responses import JSONResponse
            return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)
        _requests[client_ip].append(now)
        return await call_next(request)