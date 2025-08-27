import unittest
from katas.github_user_fetcher import *
from unittest.mock import patch, Mock

class TestFetchGitHubUser(unittest.TestCase):
    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_user(self, mock_get):
        # Arrange
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = {
            'login': 'TameerAmer',
            'name': 'Tameer Amer',
            'public_repos': 5,
            'followers': 10
        }

        # Act
        user_info = fetch_github_user("TameerAmer")

        # Assert
        self.assertEqual(user_info['login'], 'TameerAmer')
        self.assertEqual(user_info['name'], 'Tameer Amer')
        self.assertEqual(user_info['followers'], 10)

        self.assertEqual(get_user_repositories_count("TameerAmer"), 5)


    def test_fetch_non_existing_user(self):
        self.assertEqual(fetch_github_user("non_existing_user!!!!!"), None)
        self.assertEqual(get_user_repositories_count("non_existing_user!!!!!"), 0)
        
