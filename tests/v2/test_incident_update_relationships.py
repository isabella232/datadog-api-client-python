# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.relationship_to_incident_integration_metadatas import RelationshipToIncidentIntegrationMetadatas
from datadog_api_client.v2.model.relationship_to_incident_postmortem import RelationshipToIncidentPostmortem
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
globals()['RelationshipToIncidentIntegrationMetadatas'] = RelationshipToIncidentIntegrationMetadatas
globals()['RelationshipToIncidentPostmortem'] = RelationshipToIncidentPostmortem
globals()['RelationshipToUser'] = RelationshipToUser
from datadog_api_client.v2.model.incident_update_relationships import IncidentUpdateRelationships


class TestIncidentUpdateRelationships(unittest.TestCase):
    """IncidentUpdateRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentUpdateRelationships(self):
        """Test IncidentUpdateRelationships"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentUpdateRelationships()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
