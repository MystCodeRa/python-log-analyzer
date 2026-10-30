
import unittest
from log_analyzer import analyze_logs


class TestLogAnalyzer(unittest.TestCase):

    # Test the total number of log events
    def test_total_events(self):
        results = analyze_logs("sample.log")
        self.assertEqual(results["total_events"], 10)

    # Test successful login detection
    def test_successful_logins(self):
        results = analyze_logs("sample.log")
        self.assertEqual(results["successful_logins"], 3)

    # Test failed login detection
    def test_failed_logins(self):
        results = analyze_logs("sample.log")
        self.assertEqual(results["failed_logins"], 5)

    # Test unauthorized access detection
    def test_unauthorized_access(self):
        results = analyze_logs("sample.log")
        self.assertEqual(results["unauthorized_access"], 2)

    # Test failed login attempts by IP address
    def test_failed_ip_count(self):
        results = analyze_logs("sample.log")
        self.assertEqual(results["failed_ips"]["192.168.1.15"], 3)


if __name__ == "__main__":
    unittest.main()

