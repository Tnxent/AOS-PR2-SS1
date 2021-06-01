# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.cliente_links_parent import ClienteLinksParent  # noqa: F401,E501
from swagger_server import util


class ClienteLinks(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, parent: ClienteLinksParent=None, _self: ClienteLinksParent=None):  # noqa: E501
        """ClienteLinks - a model defined in Swagger

        :param parent: The parent of this ClienteLinks.  # noqa: E501
        :type parent: ClienteLinksParent
        :param _self: The _self of this ClienteLinks.  # noqa: E501
        :type _self: ClienteLinksParent
        """
        self.swagger_types = {
            'parent': ClienteLinksParent,
            '_self': ClienteLinksParent
        }

        self.attribute_map = {
            'parent': 'parent',
            '_self': 'self'
        }
        self._parent = parent
        self.__self = _self

    @classmethod
    def from_dict(cls, dikt) -> 'ClienteLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cliente_links of this ClienteLinks.  # noqa: E501
        :rtype: ClienteLinks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parent(self) -> ClienteLinksParent:
        """Gets the parent of this ClienteLinks.


        :return: The parent of this ClienteLinks.
        :rtype: ClienteLinksParent
        """
        return self._parent

    @parent.setter
    def parent(self, parent: ClienteLinksParent):
        """Sets the parent of this ClienteLinks.


        :param parent: The parent of this ClienteLinks.
        :type parent: ClienteLinksParent
        """

        self._parent = parent

    @property
    def _self(self) -> ClienteLinksParent:
        """Gets the _self of this ClienteLinks.


        :return: The _self of this ClienteLinks.
        :rtype: ClienteLinksParent
        """
        return self.__self

    @_self.setter
    def _self(self, _self: ClienteLinksParent):
        """Sets the _self of this ClienteLinks.


        :param _self: The _self of this ClienteLinks.
        :type _self: ClienteLinksParent
        """

        self.__self = _self