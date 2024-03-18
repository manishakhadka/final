"""add fields in user table

Revision ID: a0c0228fc163
Revises: 306b93189fc3
Create Date: 2024-03-14 06:28:22.793131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a0c0228fc163'
down_revision: Union[str, None] = '306b93189fc3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drinks', sa.Column('discount', mysql.DOUBLE(asdecimal=True), nullable=True))
    op.add_column('orders', sa.Column('address', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'address')
    op.drop_column('drinks', 'discount')
    # ### end Alembic commands ###
