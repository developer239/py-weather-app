"""Health check endpoints for Kubernetes probes."""

from flask import Blueprint, Response, g
from sqlmodel import Session, text

bp = Blueprint("health", __name__)


@bp.route("/health")
def health() -> Response:
    """Liveness probe endpoint."""
    return Response("ok", status=200, mimetype="text/plain")


@bp.route("/ready")
def ready() -> Response:
    """Readiness probe endpoint."""
    try:
        session: Session = g.db_session
        session.exec(text("SELECT 1"))  # type: ignore[call-overload]
        return Response("ok", status=200, mimetype="text/plain")
    except Exception:
        return Response("database unavailable", status=503, mimetype="text/plain")
