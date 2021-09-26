# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util
from openapi_server.db import db



class Event(db.Model,Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """
    _id = db.Column(db.Integer, primary_key=True)
    _cluster = db.Column(db.String(80), unique=False, nullable=False)
    _message = db.Column(db.String(80), unique=False, nullable=False)
 
#    def __repr__(self):
#        return '<Event %r>' % self.id
    openapi_types = {
        'id': int,
        'cluster': str,
        'message': str
    }

    attribute_map = {
        'id': 'id',
        'cluster': 'cluster',
        'message': 'message'
    }
    
    def __init__(self, id=None, cluster=None, message=None, **kwargs):  # noqa: E501
        db.Model.__init__(self,**kwargs)
        """Event - a model defined in OpenAPI

        :param id: The id of this Event.  # noqa: E501
        :type id: int
        :param cluster: The cluster of this Event.  # noqa: E501
        :type cluster: str
        :param message: The message of this Event.  # noqa: E501
        :type message: str
        """

        self._id = id
        self._cluster = cluster
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'Event':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Event of this Event.  # noqa: E501
        :rtype: Event
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Event.


        :return: The id of this Event.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event.


        :param id: The id of this Event.
        :type id: int
        """

        self._id = id

    @property
    def cluster(self):
        """Gets the cluster of this Event.


        :return: The cluster of this Event.
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Event.


        :param cluster: The cluster of this Event.
        :type cluster: str
        """

        self._cluster = cluster

    @property
    def message(self):
        """Gets the message of this Event.


        :return: The message of this Event.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Event.


        :param message: The message of this Event.
        :type message: str
        """

        self._message = message
