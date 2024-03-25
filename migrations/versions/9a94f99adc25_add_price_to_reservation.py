"""Add price to reservation

Revision ID: 9a94f99adc25
Revises: 0af48b2b9540
Create Date: 2024-03-23 17:26:34.197097

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9a94f99adc25'
down_revision = '0af48b2b9540'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.drop_column('total')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total', mysql.DECIMAL(precision=10, scale=2), nullable=False))

    # ### end Alembic commands ###
