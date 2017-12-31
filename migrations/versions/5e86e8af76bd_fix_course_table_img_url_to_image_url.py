"""fix Course table img_url to image_url

Revision ID: 5e86e8af76bd
Revises: d7b57970d49c
Create Date: 2018-01-01 00:33:28.627860

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5e86e8af76bd'
down_revision = 'd7b57970d49c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('image_url', sa.String(length=256), nullable=True))
    op.drop_column('course', 'img_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('img_url', mysql.VARCHAR(length=256), nullable=True))
    op.drop_column('course', 'image_url')
    # ### end Alembic commands ###
