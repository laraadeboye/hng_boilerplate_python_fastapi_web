"""product comment migration

Revision ID: 224b03e9169c
Revises: 9faa5001e400
Create Date: 2024-08-08 09:15:02.235957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '224b03e9169c'
down_revision: Union[str, None] = '9faa5001e400'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('oauth', 'access_token',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('oauth', 'refresh_token',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('roles', sa.Column('is_builtin', sa.Boolean(), nullable=True))
    op.alter_column('user_organization_roles', 'role_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_organization_roles', 'role_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('roles', 'is_builtin')
    op.alter_column('oauth', 'refresh_token',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('oauth', 'access_token',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
