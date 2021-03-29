# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0-SDK.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionoscloud
from ionoscloud.models.nat_gateway import NatGateway  # noqa: E501
from ionoscloud.rest import ApiException

class TestNatGateway(unittest.TestCase):
    """NatGateway unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NatGateway
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.nat_gateway.NatGateway()  # noqa: E501
        if include_optional :
            return NatGateway(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = "nat-gateway",
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
                properties = ionoscloud.models.nat_gateway_properties.NatGatewayProperties(
                    name = 'My NAT Gateway', 
                    public_ips = [81.173.1.2, 82.231.2.5, 92.221.2.4], 
                    lans = [
                        ionoscloud.models.nat_gateway_lan_properties.NatGatewayLanProperties(
                            id = 3, 
                            gateway_ips = [10.12.1.2/24, 10.11.2.5/24, 10.11.2.4], )
                        ], ),
                entities = ionoscloud.models.nat_gateway_entities.NatGatewayEntities(
                    rules = ionoscloud.models.nat_gateway_rules.NatGatewayRules(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "collection", 
                        href = '<RESOURCE-URI>', 
                        items = [
                            ionoscloud.models.nat_gateway_rule.NatGatewayRule(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "nat-gateway-rule", 
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
                                properties = ionoscloud.models.nat_gateway_rule_properties.NatGatewayRuleProperties(
                                    name = 'My NAT Gateway Rule', 
                                    type = "SNAT", 
                                    protocol = "TCP", 
                                    source_subnet = '10.0.1.0/24', 
                                    public_ip = '192.18.7.17', 
                                    target_subnet = '10.0.1.0/24', 
                                    target_port_range = ionoscloud.models.target_port_range.TargetPortRange(
                                        start = 10000, 
                                        end = 20000, ), ), )
                            ], ), 
                    flowlogs = ionoscloud.models.flow_logs.FlowLogs(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "collection", 
                        href = '<RESOURCE-URI>', 
                        offset = 0, 
                        limit = 1000, 
                        _links = ionoscloud.models.pagination_links.PaginationLinks(
                            prev = '<PREVIOUS-PAGE-URI>', 
                            self = '<THIS-PAGE-URI>', 
                            next = '<NEXT-PAGE-URI>', ), ), )
            )
        else :
            return NatGateway(
                properties = ionoscloud.models.nat_gateway_properties.NatGatewayProperties(
                    name = 'My NAT Gateway', 
                    public_ips = [81.173.1.2, 82.231.2.5, 92.221.2.4], 
                    lans = [
                        ionoscloud.models.nat_gateway_lan_properties.NatGatewayLanProperties(
                            id = 3, 
                            gateway_ips = [10.12.1.2/24, 10.11.2.5/24, 10.11.2.4], )
                        ], ),
        )

    def testNatGateway(self):
        """Test NatGateway"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
