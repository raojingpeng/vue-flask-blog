"""modified html_format to html, md_format to markdown

Revision ID: d2fae4114cb0
Revises: caf1e21e3a79
Create Date: 2019-04-21 20:10:10.533648

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2fae4114cb0'
down_revision = 'caf1e21e3a79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('html', sa.Text(), nullable=True))
    op.add_column('post', sa.Column('markdown', sa.Text(), nullable=True))
    op.drop_column('post', 'html_format')
    op.drop_column('post', 'md_format')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('md_format', mysql.TEXT(), nullable=True))
    op.add_column('post', sa.Column('html_format', mysql.TEXT(), nullable=True))
    op.drop_column('post', 'markdown')
    op.drop_column('post', 'html')
    # ### end Alembic commands ###