import unittest


def sort_scores(unsorted_scores, highest_possible_score):
    # Sort the scores in O(n) time
    all_scores = [0] * (highest_possible_score + 1)
    for i in unsorted_scores:
        all_scores[i + 1] += i

    output = []
    for i in range(len(all_scores), -1,  -1):
        if all_scores[i-1] != 0:
            output += (all_scores[i-1]//(i-2)) * [i-2]

    return output


# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)

