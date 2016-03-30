revision = '1009b61529d2'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lyrics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('url', sa.Unicode(length=255), nullable=True),
    sa.Column('html', sa.UnicodeText(), nullable=True),
    sa.Column('provider', sa.Unicode(length=255), nullable=True),
    sa.Column('artist', sa.Unicode(length=255), nullable=True),
    sa.Column('title', sa.Unicode(length=255), nullable=True),
    sa.Column('text', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('artist', 'title', name=u'ix_artist_title')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lyrics')
    ### end Alembic commands ###
