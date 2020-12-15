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
from ionoscloud.models.backup_unit_properties import BackupUnitProperties  # noqa: E501
from ionoscloud.rest import ApiException

class TestBackupUnitProperties(unittest.TestCase):
    """BackupUnitProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BackupUnitProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.backup_unit_properties.BackupUnitProperties()  # noqa: E501
        if include_optional :
            return BackupUnitProperties(
                name = 'BackupUnitName',
                password = 'mypass123',
                email = 'email@email.com'
            )
        else :
            return BackupUnitProperties(
                name = 'BackupUnitName',
        )

    def testBackupUnitProperties(self):
        """Test BackupUnitProperties"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
