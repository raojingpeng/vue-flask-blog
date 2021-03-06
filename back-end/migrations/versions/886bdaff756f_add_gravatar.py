"""add gravatar ..

Revision ID: 886bdaff756f
Revises: b6a3bfcc703f
Create Date: 2019-04-18 14:54:12.154807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '886bdaff756f'
down_revision = 'b6a3bfcc703f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('user', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'name')
    op.drop_column('user', 'member_since')
    op.drop_column('user', 'location')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
