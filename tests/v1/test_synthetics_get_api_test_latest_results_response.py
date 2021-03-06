# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_api_test_result_short
except ImportError:
    synthetics_api_test_result_short = sys.modules[
        'datadog_api_client.v1.model.synthetics_api_test_result_short']
from datadog_api_client.v1.model.synthetics_get_api_test_latest_results_response import SyntheticsGetAPITestLatestResultsResponse


class TestSyntheticsGetAPITestLatestResultsResponse(unittest.TestCase):
    """SyntheticsGetAPITestLatestResultsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsGetAPITestLatestResultsResponse(self):
        """Test SyntheticsGetAPITestLatestResultsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsGetAPITestLatestResultsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
