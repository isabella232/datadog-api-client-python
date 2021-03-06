# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import aws_account
except ImportError:
    aws_account = sys.modules[
        'datadog_api_client.v1.model.aws_account']
from datadog_api_client.v1.model.aws_account_list_response import AWSAccountListResponse


class TestAWSAccountListResponse(unittest.TestCase):
    """AWSAccountListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAWSAccountListResponse(self):
        """Test AWSAccountListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AWSAccountListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
