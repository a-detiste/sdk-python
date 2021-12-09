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


class KubernetesNodeMetadata(object):
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

        'etag': 'str',

        'created_date': 'datetime',

        'last_modified_date': 'datetime',

        'state': 'str',

        'last_software_updated_date': 'datetime',
    }

    attribute_map = {

        'etag': 'etag',

        'created_date': 'createdDate',

        'last_modified_date': 'lastModifiedDate',

        'state': 'state',

        'last_software_updated_date': 'lastSoftwareUpdatedDate',
    }

    def __init__(self, etag=None, created_date=None, last_modified_date=None, state=None, last_software_updated_date=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesNodeMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._etag = None
        self._created_date = None
        self._last_modified_date = None
        self._state = None
        self._last_software_updated_date = None
        self.discriminator = None

        if etag is not None:
            self.etag = etag
        if created_date is not None:
            self.created_date = created_date
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if state is not None:
            self.state = state
        if last_software_updated_date is not None:
            self.last_software_updated_date = last_software_updated_date


    @property
    def etag(self):
        """Gets the etag of this KubernetesNodeMetadata.  # noqa: E501

        Resource's Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an 'ETag response header to requests which don't use 'depth' parameter.   # noqa: E501

        :return: The etag of this KubernetesNodeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this KubernetesNodeMetadata.

        Resource's Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an 'ETag response header to requests which don't use 'depth' parameter.   # noqa: E501

        :param etag: The etag of this KubernetesNodeMetadata.  # noqa: E501
        :type etag: str
        """

        self._etag = etag

    @property
    def created_date(self):
        """Gets the created_date of this KubernetesNodeMetadata.  # noqa: E501

        The last time the resource was created.  # noqa: E501

        :return: The created_date of this KubernetesNodeMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this KubernetesNodeMetadata.

        The last time the resource was created.  # noqa: E501

        :param created_date: The created_date of this KubernetesNodeMetadata.  # noqa: E501
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this KubernetesNodeMetadata.  # noqa: E501

        The last time the resource was modified.  # noqa: E501

        :return: The last_modified_date of this KubernetesNodeMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this KubernetesNodeMetadata.

        The last time the resource was modified.  # noqa: E501

        :param last_modified_date: The last_modified_date of this KubernetesNodeMetadata.  # noqa: E501
        :type last_modified_date: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def state(self):
        """Gets the state of this KubernetesNodeMetadata.  # noqa: E501

        State of the resource.  # noqa: E501

        :return: The state of this KubernetesNodeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this KubernetesNodeMetadata.

        State of the resource.  # noqa: E501

        :param state: The state of this KubernetesNodeMetadata.  # noqa: E501
        :type state: str
        """
        allowed_values = ["PROVISIONING", "PROVISIONED", "READY", "TERMINATING", "REBUILDING", "BUSY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def last_software_updated_date(self):
        """Gets the last_software_updated_date of this KubernetesNodeMetadata.  # noqa: E501

        The last time the software was updated on the node.  # noqa: E501

        :return: The last_software_updated_date of this KubernetesNodeMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_software_updated_date

    @last_software_updated_date.setter
    def last_software_updated_date(self, last_software_updated_date):
        """Sets the last_software_updated_date of this KubernetesNodeMetadata.

        The last time the software was updated on the node.  # noqa: E501

        :param last_software_updated_date: The last_software_updated_date of this KubernetesNodeMetadata.  # noqa: E501
        :type last_software_updated_date: datetime
        """

        self._last_software_updated_date = last_software_updated_date
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
        if not isinstance(other, KubernetesNodeMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesNodeMetadata):
            return True

        return self.to_dict() != other.to_dict()
