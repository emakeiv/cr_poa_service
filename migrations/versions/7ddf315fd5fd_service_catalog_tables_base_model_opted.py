"""service_catalog_tables_base_model_opted

Revision ID: 7ddf315fd5fd
Revises: 08dde328e988
Create Date: 2024-01-17 09:38:30.462311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ddf315fd5fd'
down_revision: Union[str, None] = '08dde328e988'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('serviso_katalogas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('paslaugos_kodas', sa.String(), nullable=False),
    sa.Column('institucijos_kodas', sa.Integer(), nullable=True),
    sa.Column('institucijos_pavadinimas', sa.String(), nullable=True),
    sa.Column('paslaugos_pavadinimas', sa.String(), nullable=True),
    sa.Column('paslaugos_tipas', sa.String(), nullable=True),
    sa.Column('el_paslauga', sa.String(), nullable=True),
    sa.Column('tik_notarinis', sa.Boolean(), nullable=True),
    sa.Column('prokuratura', sa.Boolean(), nullable=True),
    sa.Column('aktyvumas', sa.Boolean(), nullable=True),
    sa.Column('galioja_nuo', sa.Date(), nullable=True),
    sa.Column('galioja_iki', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'paslaugos_kodas')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('serviso_katalogas')
    # ### end Alembic commands ###
