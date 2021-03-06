# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import logs_archive_destination_gcs_type
except ImportError:
    logs_archive_destination_gcs_type = sys.modules[
        'datadog_api_client.v2.model.logs_archive_destination_gcs_type']
try:
    from datadog_api_client.v2.model import logs_archive_integration_gcs
except ImportError:
    logs_archive_integration_gcs = sys.modules[
        'datadog_api_client.v2.model.logs_archive_integration_gcs']
from datadog_api_client.v2.model.logs_archive_destination_gcs import LogsArchiveDestinationGCS


class TestLogsArchiveDestinationGCS(unittest.TestCase):
    """LogsArchiveDestinationGCS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsArchiveDestinationGCS(self):
        """Test LogsArchiveDestinationGCS"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsArchiveDestinationGCS()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
