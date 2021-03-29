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


class RequestMetadata(object):
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
        'created_date': 'datetime',
        'created_by': 'str',
        'etag': 'str',
        'request_status': 'RequestStatus',
    }

    attribute_map = {
        'created_date': 'createdDate',
        'created_by': 'createdBy',
        'etag': 'etag',
        'request_status': 'requestStatus',
    }

    def __init__(self, created_date=None, created_by=None, etag=None, request_status=None, local_vars_configuration=None):  # noqa: E501
        """RequestMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_date = None
        self._created_by = None
        self._etag = None
        self._request_status = None
        self.discriminator = None

        if created_date is not None:
            self.created_date = created_date
        if created_by is not None:
            self.created_by = created_by
        if etag is not None:
            self.etag = etag
        if request_status is not None:
            self.request_status = request_status

    @property
    def created_date(self):
        """Gets the created_date of this RequestMetadata.  # noqa: E501

        The last time the resource was created  # noqa: E501

        :return: The created_date of this RequestMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this RequestMetadata.

        The last time the resource was created  # noqa: E501

        :param created_date: The created_date of this RequestMetadata.  # noqa: E501
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def created_by(self):
        """Gets the created_by of this RequestMetadata.  # noqa: E501

        The user who created the resource.  # noqa: E501

        :return: The created_by of this RequestMetadata.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RequestMetadata.

        The user who created the resource.  # noqa: E501

        :param created_by: The created_by of this RequestMetadata.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def etag(self):
        """Gets the etag of this RequestMetadata.  # noqa: E501

        Resource's Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11 . Entity Tag is also added as an 'ETag response header to requests which don't use 'depth' parameter.   # noqa: E501

        :return: The etag of this RequestMetadata.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this RequestMetadata.

        Resource's Entity Tag as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11 . Entity Tag is also added as an 'ETag response header to requests which don't use 'depth' parameter.   # noqa: E501

        :param etag: The etag of this RequestMetadata.  # noqa: E501
        :type etag: str
        """

        self._etag = etag

    @property
    def request_status(self):
        """Gets the request_status of this RequestMetadata.  # noqa: E501


        :return: The request_status of this RequestMetadata.  # noqa: E501
        :rtype: RequestStatus
        """
        return self._request_status

    @request_status.setter
    def request_status(self, request_status):
        """Sets the request_status of this RequestMetadata.


        :param request_status: The request_status of this RequestMetadata.  # noqa: E501
        :type request_status: RequestStatus
        """

        self._request_status = request_status

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
        if not isinstance(other, RequestMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestMetadata):
            return True

        return self.to_dict() != other.to_dict()
