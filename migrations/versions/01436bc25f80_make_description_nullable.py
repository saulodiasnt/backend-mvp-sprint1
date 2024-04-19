"""make description nullable

Revision ID: 01436bc25f80
Revises: f259ccad6d8d
Create Date: 2024-04-19 19:18:25.104186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01436bc25f80'
down_revision = 'f259ccad6d8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###