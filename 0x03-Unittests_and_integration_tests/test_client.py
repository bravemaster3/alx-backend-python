#!/usr/bin/env python3
"""
Testing the client GithubOrgClient classes
"""

from fixtures import TEST_PAYLOAD
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
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

    @patch('client.get_json', return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    def test_public_repos(self, mock_get_json):
        """method to test GithubOrgClient.public_repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            str1 = "https://api.github.com/"
            str2 = "orgs/octocat/repos"
            mock_public_repos_url.return_value = str1 + str2
            test_client = GithubOrgClient("octocat")
            repos = test_client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()


class TestGithubOrgClient(unittest.TestCase):
    """Class definition"""
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """method to test GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0], "repos_payload": TEST_PAYLOAD[0][1]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public repos"""
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload,
            self.org_payload, self.repos_payload
        ]

        test_client = GithubOrgClient("google")
        public_repos = test_client.public_repos()

        expected_repos = [repo['name'] for repo in self.repos_payload]
        self.assertEqual(public_repos, expected_repos)
        self.mock_get.assert_called()
