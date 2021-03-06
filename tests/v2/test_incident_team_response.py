# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_team_included_items import IncidentTeamIncludedItems
from datadog_api_client.v2.model.incident_team_response_data import IncidentTeamResponseData
globals()['IncidentTeamIncludedItems'] = IncidentTeamIncludedItems
globals()['IncidentTeamResponseData'] = IncidentTeamResponseData
from datadog_api_client.v2.model.incident_team_response import IncidentTeamResponse


class TestIncidentTeamResponse(unittest.TestCase):
    """IncidentTeamResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentTeamResponse(self):
        """Test IncidentTeamResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentTeamResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
