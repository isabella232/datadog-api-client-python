# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import usage_specified_custom_reports_page
except ImportError:
    usage_specified_custom_reports_page = sys.modules[
        'datadog_api_client.v1.model.usage_specified_custom_reports_page']
from datadog_api_client.v1.model.usage_specified_custom_reports_meta import UsageSpecifiedCustomReportsMeta


class TestUsageSpecifiedCustomReportsMeta(unittest.TestCase):
    """UsageSpecifiedCustomReportsMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageSpecifiedCustomReportsMeta(self):
        """Test UsageSpecifiedCustomReportsMeta"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageSpecifiedCustomReportsMeta()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
