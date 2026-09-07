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
            response = JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)
            response.headers["X-RateLimit-Limit"] = str(MAX_REQUESTS)
            response.headers["X-RateLimit-Remaining"] = "0"
            return response
        _requests[client_ip].append(now)
        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = str(MAX_REQUESTS)
        response.headers["X-RateLimit-Remaining"] = str(MAX_REQUESTS - len(_requests[client_ip]))
        return response