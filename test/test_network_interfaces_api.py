# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0-SDK.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ionoscloud
from ionoscloud.api.network_interfaces_api import NetworkInterfacesApi  # noqa: E501
from ionoscloud.rest import ApiException


class TestNetworkInterfacesApi(unittest.TestCase):
    """NetworkInterfacesApi unit test stubs"""

    def setUp(self):
        self.api = ionoscloud.api.network_interfaces_api.NetworkInterfacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_datacenters_servers_nics_delete(self):
        """Test case for datacenters_servers_nics_delete

        Delete a Network Interface  # noqa: E501
        """
        pass

    def test_datacenters_servers_nics_find_by_id(self):
        """Test case for datacenters_servers_nics_find_by_id

        Retrieve a Network Interface  # noqa: E501
        """
        pass

    def test_datacenters_servers_nics_get(self):
        """Test case for datacenters_servers_nics_get

        List Network Interfaces  # noqa: E501
        """
        pass

    def test_datacenters_servers_nics_patch(self):
        """Test case for datacenters_servers_nics_patch

        Partially Modify a Network Interface  # noqa: E501
        """
        pass

    def test_datacenters_servers_nics_post(self):
        """Test case for datacenters_servers_nics_post

        Create a Network Interface  # noqa: E501
        """
        pass

    def test_datacenters_servers_nics_put(self):
        """Test case for datacenters_servers_nics_put

        Modify a Network Interface  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
