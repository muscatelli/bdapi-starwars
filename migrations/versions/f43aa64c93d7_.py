"""empty message

Revision ID: f43aa64c93d7
Revises: 9482a27d2fef
Create Date: 2021-09-18 01:18:34.211245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f43aa64c93d7'
down_revision = '9482a27d2fef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('model', sa.String(length=10), nullable=False),
    sa.Column('vehicle_class', sa.String(length=30), nullable=False),
    sa.Column('crews', sa.String(length=30), nullable=False),
    sa.Column('manufacturer', sa.String(length=30), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    # ### end Alembic commands ###