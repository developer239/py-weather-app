"""Logging middleware for request tracking."""

import logging
import time
import uuid

from flask import Flask, Response, g, request

logger = logging.getLogger(__name__)


def init_logging_middleware(app: Flask) -> None:
    """Initialize logging middleware with request tracking."""

    @app.before_request
    def before_request() -> None:
        """Add request ID and start time for tracking."""
        g.request_id = uuid.uuid4().hex[:8]
        g.start_time = time.perf_counter()

    @app.after_request
    def after_request(response: Response) -> Response:
        """Log request details and add request ID header."""
        duration_ms = (time.perf_counter() - g.start_time) * 1000

        logger.info(
            "Request completed",
            extra={
                "request_id": g.request_id,
                "method": request.method,
                "path": request.path,
                "status": response.status_code,
                "duration_ms": round(duration_ms, 2),
            },
        )

        response.headers["X-Request-ID"] = g.request_id
        return response
