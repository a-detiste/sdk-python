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


class KubernetesNodePoolProperties(object):
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
        'datacenter_id': 'str',
        'node_count': 'int',
        'cpu_family': 'str',
        'cores_count': 'int',
        'ram_size': 'int',
        'availability_zone': 'str',
        'storage_type': 'str',
        'storage_size': 'int',
        'k8s_version': 'str',
        'maintenance_window': 'KubernetesMaintenanceWindow',
        'auto_scaling': 'KubernetesAutoScaling',
        'lans': 'list[KubernetesNodePoolLan]',
        'labels': 'dict(str, str)',
        'annotations': 'dict(str, str)',
        'public_ips': 'list[str]',
        'available_upgrade_versions': 'list[str]',
    }

    attribute_map = {
        'name': 'name',
        'datacenter_id': 'datacenterId',
        'node_count': 'nodeCount',
        'cpu_family': 'cpuFamily',
        'cores_count': 'coresCount',
        'ram_size': 'ramSize',
        'availability_zone': 'availabilityZone',
        'storage_type': 'storageType',
        'storage_size': 'storageSize',
        'k8s_version': 'k8sVersion',
        'maintenance_window': 'maintenanceWindow',
        'auto_scaling': 'autoScaling',
        'lans': 'lans',
        'labels': 'labels',
        'annotations': 'annotations',
        'public_ips': 'publicIps',
        'available_upgrade_versions': 'availableUpgradeVersions',
    }

    def __init__(self, name=None, datacenter_id=None, node_count=None, cpu_family=None, cores_count=None, ram_size=None, availability_zone=None, storage_type=None, storage_size=None, k8s_version=None, maintenance_window=None, auto_scaling=None, lans=None, labels=None, annotations=None, public_ips=None, available_upgrade_versions=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesNodePoolProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._datacenter_id = None
        self._node_count = None
        self._cpu_family = None
        self._cores_count = None
        self._ram_size = None
        self._availability_zone = None
        self._storage_type = None
        self._storage_size = None
        self._k8s_version = None
        self._maintenance_window = None
        self._auto_scaling = None
        self._lans = None
        self._labels = None
        self._annotations = None
        self._public_ips = None
        self._available_upgrade_versions = None
        self.discriminator = None

        self.name = name
        self.datacenter_id = datacenter_id
        self.node_count = node_count
        self.cpu_family = cpu_family
        self.cores_count = cores_count
        self.ram_size = ram_size
        self.availability_zone = availability_zone
        self.storage_type = storage_type
        self.storage_size = storage_size
        if k8s_version is not None:
            self.k8s_version = k8s_version
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        if auto_scaling is not None:
            self.auto_scaling = auto_scaling
        if lans is not None:
            self.lans = lans
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations
        if public_ips is not None:
            self.public_ips = public_ips
        if available_upgrade_versions is not None:
            self.available_upgrade_versions = available_upgrade_versions

    @property
    def name(self):
        """Gets the name of this KubernetesNodePoolProperties.  # noqa: E501

        A Kubernetes Node Pool Name. Valid Kubernetes Node Pool name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  # noqa: E501

        :return: The name of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KubernetesNodePoolProperties.

        A Kubernetes Node Pool Name. Valid Kubernetes Node Pool name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  # noqa: E501

        :param name: The name of this KubernetesNodePoolProperties.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def datacenter_id(self):
        """Gets the datacenter_id of this KubernetesNodePoolProperties.  # noqa: E501

        A valid uuid of the datacenter on which user has access  # noqa: E501

        :return: The datacenter_id of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_id

    @datacenter_id.setter
    def datacenter_id(self, datacenter_id):
        """Sets the datacenter_id of this KubernetesNodePoolProperties.

        A valid uuid of the datacenter on which user has access  # noqa: E501

        :param datacenter_id: The datacenter_id of this KubernetesNodePoolProperties.  # noqa: E501
        :type datacenter_id: str
        """
        if self.local_vars_configuration.client_side_validation and datacenter_id is None:  # noqa: E501
            raise ValueError("Invalid value for `datacenter_id`, must not be `None`")  # noqa: E501

        self._datacenter_id = datacenter_id

    @property
    def node_count(self):
        """Gets the node_count of this KubernetesNodePoolProperties.  # noqa: E501

        Number of nodes part of the Node Pool  # noqa: E501

        :return: The node_count of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this KubernetesNodePoolProperties.

        Number of nodes part of the Node Pool  # noqa: E501

        :param node_count: The node_count of this KubernetesNodePoolProperties.  # noqa: E501
        :type node_count: int
        """
        if self.local_vars_configuration.client_side_validation and node_count is None:  # noqa: E501
            raise ValueError("Invalid value for `node_count`, must not be `None`")  # noqa: E501

        self._node_count = node_count

    @property
    def cpu_family(self):
        """Gets the cpu_family of this KubernetesNodePoolProperties.  # noqa: E501

        A valid cpu family name  # noqa: E501

        :return: The cpu_family of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: str
        """
        return self._cpu_family

    @cpu_family.setter
    def cpu_family(self, cpu_family):
        """Sets the cpu_family of this KubernetesNodePoolProperties.

        A valid cpu family name  # noqa: E501

        :param cpu_family: The cpu_family of this KubernetesNodePoolProperties.  # noqa: E501
        :type cpu_family: str
        """
        if self.local_vars_configuration.client_side_validation and cpu_family is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu_family`, must not be `None`")  # noqa: E501

        self._cpu_family = cpu_family

    @property
    def cores_count(self):
        """Gets the cores_count of this KubernetesNodePoolProperties.  # noqa: E501

        Number of cores for node  # noqa: E501

        :return: The cores_count of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: int
        """
        return self._cores_count

    @cores_count.setter
    def cores_count(self, cores_count):
        """Sets the cores_count of this KubernetesNodePoolProperties.

        Number of cores for node  # noqa: E501

        :param cores_count: The cores_count of this KubernetesNodePoolProperties.  # noqa: E501
        :type cores_count: int
        """
        if self.local_vars_configuration.client_side_validation and cores_count is None:  # noqa: E501
            raise ValueError("Invalid value for `cores_count`, must not be `None`")  # noqa: E501

        self._cores_count = cores_count

    @property
    def ram_size(self):
        """Gets the ram_size of this KubernetesNodePoolProperties.  # noqa: E501

        RAM size for node, minimum size is 2048MB. Ram size must be set to multiple of 1024MB.  # noqa: E501

        :return: The ram_size of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: int
        """
        return self._ram_size

    @ram_size.setter
    def ram_size(self, ram_size):
        """Sets the ram_size of this KubernetesNodePoolProperties.

        RAM size for node, minimum size is 2048MB. Ram size must be set to multiple of 1024MB.  # noqa: E501

        :param ram_size: The ram_size of this KubernetesNodePoolProperties.  # noqa: E501
        :type ram_size: int
        """
        if self.local_vars_configuration.client_side_validation and ram_size is None:  # noqa: E501
            raise ValueError("Invalid value for `ram_size`, must not be `None`")  # noqa: E501

        self._ram_size = ram_size

    @property
    def availability_zone(self):
        """Gets the availability_zone of this KubernetesNodePoolProperties.  # noqa: E501

        The availability zone in which the target VM should exist  # noqa: E501

        :return: The availability_zone of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this KubernetesNodePoolProperties.

        The availability zone in which the target VM should exist  # noqa: E501

        :param availability_zone: The availability_zone of this KubernetesNodePoolProperties.  # noqa: E501
        :type availability_zone: str
        """
        if self.local_vars_configuration.client_side_validation and availability_zone is None:  # noqa: E501
            raise ValueError("Invalid value for `availability_zone`, must not be `None`")  # noqa: E501
        allowed_values = ["AUTO", "ZONE_1", "ZONE_2"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and availability_zone not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `availability_zone` ({0}), must be one of {1}"  # noqa: E501
                .format(availability_zone, allowed_values)
            )

        self._availability_zone = availability_zone

    @property
    def storage_type(self):
        """Gets the storage_type of this KubernetesNodePoolProperties.  # noqa: E501

        Hardware type of the volume  # noqa: E501

        :return: The storage_type of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this KubernetesNodePoolProperties.

        Hardware type of the volume  # noqa: E501

        :param storage_type: The storage_type of this KubernetesNodePoolProperties.  # noqa: E501
        :type storage_type: str
        """
        if self.local_vars_configuration.client_side_validation and storage_type is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_type`, must not be `None`")  # noqa: E501
        allowed_values = ["HDD", "SSD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and storage_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `storage_type` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_type, allowed_values)
            )

        self._storage_type = storage_type

    @property
    def storage_size(self):
        """Gets the storage_size of this KubernetesNodePoolProperties.  # noqa: E501

        The size of the volume in GB. The size should be greater than 10GB.  # noqa: E501

        :return: The storage_size of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """Sets the storage_size of this KubernetesNodePoolProperties.

        The size of the volume in GB. The size should be greater than 10GB.  # noqa: E501

        :param storage_size: The storage_size of this KubernetesNodePoolProperties.  # noqa: E501
        :type storage_size: int
        """
        if self.local_vars_configuration.client_side_validation and storage_size is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_size`, must not be `None`")  # noqa: E501

        self._storage_size = storage_size

    @property
    def k8s_version(self):
        """Gets the k8s_version of this KubernetesNodePoolProperties.  # noqa: E501

        The kubernetes version in which a nodepool is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions.  # noqa: E501

        :return: The k8s_version of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: str
        """
        return self._k8s_version

    @k8s_version.setter
    def k8s_version(self, k8s_version):
        """Sets the k8s_version of this KubernetesNodePoolProperties.

        The kubernetes version in which a nodepool is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions.  # noqa: E501

        :param k8s_version: The k8s_version of this KubernetesNodePoolProperties.  # noqa: E501
        :type k8s_version: str
        """

        self._k8s_version = k8s_version

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this KubernetesNodePoolProperties.  # noqa: E501


        :return: The maintenance_window of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: KubernetesMaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this KubernetesNodePoolProperties.


        :param maintenance_window: The maintenance_window of this KubernetesNodePoolProperties.  # noqa: E501
        :type maintenance_window: KubernetesMaintenanceWindow
        """

        self._maintenance_window = maintenance_window

    @property
    def auto_scaling(self):
        """Gets the auto_scaling of this KubernetesNodePoolProperties.  # noqa: E501


        :return: The auto_scaling of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: KubernetesAutoScaling
        """
        return self._auto_scaling

    @auto_scaling.setter
    def auto_scaling(self, auto_scaling):
        """Sets the auto_scaling of this KubernetesNodePoolProperties.


        :param auto_scaling: The auto_scaling of this KubernetesNodePoolProperties.  # noqa: E501
        :type auto_scaling: KubernetesAutoScaling
        """

        self._auto_scaling = auto_scaling

    @property
    def lans(self):
        """Gets the lans of this KubernetesNodePoolProperties.  # noqa: E501

        array of additional LANs attached to worker nodes  # noqa: E501

        :return: The lans of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: list[KubernetesNodePoolLan]
        """
        return self._lans

    @lans.setter
    def lans(self, lans):
        """Sets the lans of this KubernetesNodePoolProperties.

        array of additional LANs attached to worker nodes  # noqa: E501

        :param lans: The lans of this KubernetesNodePoolProperties.  # noqa: E501
        :type lans: list[KubernetesNodePoolLan]
        """

        self._lans = lans

    @property
    def labels(self):
        """Gets the labels of this KubernetesNodePoolProperties.  # noqa: E501

        map of labels attached to node pool  # noqa: E501

        :return: The labels of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this KubernetesNodePoolProperties.

        map of labels attached to node pool  # noqa: E501

        :param labels: The labels of this KubernetesNodePoolProperties.  # noqa: E501
        :type labels: dict(str, str)
        """

        self._labels = labels

    @property
    def annotations(self):
        """Gets the annotations of this KubernetesNodePoolProperties.  # noqa: E501

        map of annotations attached to node pool  # noqa: E501

        :return: The annotations of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this KubernetesNodePoolProperties.

        map of annotations attached to node pool  # noqa: E501

        :param annotations: The annotations of this KubernetesNodePoolProperties.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def public_ips(self):
        """Gets the public_ips of this KubernetesNodePoolProperties.  # noqa: E501

        Optional array of reserved public IP addresses to be used by the nodes. IPs must be from same location as the data center used for the node pool. The array must contain one extra IP than maximum number of nodes could be. (nodeCount+1 if fixed node amount or maxNodeCount+1 if auto scaling is used) The extra provided IP Will be used during rebuilding of nodes.  # noqa: E501

        :return: The public_ips of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        """Sets the public_ips of this KubernetesNodePoolProperties.

        Optional array of reserved public IP addresses to be used by the nodes. IPs must be from same location as the data center used for the node pool. The array must contain one extra IP than maximum number of nodes could be. (nodeCount+1 if fixed node amount or maxNodeCount+1 if auto scaling is used) The extra provided IP Will be used during rebuilding of nodes.  # noqa: E501

        :param public_ips: The public_ips of this KubernetesNodePoolProperties.  # noqa: E501
        :type public_ips: list[str]
        """

        self._public_ips = public_ips

    @property
    def available_upgrade_versions(self):
        """Gets the available_upgrade_versions of this KubernetesNodePoolProperties.  # noqa: E501

        List of available versions for upgrading the node pool  # noqa: E501

        :return: The available_upgrade_versions of this KubernetesNodePoolProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_upgrade_versions

    @available_upgrade_versions.setter
    def available_upgrade_versions(self, available_upgrade_versions):
        """Sets the available_upgrade_versions of this KubernetesNodePoolProperties.

        List of available versions for upgrading the node pool  # noqa: E501

        :param available_upgrade_versions: The available_upgrade_versions of this KubernetesNodePoolProperties.  # noqa: E501
        :type available_upgrade_versions: list[str]
        """

        self._available_upgrade_versions = available_upgrade_versions

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
        if not isinstance(other, KubernetesNodePoolProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesNodePoolProperties):
            return True

        return self.to_dict() != other.to_dict()
