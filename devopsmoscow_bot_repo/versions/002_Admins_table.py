from sqlalchemy import *
from migrate import *

meta = MetaData()

admins = Table(
    'greetings_message', meta,
    Column('id', Integer, primary_key=True)
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    admins.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    admins.drop()