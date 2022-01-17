"""Exam Scores"""
import unittest

PASS = "pass"
FAIL = "fail"
PWD = "pass with distinction"
INVALID_INPUT = "invalid input"


def result(scores: int) -> str:
    """The inputs to the program are exam scores expressed as percentages"""
    print(scores)
    results = "invalid input"
    in_range = scores in range(101)
    is_int = isinstance(scores, int)
    if not (is_int and in_range):
        return results
    if scores in range(46):
        results = FAIL
    elif scores in range(45, 81):
        results = PASS
    elif scores in range(81, 101):
        results = PWD
    return results


class TestExamResults(unittest.TestCase):
    """Check Results"""
    def test_fail(self):
        """Check Fail input"""
        self.assertEqual(result(40), FAIL)

    def test_pass(self):
        """Check Pass input"""
        self.assertEqual(result(60), PASS)

    def test_pass_with_distinction(self):
        """Check Pass with distinction input"""
        self.assertEqual(result(90), PWD)

    def test_invalid_input_int(self):
        """Check Invalid input"""
        self.assertEqual(result(110), INVALID_INPUT)

    def test_invalid_input_typr(self):
        """Check Invalid input"""
        self.assertEqual(result('110'), INVALID_INPUT)


if __name__ == '__main__':
    unittest.main()
