"""Initial Migration

Revision ID: 02ef5e605078
Revises: 
Create Date: 2022-05-11 00:19:47.838069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02ef5e605078'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('about', sa.String(length=255), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('password_encrypt', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.add_column('pitches', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('pitches', sa.Column('text', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('posted', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.drop_column('pitches', 'users')
    op.drop_column('pitches', 'name')
    op.drop_column('pitches', 'pitch')
    op.drop_column('pitches', 'pitches_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitches_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('pitches', sa.Column('pitch', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('users', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'posted')
    op.drop_column('pitches', 'user_id')
    op.drop_column('pitches', 'text')
    op.drop_column('pitches', 'category')
    op.drop_column('pitches', 'id')
    op.drop_table('users')
    # ### end Alembic commands ###
