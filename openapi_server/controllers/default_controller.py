import connexion
import six

from openapi_server.services import event_service as EventService
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util


def events_get(limit=None, offset=None):  # noqa: E501
    """events_get

    Returns a list of events # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of Events to be displayed
    :type offset: int

    :rtype: List[Event]
    """
    events = EventService.get_all()
    return events

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
        EventService.add_event(connexion.request.get_json())
  
    return 'Added event'
