import unittest
from unittest.mock import patch, Mock
from katas.pinger import ping_host

class TestPinger(unittest.TestCase):

    @patch('katas.pinger.subprocess.run')
    def test_ping_minimal_mock(self, mock_run):
        mock_proc = Mock()
        mock_proc.stdout = "rtt min/avg/max/mdev = 14.000/16.456/20.000/1.000 ms\n"
        mock_proc.returncode = 0
        mock_run.return_value = mock_proc

        result = ping_host("8.8.8.8", 3)

        self.assertEqual(result['host'], "8.8.8.8")
        self.assertAlmostEqual(result['avg_response_time_ms'], 16.456)
        self.assertTrue(result['success'])

