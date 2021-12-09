# coding: utf-8

"""
    CLOUD API

    IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class KubernetesNodePoolLanRoutes(object):
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

        'network': 'str',

        'gateway_ip': 'str',
    }

    attribute_map = {

        'network': 'network',

        'gateway_ip': 'gatewayIp',
    }

    def __init__(self, network=None, gateway_ip=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesNodePoolLanRoutes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._network = None
        self._gateway_ip = None
        self.discriminator = None

        if network is not None:
            self.network = network
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip


    @property
    def network(self):
        """Gets the network of this KubernetesNodePoolLanRoutes.  # noqa: E501

        IPv4 or IPv6 CIDR to be routed via the interface.  # noqa: E501

        :return: The network of this KubernetesNodePoolLanRoutes.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this KubernetesNodePoolLanRoutes.

        IPv4 or IPv6 CIDR to be routed via the interface.  # noqa: E501

        :param network: The network of this KubernetesNodePoolLanRoutes.  # noqa: E501
        :type network: str
        """

        self._network = network

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this KubernetesNodePoolLanRoutes.  # noqa: E501

        IPv4 or IPv6 Gateway IP for the route.  # noqa: E501

        :return: The gateway_ip of this KubernetesNodePoolLanRoutes.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this KubernetesNodePoolLanRoutes.

        IPv4 or IPv6 Gateway IP for the route.  # noqa: E501

        :param gateway_ip: The gateway_ip of this KubernetesNodePoolLanRoutes.  # noqa: E501
        :type gateway_ip: str
        """

        self._gateway_ip = gateway_ip
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
        if not isinstance(other, KubernetesNodePoolLanRoutes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesNodePoolLanRoutes):
            return True

        return self.to_dict() != other.to_dict()
