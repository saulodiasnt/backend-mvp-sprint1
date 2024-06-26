"""create task table

Revision ID: f87f0ae8e2a0
Revises: 41ed9e9033b7
Create Date: 2024-04-18 15:03:48.884796

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f87f0ae8e2a0"
down_revision = "41ed9e9033b7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "task",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=80), nullable=False),
        sa.Column("description", sa.String(length=120), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("end_time", sa.Time(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task")
    # ### end Alembic commands ###
