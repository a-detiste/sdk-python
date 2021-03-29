# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0-SDK.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class Group(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'type': 'Type',
        'href': 'str',
        'properties': 'GroupProperties',
        'entities': 'GroupEntities',
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'href': 'href',
        'properties': 'properties',
        'entities': 'entities',
    }

    def __init__(self, id=None, type=None, href=None, properties=None, entities=None, local_vars_configuration=None):  # noqa: E501
        """Group - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._href = None
        self._properties = None
        self._entities = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if href is not None:
            self.href = href
        self.properties = properties
        if entities is not None:
            self.entities = entities

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501

        The resource's unique identifier  # noqa: E501

        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.

        The resource's unique identifier  # noqa: E501

        :param id: The id of this Group.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Group.  # noqa: E501

        The type of the resource  # noqa: E501

        :return: The type of this Group.  # noqa: E501
        :rtype: Type
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Group.

        The type of the resource  # noqa: E501

        :param type: The type of this Group.  # noqa: E501
        :type type: Type
        """

        self._type = type

    @property
    def href(self):
        """Gets the href of this Group.  # noqa: E501

        URL to the object representation (absolute path)  # noqa: E501

        :return: The href of this Group.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Group.

        URL to the object representation (absolute path)  # noqa: E501

        :param href: The href of this Group.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def properties(self):
        """Gets the properties of this Group.  # noqa: E501


        :return: The properties of this Group.  # noqa: E501
        :rtype: GroupProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Group.


        :param properties: The properties of this Group.  # noqa: E501
        :type properties: GroupProperties
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def entities(self):
        """Gets the entities of this Group.  # noqa: E501


        :return: The entities of this Group.  # noqa: E501
        :rtype: GroupEntities
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this Group.


        :param entities: The entities of this Group.  # noqa: E501
        :type entities: GroupEntities
        """

        self._entities = entities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Group):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Group):
            return True

        return self.to_dict() != other.to_dict()
