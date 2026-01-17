"""Error handlers for the application."""

import logging

from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

logger = logging.getLogger(__name__)


def init_error_handlers(app: Flask) -> None:
    """Initialize error handlers for common HTTP errors."""

    @app.errorhandler(404)
    def not_found(error: HTTPException) -> tuple[str, int]:
        """Handle 404 Not Found errors."""
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_error(error: HTTPException) -> tuple[str, int]:
        """Handle 500 Internal Server errors."""
        logger.exception("Internal server error")
        return render_template("errors/500.html"), 500
