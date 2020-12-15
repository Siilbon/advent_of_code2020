import pytest
from p1_solution import find_sum_pair


def test_find_sum_pair():
    assert find_sum_pair(numbers=[1721, 979, 366, 299, 675, 1456],
                         target_sum=2020) == (1721, 299)
