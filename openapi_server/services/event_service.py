from openapi_server.models import Event

from openapi_server.db import session


def get_all():
    events = session.query(Event).all()
    print("length of events is: " + str(len(events)))
    events_json = []
    for event in events:
        print(event)
        print(event.to_dict())
        events_json.append(event.to_dict())
    print("All events")
    print(events_json)
    return events_json

def add_event(event_json):
    event = Event.from_dict(event_json) # noqa: E501
    session.add(event)
    session.commit()
