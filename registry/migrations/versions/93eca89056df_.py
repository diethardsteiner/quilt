"""Role support

Revision ID: 93eca89056df
Revises: cab5dbaad226
Create Date: 2019-01-23 16:59:59.667540

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '93eca89056df'
down_revision = 'cab5dbaad226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('arn', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('user', sa.Column('role_id', postgresql.UUID(), nullable=True))
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    op.drop_table('role')
    # ### end Alembic commands ###
