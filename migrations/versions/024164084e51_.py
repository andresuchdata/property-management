"""empty message

Revision ID: 024164084e51
Revises: 
Create Date: 2024-10-04 15:05:31.668061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '024164084e51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('unit_type', sa.Enum('LAND', 'HOUSE', 'ROOM', name='unittype'), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.Column('unit_period', sa.Enum('MONTHS', 'DAYS', 'YEARS', name='unitperiod'), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('images', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('nik', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('profile_picture', sa.String(length=255), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('rentals',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('period', sa.Integer(), nullable=False),
    sa.Column('property_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['property_id'], ['properties.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('currency', sa.Enum('IDR', 'USD', name='currency'), nullable=False),
    sa.Column('payment_status', sa.Boolean(), nullable=False),
    sa.Column('rental_id', sa.String(length=36), nullable=False),
    sa.Column('transaction_id', sa.String(length=100), nullable=True),
    sa.Column('payment_method', sa.String(length=50), nullable=True),
    sa.Column('payment_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['rental_id'], ['rentals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.drop_table('rentals')
    op.drop_table('users')
    op.drop_table('properties')
    # ### end Alembic commands ###
