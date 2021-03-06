# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import user
except ImportError:
    user = sys.modules[
        'datadog_api_client.v2.model.user']
try:
    from datadog_api_client.v2.model import user_response_included_item
except ImportError:
    user_response_included_item = sys.modules[
        'datadog_api_client.v2.model.user_response_included_item']
from datadog_api_client.v2.model.user_response import UserResponse


class TestUserResponse(unittest.TestCase):
    """UserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserResponse(self):
        """Test UserResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
