"""Security middleware for adding security headers."""

from flask import Flask, Response


def init_security_middleware(app: Flask) -> None:
    """Initialize security middleware with security headers."""

    @app.after_request
    def add_security_headers(response: Response) -> Response:
        """Add security headers to all responses."""
        # Prevent MIME type sniffing
        response.headers["X-Content-Type-Options"] = "nosniff"

        # Prevent clickjacking
        response.headers["X-Frame-Options"] = "DENY"

        # Enable XSS filter
        response.headers["X-XSS-Protection"] = "1; mode=block"

        # Control referrer information
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

        # Content Security Policy
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "style-src 'self' https://cdn.jsdelivr.net; "
            "script-src 'self'; "
            "img-src 'self' data:; "
            "font-src 'self' https://cdn.jsdelivr.net; "
        )

        return response
