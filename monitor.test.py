import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        self.assertFalse(vitals_ok(94, 90, 70))
        self.assertFalse(vitals_ok(104, 90, 70))
        self.assertFalse(vitals_ok(98.1, 70, 98))
        self.assertTrue(vitals_ok(95.2, 70, 50))
        self.assertTrue(vitals_ok(101, 70, 50))
        self.assertTrue(vitals_ok(99, 61, 50))
        self.assertTrue(vitals_ok(99, 99, 50))
        self.assertTrue(vitals_ok(99, 95, 1))
        self.assertTrue(vitals_ok(99, 95, 89))

if __name__ == '__main__':
  unittest.main()


