#!/usr/bin/env python3
"""
Testing the client GithubOrgClient classes
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """method to test GithubOrgClient.org"""
        test_client = GithubOrgClient(org_name)
        response = test_client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, {"payload": True})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """method to test GithubOrgClient._public_repos_url"""
        payload = {"repos_url": "https://api.github.com/orgs/octocat/repos"}
        mock_org.return_value = payload

        test_client = GithubOrgClient("octocat")
        result = test_client._public_repos_url

        self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json', return_value=[{"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json):
        """method to test GithubOrgClient.public_repos"""
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/octocat/repos"
            test_client = GithubOrgClient("octocat")
            repos = test_client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
