import connexion
import six

from openapi_server.models.event import Event  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util
from openapi_server.db import db


def events_get(limit=None, offset=None):  # noqa: E501
    """events_get

    Returns a list of events # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of Events to be displayed
    :type offset: int

    :rtype: List[Event]
    """
    events = Event.query.all()
    print("length of events is: " + str(len(events)))
    print(events[0].to_str())
    events_json = []
    for event in events:
        print(event)
        print(event.to_dict())
        events_json.append(event.to_dict())
    print("All events")
    print(events_json)
    return events_json


def events_post(event=None):  # noqa: E501
    """events_post

    Create a new event # noqa: E501

    :param event: 
    :type event: dict | bytes

    :rtype: None
    """
    if event == None:
        # This shouldn't happen, but it seems that connexion is calling
        # this method without passing the event
        # https://github.com/zalando/connexion/issues/1241
        # https://github.com/OpenAPITools/openapi-generator/issues/3345
        # https://github.com/OpenAPITools/openapi-generator/issues/1666
        raise TypeError("events_post got called without an event")
    if connexion.request.is_json:
        event = Event.from_dict(connexion.request.get_json()) # noqa: E501
        db.session.add(event)
        db.session.commit()
    return 'Added event'
