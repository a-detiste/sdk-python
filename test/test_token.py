# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionoscloud
from ionoscloud.models.token import Token  # noqa: E501
from ionoscloud.rest import ApiException

class TestToken(unittest.TestCase):
    """Token unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Token
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.token.Token()  # noqa: E501
        if include_optional :
            return Token(
                token = 'eyJ0eXAiOiJKV1QiLCJraWQiOiI0MWM1MDFlNC03NGY3LTQwYjctYmMxMi1lZWIzMTAzNThlZDkiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJpb25vc2Nsb3VkIiwiaWF0IjoxNjAyNDg5NTkzMDcxLCJzZXJ2ZXIiOnsidXVpZCI6IjMwNGEwZGVlLWE3OTgtNDNhNi04MzIyLTk3M2NiYzc3Yjg4ZCIsIm5hbWUiOiJTZXJ2ZXIifX0.TND9kJd8GXM39XP5PMH_LnF_99al4MEkI_eoEowPvPztirgM50aZEdg6SuLYQzg-R7vrA7hEFaK4NJb2BUUsIZYVMhjl1QmKUE5TnP0Q2zYnIfNQNZFDu2rKrOydPCkPQwlMVvvZLeBSz7lrKYujF-qZ_yY_6SHlFtt-rg6IznRtup8AFziXtl-9cEsWU92_GCTd5LiriQrsnFAiGRbb0p2_6OYAQAH9FeWu4cxrbSwUmeR7Q4klJyZqFd0fv6UTFBtpSiyci7rsB142MXyLcqM4PrBkgd9P5OFbJYf5lbsb9pW04wLSl9rqoWGgZvWsqpuzosUkQRZt_O5yuYmT9w'
            )
        else :
            return Token(
        )

    def testToken(self):
        """Test Token"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
