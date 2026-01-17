"""Health check endpoints for Kubernetes probes."""

from flask import Blueprint, Response

bp = Blueprint("health", __name__)


@bp.route("/health")
def health() -> Response:
    """Liveness probe endpoint."""
    return Response("ok", status=200, mimetype="text/plain")


@bp.route("/ready")
def ready() -> Response:
    """Readiness probe endpoint."""
    # TODO: Add database connectivity check when DB is added
    return Response("ok", status=200, mimetype="text/plain")
