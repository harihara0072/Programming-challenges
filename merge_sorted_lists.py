import unittest


def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list

    if len(my_list) == 0:
        return alices_list
    elif len(alices_list) == 0:
        return my_list

    size_of_my_list = len(my_list)
    size_of_alices_list = len(alices_list)

    if size_of_my_list < size_of_alices_list:
        arr1, arr2 = my_list, alices_list
    else:
        arr1, arr2 = alices_list, my_list
    output = []

    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1
    if i == len(arr1):
        output = output + arr2[j::]
    else:
        output = output + arr1[i::]

    return output


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
