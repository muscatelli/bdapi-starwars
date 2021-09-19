"""empty message

Revision ID: 9482a27d2fef
Revises: 2002df49b364
Create Date: 2021-09-18 01:16:36.939943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9482a27d2fef'
down_revision = '2002df49b364'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), nullable=False),
    sa.Column('model', sa.VARCHAR(length=10), nullable=False),
    sa.Column('vehicle_class', sa.VARCHAR(length=30), nullable=False),
    sa.Column('crews', sa.VARCHAR(length=30), nullable=False),
    sa.Column('manufacturer', sa.VARCHAR(length=30), nullable=False),
    sa.Column('cost_in_credits', sa.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###