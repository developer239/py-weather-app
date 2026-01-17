"""Initial schema with cities and weather_codes tables.

Revision ID: 001
Revises:
Create Date: 2025-01-17

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "cities",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_cities_name"), "cities", ["name"], unique=True)

    op.create_table(
        "weather_codes",
        sa.Column("code", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("code"),
    )


def downgrade() -> None:
    op.drop_table("weather_codes")
    op.drop_index(op.f("ix_cities_name"), table_name="cities")
    op.drop_table("cities")
