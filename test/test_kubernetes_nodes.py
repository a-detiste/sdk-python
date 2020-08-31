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
from ionos_cloud_sdk_python.models.kubernetes_nodes import KubernetesNodes  # noqa: E501
from ionos_cloud_sdk_python.rest import ApiException

class TestKubernetesNodes(unittest.TestCase):
    """KubernetesNodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubernetesNodes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionos_cloud_sdk_python.models.kubernetes_nodes.KubernetesNodes()  # noqa: E501
        if include_optional :
            return KubernetesNodes(
                id = '1e072e52-2ed3-492f-b6b6-c6b116907527/nodepools', 
                type = 'collection', 
                href = '<RESOURCE-URI>', 
                items = [
                    ionos_cloud_sdk_python.models.kubernetes_node.KubernetesNode(
                        id = '1e072e52-2ed3-492f-b6b6-c6b116907527', 
                        type = 'nodepool', 
                        href = '<RESOURCE-URI>', 
                        metadata = ionos_cloud_sdk_python.models.kubernetes_node_metadata.KubernetesNodeMetadata(
                            etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                            created_date = '2015-12-04T14:34:09.809Z', 
                            last_modified_date = '2015-12-04T14:34:09.809Z', 
                            state = 'AVAILABLE', 
                            last_software_updated_date = '2015-12-04T14:34:09.809Z', ), 
                        properties = ionos_cloud_sdk_python.models.kubernetes_node_properties.KubernetesNodeProperties(
                            name = 'k8s-node', 
                            public_ip = '192.168.23.2', 
                            k8s_version = '1.15.4', ), )
                    ]
            )
        else :
            return KubernetesNodes(
        )

    def testKubernetesNodes(self):
        """Test KubernetesNodes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
