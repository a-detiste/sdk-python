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


class RequestStatusMetadata(object):
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

        'status': 'str',

        'message': 'str',

        'etag': 'str',

        'targets': 'list[RequestTarget]',
    }

    attribute_map = {

        'status': 'status',

        'message': 'message',

        'etag': 'etag',

        'targets': 'targets',
    }

    def __init__(self, status=None, message=None, etag=None, targets=None, local_vars_configuration=None):  # noqa: E501
        """RequestStatusMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._message = None
        self._etag = None
        self._targets = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if etag is not None:
            self.etag = etag
        if targets is not None:
            self.targets = targets


    @property
    def status(self):
        """Gets the status of this RequestStatusMetadata.  # noqa: E501


        :return: The status of this RequestStatusMetadata.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RequestStatusMetadata.


        :param status: The status of this RequestStatusMetadata.  # noqa: E501
        :type status: str
        """
        allowed_values = ["QUEUED", "RUNNING", "DONE", "FAILED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this RequestStatusMetadata.  # noqa: E501


        :return: The message of this RequestStatusMetadata.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RequestStatusMetadata.


        :param message: The message of this RequestStatusMetadata.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def etag(self):
        """Gets the etag of this RequestStatusMetadata.  # noqa: E501

        Resource's Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an 'ETag response header to requests which don't use 'depth' parameter.   # noqa: E501

        :return: The etag of this RequestStatusMetadata.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this RequestStatusMetadata.

        Resource's Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11  Entity Tag is also added as an 'ETag response header to requests which don't use 'depth' parameter.   # noqa: E501

        :param etag: The etag of this RequestStatusMetadata.  # noqa: E501
        :type etag: str
        """

        self._etag = etag

    @property
    def targets(self):
        """Gets the targets of this RequestStatusMetadata.  # noqa: E501


        :return: The targets of this RequestStatusMetadata.  # noqa: E501
        :rtype: list[RequestTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this RequestStatusMetadata.


        :param targets: The targets of this RequestStatusMetadata.  # noqa: E501
        :type targets: list[RequestTarget]
        """

        self._targets = targets
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
        if not isinstance(other, RequestStatusMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestStatusMetadata):
            return True

        return self.to_dict() != other.to_dict()
