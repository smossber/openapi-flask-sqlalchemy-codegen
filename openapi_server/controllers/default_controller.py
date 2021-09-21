import connexion
import six

from openapi_server.models.event import Event  # noqa: E501
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
    return 'do some magic!'


def events_post(event):  # noqa: E501
    """events_post

    Create a new event # noqa: E501

    :param event: 
    :type event: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        event = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
