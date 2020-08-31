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


class KubernetesAutoScaling(object):
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
        'min_node_count': 'int',
        'max_node_count': 'int'
    }

    attribute_map = {
        'min_node_count': 'minNodeCount',
        'max_node_count': 'maxNodeCount'
    }

    def __init__(self, min_node_count=None, max_node_count=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesAutoScaling - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._min_node_count = None
        self._max_node_count = None
        self.discriminator = None

        if min_node_count is not None:
            self.min_node_count = min_node_count
        if max_node_count is not None:
            self.max_node_count = max_node_count

    @property
    def min_node_count(self):
        """Gets the min_node_count of this KubernetesAutoScaling.  # noqa: E501

        The minimum number of worker nodes that the managed node group can scale in. Should be set together with 'maxNodeCount'. Value for this attribute must be greater than equal to 1 and less than equal to maxNodeCount.  # noqa: E501

        :return: The min_node_count of this KubernetesAutoScaling.  # noqa: E501
        :rtype: int
        """
        return self._min_node_count

    @min_node_count.setter
    def min_node_count(self, min_node_count):
        """Sets the min_node_count of this KubernetesAutoScaling.

        The minimum number of worker nodes that the managed node group can scale in. Should be set together with 'maxNodeCount'. Value for this attribute must be greater than equal to 1 and less than equal to maxNodeCount.  # noqa: E501

        :param min_node_count: The min_node_count of this KubernetesAutoScaling.  # noqa: E501
        :type min_node_count: int
        """

        self._min_node_count = min_node_count

    @property
    def max_node_count(self):
        """Gets the max_node_count of this KubernetesAutoScaling.  # noqa: E501

        The maximum number of worker nodes that the managed node pool can scale-out. Should be set together with 'minNodeCount'. Value for this attribute must be greater than equal to 1 and minNodeCount.  # noqa: E501

        :return: The max_node_count of this KubernetesAutoScaling.  # noqa: E501
        :rtype: int
        """
        return self._max_node_count

    @max_node_count.setter
    def max_node_count(self, max_node_count):
        """Sets the max_node_count of this KubernetesAutoScaling.

        The maximum number of worker nodes that the managed node pool can scale-out. Should be set together with 'minNodeCount'. Value for this attribute must be greater than equal to 1 and minNodeCount.  # noqa: E501

        :param max_node_count: The max_node_count of this KubernetesAutoScaling.  # noqa: E501
        :type max_node_count: int
        """

        self._max_node_count = max_node_count

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
        if not isinstance(other, KubernetesAutoScaling):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesAutoScaling):
            return True

        return self.to_dict() != other.to_dict()
