"""empty message

Revision ID: 705551842be1
Revises: 
Create Date: 2019-02-11 18:26:25.983495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '705551842be1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uname', sa.String(length=30), nullable=False),
    sa.Column('upwd', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###