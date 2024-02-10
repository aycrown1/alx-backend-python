#!/usr/bin/env python3
"""
module to the test client.GithubOrgClient class
"""
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    implement the test_org method
    """

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """test that GithubOrgClient.org returns the correct value.
        """
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, {"payload": True})
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org) -> None:
        """
        unit-test GithubOrgClient._public_repos_url"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = payload
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client._public_repos_url,
                         payload["repos_url"])
