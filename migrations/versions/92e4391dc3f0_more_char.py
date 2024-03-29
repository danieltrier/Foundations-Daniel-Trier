"""more char

Revision ID: 92e4391dc3f0
Revises: 406cf4f73784
Create Date: 2023-04-12 17:17:33.836604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92e4391dc3f0'
down_revision = '406cf4f73784'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('e_mail',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=150),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('e_mail',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=80),
               existing_nullable=True)

    # ### end Alembic commands ###
