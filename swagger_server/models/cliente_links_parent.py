# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ClienteLinksParent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, href: str=None, rel: str=None):  # noqa: E501
        """ClienteLinksParent - a model defined in Swagger

        :param href: The href of this ClienteLinksParent.  # noqa: E501
        :type href: str
        :param rel: The rel of this ClienteLinksParent.  # noqa: E501
        :type rel: str
        """
        self.swagger_types = {
            'href': str,
            'rel': str
        }

        self.attribute_map = {
            'href': 'href',
            'rel': 'rel'
        }
        self._href = href
        self._rel = rel

    @classmethod
    def from_dict(cls, dikt) -> 'ClienteLinksParent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cliente_links_parent of this ClienteLinksParent.  # noqa: E501
        :rtype: ClienteLinksParent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self) -> str:
        """Gets the href of this ClienteLinksParent.

        URL del enlace  # noqa: E501

        :return: The href of this ClienteLinksParent.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this ClienteLinksParent.

        URL del enlace  # noqa: E501

        :param href: The href of this ClienteLinksParent.
        :type href: str
        """

        self._href = href

    @property
    def rel(self) -> str:
        """Gets the rel of this ClienteLinksParent.

        Relación del documento enlazado con el actual. Contiene una lista de tipos de enlaces separados por espacio.  # noqa: E501

        :return: The rel of this ClienteLinksParent.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel: str):
        """Sets the rel of this ClienteLinksParent.

        Relación del documento enlazado con el actual. Contiene una lista de tipos de enlaces separados por espacio.  # noqa: E501

        :param rel: The rel of this ClienteLinksParent.
        :type rel: str
        """

        self._rel = rel
