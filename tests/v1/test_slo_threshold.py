# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import slo_timeframe
except ImportError:
    slo_timeframe = sys.modules[
        'datadog_api_client.v1.model.slo_timeframe']
from datadog_api_client.v1.model.slo_threshold import SLOThreshold


class TestSLOThreshold(unittest.TestCase):
    """SLOThreshold unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOThreshold(self):
        """Test SLOThreshold"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOThreshold()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
