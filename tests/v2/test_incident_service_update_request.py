# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_service_update_data import IncidentServiceUpdateData
globals()['IncidentServiceUpdateData'] = IncidentServiceUpdateData
from datadog_api_client.v2.model.incident_service_update_request import IncidentServiceUpdateRequest


class TestIncidentServiceUpdateRequest(unittest.TestCase):
    """IncidentServiceUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentServiceUpdateRequest(self):
        """Test IncidentServiceUpdateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentServiceUpdateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
