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


class PrivateCrossConnectProperties(object):
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
        'name': 'str',
        'description': 'str',
        'peers': 'list[Peer]',
        'connectable_datacenters': 'list[ConnectableDatacenter]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'peers': 'peers',
        'connectable_datacenters': 'connectableDatacenters'
    }

    def __init__(self, name=None, description=None, peers=None, connectable_datacenters=None, local_vars_configuration=None):  # noqa: E501
        """PrivateCrossConnectProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._peers = None
        self._connectable_datacenters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if peers is not None:
            self.peers = peers
        if connectable_datacenters is not None:
            self.connectable_datacenters = connectable_datacenters

    @property
    def name(self):
        """Gets the name of this PrivateCrossConnectProperties.  # noqa: E501

        A name of that resource  # noqa: E501

        :return: The name of this PrivateCrossConnectProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrivateCrossConnectProperties.

        A name of that resource  # noqa: E501

        :param name: The name of this PrivateCrossConnectProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PrivateCrossConnectProperties.  # noqa: E501

        Human readable description  # noqa: E501

        :return: The description of this PrivateCrossConnectProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PrivateCrossConnectProperties.

        Human readable description  # noqa: E501

        :param description: The description of this PrivateCrossConnectProperties.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def peers(self):
        """Gets the peers of this PrivateCrossConnectProperties.  # noqa: E501

        Read-Only attribute. Lists LAN's joined to this private cross connect  # noqa: E501

        :return: The peers of this PrivateCrossConnectProperties.  # noqa: E501
        :rtype: list[Peer]
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this PrivateCrossConnectProperties.

        Read-Only attribute. Lists LAN's joined to this private cross connect  # noqa: E501

        :param peers: The peers of this PrivateCrossConnectProperties.  # noqa: E501
        :type peers: list[Peer]
        """

        self._peers = peers

    @property
    def connectable_datacenters(self):
        """Gets the connectable_datacenters of this PrivateCrossConnectProperties.  # noqa: E501

        Read-Only attribute. Lists datacenters that can be joined to this private cross connect  # noqa: E501

        :return: The connectable_datacenters of this PrivateCrossConnectProperties.  # noqa: E501
        :rtype: list[ConnectableDatacenter]
        """
        return self._connectable_datacenters

    @connectable_datacenters.setter
    def connectable_datacenters(self, connectable_datacenters):
        """Sets the connectable_datacenters of this PrivateCrossConnectProperties.

        Read-Only attribute. Lists datacenters that can be joined to this private cross connect  # noqa: E501

        :param connectable_datacenters: The connectable_datacenters of this PrivateCrossConnectProperties.  # noqa: E501
        :type connectable_datacenters: list[ConnectableDatacenter]
        """

        self._connectable_datacenters = connectable_datacenters

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
        if not isinstance(other, PrivateCrossConnectProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrivateCrossConnectProperties):
            return True

        return self.to_dict() != other.to_dict()
