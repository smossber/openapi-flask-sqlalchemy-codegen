from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry
from openapi_server.models import Event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

mapper_registry = registry()


event_table = Table(
    'event',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('cluster', String(50)),
    Column('message', String(50)),
)

mapper_registry.map_imperatively(Event, event_table, column_prefix='_')

mapper_registry.metadata.create_all(engine)