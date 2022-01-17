
import unittest

PASS = "pass"
FAIL = "fail"
PWD = "pass with distinction"
INVALID_INPUT = "invalid input"


def result(scores: int) -> str:
    """The inputs to the program are exam scores expressed as percentages"""
    print(scores)
    result = "invalid input"
    in_range = scores in range(101)
    is_int = isinstance(scores, int)
    if not (is_int and in_range):
        return result
    if scores in range(46):
        result = FAIL
    elif scores in range(45, 81):
        result = PASS
    elif scores in range(81, 101):
        result = PWD
    return result


class TestExamResults(unittest.TestCase):

    def test_fail(self):
        self.assertEqual(result(40), FAIL)

    def test_pass(self):
        self.assertEqual(result(60), PASS)

    def test_pass_with_distinction(self):
        self.assertEqual(result(90), PWD)

    def test_invalid_input_int(self):
        self.assertEqual(result(110), INVALID_INPUT)

    def test_invalid_input_typr(self):
        self.assertEqual(result('110'), INVALID_INPUT)


if __name__ == '__main__':
    unittest.main()