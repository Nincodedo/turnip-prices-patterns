import unittest

from analyze import AnalyzeTurnips


class MyTestCase(unittest.TestCase):
    def test_is_decreasing(self):
        analyze = AnalyzeTurnips()
        week = [10, 8, 5]
        is_decrease = analyze.get_algorithm_for_week(week)
        self.assertTrue(is_decrease == "decreasing")


if __name__ == '__main__':
    unittest.main()
