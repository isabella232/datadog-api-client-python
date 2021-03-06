# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.process_summary_attributes import ProcessSummaryAttributes
from datadog_api_client.v2.model.process_summary_type import ProcessSummaryType
globals()['ProcessSummaryAttributes'] = ProcessSummaryAttributes
globals()['ProcessSummaryType'] = ProcessSummaryType
from datadog_api_client.v2.model.process_summary import ProcessSummary


class TestProcessSummary(unittest.TestCase):
    """ProcessSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProcessSummary(self):
        """Test ProcessSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProcessSummary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
