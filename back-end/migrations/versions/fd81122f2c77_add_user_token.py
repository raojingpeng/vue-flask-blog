"""add user token

Revision ID: fd81122f2c77
Revises: 18b2f67ff7ef
Create Date: 2019-04-11 19:50:12.365719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd81122f2c77'
down_revision = '18b2f67ff7ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'token_expiration')
    # ### end Alembic commands ###
