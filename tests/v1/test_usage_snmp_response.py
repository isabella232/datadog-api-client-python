# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import usage_snmp_hour
except ImportError:
    usage_snmp_hour = sys.modules[
        'datadog_api_client.v1.model.usage_snmp_hour']
from datadog_api_client.v1.model.usage_snmp_response import UsageSNMPResponse


class TestUsageSNMPResponse(unittest.TestCase):
    """UsageSNMPResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageSNMPResponse(self):
        """Test UsageSNMPResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageSNMPResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()