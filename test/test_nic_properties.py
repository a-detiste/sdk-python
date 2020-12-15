# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionoscloud
from ionoscloud.models.nic_properties import NicProperties  # noqa: E501
from ionoscloud.rest import ApiException

class TestNicProperties(unittest.TestCase):
    """NicProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NicProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.nic_properties.NicProperties()  # noqa: E501
        if include_optional :
            return NicProperties(
                name = 'My resource',
                mac = '00:0a:95:9d:68:16',
                ips = [
                    ''
                    ],
                dhcp = True,
                lan = 2,
                firewall_active = False,
                nat = True
            )
        else :
            return NicProperties(
                lan = 2,
        )

    def testNicProperties(self):
        """Test NicProperties"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
