# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionos_cloud_sdk_python.configuration import Configuration


class Peer(object):
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
        'name': 'str',
        'datacenter_id': 'str',
        'datacenter_name': 'str',
        'location': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'datacenter_id': 'datacenterId',
        'datacenter_name': 'datacenterName',
        'location': 'location'
    }

    def __init__(self, id=None, name=None, datacenter_id=None, datacenter_name=None, location=None, local_vars_configuration=None):  # noqa: E501
        """Peer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._datacenter_id = None
        self._datacenter_name = None
        self._location = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if datacenter_id is not None:
            self.datacenter_id = datacenter_id
        if datacenter_name is not None:
            self.datacenter_name = datacenter_name
        if location is not None:
            self.location = location

    @property
    def id(self):
        """Gets the id of this Peer.  # noqa: E501


        :return: The id of this Peer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Peer.


        :param id: The id of this Peer.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Peer.  # noqa: E501


        :return: The name of this Peer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Peer.


        :param name: The name of this Peer.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def datacenter_id(self):
        """Gets the datacenter_id of this Peer.  # noqa: E501


        :return: The datacenter_id of this Peer.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_id

    @datacenter_id.setter
    def datacenter_id(self, datacenter_id):
        """Sets the datacenter_id of this Peer.


        :param datacenter_id: The datacenter_id of this Peer.  # noqa: E501
        :type datacenter_id: str
        """

        self._datacenter_id = datacenter_id

    @property
    def datacenter_name(self):
        """Gets the datacenter_name of this Peer.  # noqa: E501


        :return: The datacenter_name of this Peer.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_name

    @datacenter_name.setter
    def datacenter_name(self, datacenter_name):
        """Sets the datacenter_name of this Peer.


        :param datacenter_name: The datacenter_name of this Peer.  # noqa: E501
        :type datacenter_name: str
        """

        self._datacenter_name = datacenter_name

    @property
    def location(self):
        """Gets the location of this Peer.  # noqa: E501


        :return: The location of this Peer.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Peer.


        :param location: The location of this Peer.  # noqa: E501
        :type location: str
        """

        self._location = location

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
        if not isinstance(other, Peer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Peer):
            return True

        return self.to_dict() != other.to_dict()
