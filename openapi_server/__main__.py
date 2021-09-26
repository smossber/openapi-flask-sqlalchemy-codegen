#!/usr/bin/env python3

import connexion
import sys
import logging
from openapi_server import encoder
from openapi_server.db import db

from openapi_server.models import Event

app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
app.app.logger.setLevel(logging.DEBUG)
app.app.json_encoder = encoder.JSONEncoder

app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.app = app.app


db.init_app(app.app)


# create_all ensures that the table is created in the DB
# if it's already present, it doesn't do anything
db.create_all()
events = Event.query.all()
#new_event = Event(id="1",cluster="test",message="message")
#db.session.add(new_event)
#db.session.commit()


app.add_api('openapi.yaml',
            arguments={'title': 'OpsLog API'},
            pythonic_params=True)

application = app.app
