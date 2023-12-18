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


class DatacenterProperties(object):
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

        'cpu_architecture': 'list[CpuArchitectureProperties]',

        'description': 'str',

        'features': 'list[str]',

        'ipv6_cidr_block': 'str',

        'location': 'str',

        'name': 'str',

        'sec_auth_protection': 'bool',

        'version': 'int',
    }

    attribute_map = {

        'cpu_architecture': 'cpuArchitecture',

        'description': 'description',

        'features': 'features',

        'ipv6_cidr_block': 'ipv6CidrBlock',

        'location': 'location',

        'name': 'name',

        'sec_auth_protection': 'secAuthProtection',

        'version': 'version',
    }

    def __init__(self, cpu_architecture=None, description=None, features=None, ipv6_cidr_block=None, location=None, name=None, sec_auth_protection=None, version=None, local_vars_configuration=None):  # noqa: E501
        """DatacenterProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu_architecture = None
        self._description = None
        self._features = None
        self._ipv6_cidr_block = None
        self._location = None
        self._name = None
        self._sec_auth_protection = None
        self._version = None
        self.discriminator = None

        if cpu_architecture is not None:
            self.cpu_architecture = cpu_architecture
        if description is not None:
            self.description = description
        if features is not None:
            self.features = features
        self.ipv6_cidr_block = ipv6_cidr_block
        self.location = location
        if name is not None:
            self.name = name
        if sec_auth_protection is not None:
            self.sec_auth_protection = sec_auth_protection
        if version is not None:
            self.version = version


    @property
    def cpu_architecture(self):
        """Gets the cpu_architecture of this DatacenterProperties.  # noqa: E501

        Array of features and CPU families available in a location  # noqa: E501

        :return: The cpu_architecture of this DatacenterProperties.  # noqa: E501
        :rtype: list[CpuArchitectureProperties]
        """
        return self._cpu_architecture

    @cpu_architecture.setter
    def cpu_architecture(self, cpu_architecture):
        """Sets the cpu_architecture of this DatacenterProperties.

        Array of features and CPU families available in a location  # noqa: E501

        :param cpu_architecture: The cpu_architecture of this DatacenterProperties.  # noqa: E501
        :type cpu_architecture: list[CpuArchitectureProperties]
        """

        self._cpu_architecture = cpu_architecture

    @property
    def description(self):
        """Gets the description of this DatacenterProperties.  # noqa: E501

        A description for the datacenter, such as staging, production.  # noqa: E501

        :return: The description of this DatacenterProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatacenterProperties.

        A description for the datacenter, such as staging, production.  # noqa: E501

        :param description: The description of this DatacenterProperties.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def features(self):
        """Gets the features of this DatacenterProperties.  # noqa: E501

        List of features supported by the location where this data center is provisioned.  # noqa: E501

        :return: The features of this DatacenterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this DatacenterProperties.

        List of features supported by the location where this data center is provisioned.  # noqa: E501

        :param features: The features of this DatacenterProperties.  # noqa: E501
        :type features: list[str]
        """

        self._features = features

    @property
    def ipv6_cidr_block(self):
        """Gets the ipv6_cidr_block of this DatacenterProperties.  # noqa: E501

        This value is either 'null' or contains an automatically-assigned /56 IPv6 CIDR block if IPv6 is enabled on this virtual data center. It can neither be changed nor removed.  # noqa: E501

        :return: The ipv6_cidr_block of this DatacenterProperties.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """Sets the ipv6_cidr_block of this DatacenterProperties.

        This value is either 'null' or contains an automatically-assigned /56 IPv6 CIDR block if IPv6 is enabled on this virtual data center. It can neither be changed nor removed.  # noqa: E501

        :param ipv6_cidr_block: The ipv6_cidr_block of this DatacenterProperties.  # noqa: E501
        :type ipv6_cidr_block: str
        """

        self._ipv6_cidr_block = ipv6_cidr_block

    @property
    def location(self):
        """Gets the location of this DatacenterProperties.  # noqa: E501

        The physical location where the datacenter will be created. This will be where all of your servers live. Property cannot be modified after datacenter creation (disallowed in update requests).  # noqa: E501

        :return: The location of this DatacenterProperties.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DatacenterProperties.

        The physical location where the datacenter will be created. This will be where all of your servers live. Property cannot be modified after datacenter creation (disallowed in update requests).  # noqa: E501

        :param location: The location of this DatacenterProperties.  # noqa: E501
        :type location: str
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def name(self):
        """Gets the name of this DatacenterProperties.  # noqa: E501

        The name of the  resource.  # noqa: E501

        :return: The name of this DatacenterProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatacenterProperties.

        The name of the  resource.  # noqa: E501

        :param name: The name of this DatacenterProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def sec_auth_protection(self):
        """Gets the sec_auth_protection of this DatacenterProperties.  # noqa: E501

        Boolean value representing if the data center requires extra protection, such as two-step verification.  # noqa: E501

        :return: The sec_auth_protection of this DatacenterProperties.  # noqa: E501
        :rtype: bool
        """
        return self._sec_auth_protection

    @sec_auth_protection.setter
    def sec_auth_protection(self, sec_auth_protection):
        """Sets the sec_auth_protection of this DatacenterProperties.

        Boolean value representing if the data center requires extra protection, such as two-step verification.  # noqa: E501

        :param sec_auth_protection: The sec_auth_protection of this DatacenterProperties.  # noqa: E501
        :type sec_auth_protection: bool
        """

        self._sec_auth_protection = sec_auth_protection

    @property
    def version(self):
        """Gets the version of this DatacenterProperties.  # noqa: E501

        The version of the data center; incremented with every change.  # noqa: E501

        :return: The version of this DatacenterProperties.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DatacenterProperties.

        The version of the data center; incremented with every change.  # noqa: E501

        :param version: The version of this DatacenterProperties.  # noqa: E501
        :type version: int
        """

        self._version = version
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
        if not isinstance(other, DatacenterProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatacenterProperties):
            return True

        return self.to_dict() != other.to_dict()
