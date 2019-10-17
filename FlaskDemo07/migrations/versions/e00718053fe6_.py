"""empty message

Revision ID: e00718053fe6
Revises: 44ad030f8da1
Create Date: 2019-01-31 10:03:14.609958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e00718053fe6'
down_revision = '44ad030f8da1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wife', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'wife', ['user_id'])
    op.create_foreign_key(None, 'wife', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wife', type_='foreignkey')
    op.drop_constraint(None, 'wife', type_='unique')
    op.drop_column('wife', 'user_id')
    # ### end Alembic commands ###