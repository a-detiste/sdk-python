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


class GroupShareProperties(object):
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

        'edit_privilege': 'bool',

        'share_privilege': 'bool',
    }

    attribute_map = {

        'edit_privilege': 'editPrivilege',

        'share_privilege': 'sharePrivilege',
    }

    def __init__(self, edit_privilege=None, share_privilege=None, local_vars_configuration=None):  # noqa: E501
        """GroupShareProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._edit_privilege = None
        self._share_privilege = None
        self.discriminator = None

        if edit_privilege is not None:
            self.edit_privilege = edit_privilege
        if share_privilege is not None:
            self.share_privilege = share_privilege


    @property
    def edit_privilege(self):
        """Gets the edit_privilege of this GroupShareProperties.  # noqa: E501

        edit privilege on a resource  # noqa: E501

        :return: The edit_privilege of this GroupShareProperties.  # noqa: E501
        :rtype: bool
        """
        return self._edit_privilege

    @edit_privilege.setter
    def edit_privilege(self, edit_privilege):
        """Sets the edit_privilege of this GroupShareProperties.

        edit privilege on a resource  # noqa: E501

        :param edit_privilege: The edit_privilege of this GroupShareProperties.  # noqa: E501
        :type edit_privilege: bool
        """

        self._edit_privilege = edit_privilege

    @property
    def share_privilege(self):
        """Gets the share_privilege of this GroupShareProperties.  # noqa: E501

        share privilege on a resource  # noqa: E501

        :return: The share_privilege of this GroupShareProperties.  # noqa: E501
        :rtype: bool
        """
        return self._share_privilege

    @share_privilege.setter
    def share_privilege(self, share_privilege):
        """Sets the share_privilege of this GroupShareProperties.

        share privilege on a resource  # noqa: E501

        :param share_privilege: The share_privilege of this GroupShareProperties.  # noqa: E501
        :type share_privilege: bool
        """

        self._share_privilege = share_privilege
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
        if not isinstance(other, GroupShareProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupShareProperties):
            return True

        return self.to_dict() != other.to_dict()
