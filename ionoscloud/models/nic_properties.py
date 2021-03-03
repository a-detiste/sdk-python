# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class NicProperties(object):
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
        'mac': 'str',
        'ips': 'list[str]',
        'dhcp': 'bool',
        'lan': 'int',
        'firewall_active': 'bool',
        'firewall_type': 'str',
        'device_number': 'int',
        'pci_slot': 'int',
    }

    attribute_map = {
        'name': 'name',
        'mac': 'mac',
        'ips': 'ips',
        'dhcp': 'dhcp',
        'lan': 'lan',
        'firewall_active': 'firewallActive',
        'firewall_type': 'firewallType',
        'device_number': 'deviceNumber',
        'pci_slot': 'pciSlot',
    }

    def __init__(self, name=None, mac=None, ips=None, dhcp=None, lan=None, firewall_active=None, firewall_type=None, device_number=None, pci_slot=None, local_vars_configuration=None):  # noqa: E501
        """NicProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._mac = None
        self._ips = None
        self._dhcp = None
        self._lan = None
        self._firewall_active = None
        self._firewall_type = None
        self._device_number = None
        self._pci_slot = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if mac is not None:
            self.mac = mac
        if ips is not None:
            self.ips = ips
        if dhcp is not None:
            self.dhcp = dhcp
        self.lan = lan
        if firewall_active is not None:
            self.firewall_active = firewall_active
        if firewall_type is not None:
            self.firewall_type = firewall_type
        if device_number is not None:
            self.device_number = device_number
        if pci_slot is not None:
            self.pci_slot = pci_slot

    @property
    def name(self):
        """Gets the name of this NicProperties.  # noqa: E501

        A name of that resource  # noqa: E501

        :return: The name of this NicProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NicProperties.

        A name of that resource  # noqa: E501

        :param name: The name of this NicProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def mac(self):
        """Gets the mac of this NicProperties.  # noqa: E501

        The MAC address of the NIC  # noqa: E501

        :return: The mac of this NicProperties.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this NicProperties.

        The MAC address of the NIC  # noqa: E501

        :param mac: The mac of this NicProperties.  # noqa: E501
        :type mac: str
        """

        self._mac = mac

    @property
    def ips(self):
        """Gets the ips of this NicProperties.  # noqa: E501

        Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.  # noqa: E501

        :return: The ips of this NicProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this NicProperties.

        Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.  # noqa: E501

        :param ips: The ips of this NicProperties.  # noqa: E501
        :type ips: list[str]
        """

        self._ips = ips

    @property
    def dhcp(self):
        """Gets the dhcp of this NicProperties.  # noqa: E501

        Indicates if the nic will reserve an IP using DHCP  # noqa: E501

        :return: The dhcp of this NicProperties.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """Sets the dhcp of this NicProperties.

        Indicates if the nic will reserve an IP using DHCP  # noqa: E501

        :param dhcp: The dhcp of this NicProperties.  # noqa: E501
        :type dhcp: bool
        """

        self._dhcp = dhcp

    @property
    def lan(self):
        """Gets the lan of this NicProperties.  # noqa: E501

        The LAN ID the NIC will sit on. If the LAN ID does not exist it will be implicitly created  # noqa: E501

        :return: The lan of this NicProperties.  # noqa: E501
        :rtype: int
        """
        return self._lan

    @lan.setter
    def lan(self, lan):
        """Sets the lan of this NicProperties.

        The LAN ID the NIC will sit on. If the LAN ID does not exist it will be implicitly created  # noqa: E501

        :param lan: The lan of this NicProperties.  # noqa: E501
        :type lan: int
        """
        if self.local_vars_configuration.client_side_validation and lan is None:  # noqa: E501
            raise ValueError("Invalid value for `lan`, must not be `None`")  # noqa: E501

        self._lan = lan

    @property
    def firewall_active(self):
        """Gets the firewall_active of this NicProperties.  # noqa: E501

        Activate or deactivate the firewall. By default an active firewall without any defined rules will block all incoming network traffic except for the firewall rules that explicitly allows certain protocols, ip addresses and ports.  # noqa: E501

        :return: The firewall_active of this NicProperties.  # noqa: E501
        :rtype: bool
        """
        return self._firewall_active

    @firewall_active.setter
    def firewall_active(self, firewall_active):
        """Sets the firewall_active of this NicProperties.

        Activate or deactivate the firewall. By default an active firewall without any defined rules will block all incoming network traffic except for the firewall rules that explicitly allows certain protocols, ip addresses and ports.  # noqa: E501

        :param firewall_active: The firewall_active of this NicProperties.  # noqa: E501
        :type firewall_active: bool
        """

        self._firewall_active = firewall_active

    @property
    def firewall_type(self):
        """Gets the firewall_type of this NicProperties.  # noqa: E501

        The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS  # noqa: E501

        :return: The firewall_type of this NicProperties.  # noqa: E501
        :rtype: str
        """
        return self._firewall_type

    @firewall_type.setter
    def firewall_type(self, firewall_type):
        """Sets the firewall_type of this NicProperties.

        The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS  # noqa: E501

        :param firewall_type: The firewall_type of this NicProperties.  # noqa: E501
        :type firewall_type: str
        """
        allowed_values = ["INGRESS", "EGRESS", "BIDIRECTIONAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and firewall_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `firewall_type` ({0}), must be one of {1}"  # noqa: E501
                .format(firewall_type, allowed_values)
            )

        self._firewall_type = firewall_type

    @property
    def device_number(self):
        """Gets the device_number of this NicProperties.  # noqa: E501

        The Logical Unit Number (LUN) of the storage volume. Null if this NIC was create from CloudAPI and no DCD changes were done on the Datacenter.  # noqa: E501

        :return: The device_number of this NicProperties.  # noqa: E501
        :rtype: int
        """
        return self._device_number

    @device_number.setter
    def device_number(self, device_number):
        """Sets the device_number of this NicProperties.

        The Logical Unit Number (LUN) of the storage volume. Null if this NIC was create from CloudAPI and no DCD changes were done on the Datacenter.  # noqa: E501

        :param device_number: The device_number of this NicProperties.  # noqa: E501
        :type device_number: int
        """

        self._device_number = device_number

    @property
    def pci_slot(self):
        """Gets the pci_slot of this NicProperties.  # noqa: E501

        The PCI slot number of the Nic.  # noqa: E501

        :return: The pci_slot of this NicProperties.  # noqa: E501
        :rtype: int
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """Sets the pci_slot of this NicProperties.

        The PCI slot number of the Nic.  # noqa: E501

        :param pci_slot: The pci_slot of this NicProperties.  # noqa: E501
        :type pci_slot: int
        """

        self._pci_slot = pci_slot

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
        if not isinstance(other, NicProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NicProperties):
            return True

        return self.to_dict() != other.to_dict()
