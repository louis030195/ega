"""
    API Reference

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import timingapp
from timingapp.api.teams_api import TeamsApi  # noqa: E501


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_teams_get(self):
        """Test case for api_v1_teams_get

        Return a list containing all the teams you are a member of.  # noqa: E501
        """
        pass

    def test_api_v1_teams_team_id_members_get(self):
        """Test case for api_v1_teams_team_id_members_get

        Return a list containing all active members of the given team.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
