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

import ionos_cloud_sdk_python
from ionos_cloud_sdk_python.models.kubernetes_maintenance_window import KubernetesMaintenanceWindow  # noqa: E501
from ionos_cloud_sdk_python.rest import ApiException

class TestKubernetesMaintenanceWindow(unittest.TestCase):
    """KubernetesMaintenanceWindow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubernetesMaintenanceWindow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionos_cloud_sdk_python.models.kubernetes_maintenance_window.KubernetesMaintenanceWindow()  # noqa: E501
        if include_optional :
            return KubernetesMaintenanceWindow(
                day_of_the_week = 'Monday', 
                time = '13:00:00'
            )
        else :
            return KubernetesMaintenanceWindow(
        )

    def testKubernetesMaintenanceWindow(self):
        """Test KubernetesMaintenanceWindow"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
