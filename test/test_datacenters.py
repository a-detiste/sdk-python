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
from ionoscloud.models.datacenters import Datacenters  # noqa: E501
from ionoscloud.rest import ApiException

class TestDatacenters(unittest.TestCase):
    """Datacenters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Datacenters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.datacenters.Datacenters()  # noqa: E501
        if include_optional :
            return Datacenters(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = "collection",
                href = '<RESOURCE-URI>',
                items = [
                    ionoscloud.models.datacenter.Datacenter(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "datacenter", 
                        href = '<RESOURCE-URI>', 
                        metadata = ionoscloud.models.datacenter_element_metadata.DatacenterElementMetadata(
                            etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                            created_date = '2015-12-04T14:34:09.809Z', 
                            created_by = 'user@example.com', 
                            created_by_user_id = 'user@example.com', 
                            last_modified_date = '2015-12-04T14:34:09.809Z', 
                            last_modified_by = 'user@example.com', 
                            last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                            state = 'AVAILABLE', ), 
                        properties = ionoscloud.models.datacenter_properties.DatacenterProperties(
                            name = 'My resource', 
                            description = 'My Production Datacenter', 
                            location = 'us/las', 
                            version = 8, 
                            features = [SSD], 
                            sec_auth_protection = True, ), 
                        entities = ionoscloud.models.data_center_entities.DataCenterEntities(
                            servers = ionoscloud.models.servers.Servers(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = '<RESOURCE-URI>', 
                                items = [
                                    ionoscloud.models.server.Server(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = "server", 
                                        href = '<RESOURCE-URI>', 
                                        properties = ionoscloud.models.server_properties.ServerProperties(
                                            name = 'My resource', 
                                            cores = 4, 
                                            ram = 4096, 
                                            availability_zone = 'AUTO', 
                                            vm_state = 'RUNNING', 
                                            boot_cdrom = ionoscloud.models.resource_reference.ResourceReference(
                                                id = '', 
                                                type = "resource", 
                                                href = '<RESOURCE-URI>', ), 
                                            boot_volume = ionoscloud.models.resource_reference.ResourceReference(
                                                id = '', 
                                                type = "resource", 
                                                href = '<RESOURCE-URI>', ), 
                                            cpu_family = 'AMD_OPTERON', ), )
                                    ], 
                                offset = 0, 
                                limit = 1000, 
                                _links = ionoscloud.models.pagination_links.PaginationLinks(
                                    prev = '<PREVIOUS-PAGE-URI>', 
                                    self = '<THIS-PAGE-URI>', 
                                    next = '<NEXT-PAGE-URI>', ), ), 
                            volumes = ionoscloud.models.volumes.Volumes(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = '<RESOURCE-URI>', ), 
                            loadbalancers = ionoscloud.models.loadbalancers.Loadbalancers(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = '<RESOURCE-URI>', ), 
                            lans = ionoscloud.models.lans.Lans(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = '<RESOURCE-URI>', ), ), )
                    ],
                offset = 0,
                limit = 1000,
                links = ionoscloud.models.pagination_links.PaginationLinks(
                    prev = '<PREVIOUS-PAGE-URI>', 
                    self = '<THIS-PAGE-URI>', 
                    next = '<NEXT-PAGE-URI>', )
            )
        else :
            return Datacenters(
        )

    def testDatacenters(self):
        """Test Datacenters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
