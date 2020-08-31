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


class LoadbalancerProperties(object):
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
        'ip': 'str',
        'dhcp': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'ip': 'ip',
        'dhcp': 'dhcp'
    }

    def __init__(self, name=None, ip=None, dhcp=None, local_vars_configuration=None):  # noqa: E501
        """LoadbalancerProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._ip = None
        self._dhcp = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if dhcp is not None:
            self.dhcp = dhcp

    @property
    def name(self):
        """Gets the name of this LoadbalancerProperties.  # noqa: E501

        A name of that resource  # noqa: E501

        :return: The name of this LoadbalancerProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadbalancerProperties.

        A name of that resource  # noqa: E501

        :param name: The name of this LoadbalancerProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def ip(self):
        """Gets the ip of this LoadbalancerProperties.  # noqa: E501

        IPv4 address of the loadbalancer. All attached NICs will inherit this IP. Leaving value null will assign IP automatically  # noqa: E501

        :return: The ip of this LoadbalancerProperties.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this LoadbalancerProperties.

        IPv4 address of the loadbalancer. All attached NICs will inherit this IP. Leaving value null will assign IP automatically  # noqa: E501

        :param ip: The ip of this LoadbalancerProperties.  # noqa: E501
        :type ip: str
        """
        allowed_values = ["@Valid IP address@", "null"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and ip not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `ip` ({0}), must be one of {1}"  # noqa: E501
                .format(ip, allowed_values)
            )

        self._ip = ip

    @property
    def dhcp(self):
        """Gets the dhcp of this LoadbalancerProperties.  # noqa: E501

        Indicates if the loadbalancer will reserve an IP using DHCP  # noqa: E501

        :return: The dhcp of this LoadbalancerProperties.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """Sets the dhcp of this LoadbalancerProperties.

        Indicates if the loadbalancer will reserve an IP using DHCP  # noqa: E501

        :param dhcp: The dhcp of this LoadbalancerProperties.  # noqa: E501
        :type dhcp: bool
        """

        self._dhcp = dhcp

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
        if not isinstance(other, LoadbalancerProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoadbalancerProperties):
            return True

        return self.to_dict() != other.to_dict()
