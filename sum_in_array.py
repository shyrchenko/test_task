# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
from typing import List, Tuple, Union


def find_sum_components(sorted_array: List[int], s: int) -> Union[Tuple[int, int], int]:
    i = len(sorted_array) - 1
    while i >= 0:
        if sorted_array[i] > s:
            i -= 1
            continue

        j = 0
        while j < i:
            x, y = sorted_array[i], sorted_array[j]
            current_sum = x + y
            if current_sum > s:
                break
            elif current_sum == s:
                return x, y
            else:
                j += 1

        i -= 1
    return -1


for array, s in [
    ([-3, 1, 4, 6], 7),
    ([1, 2, 3, 4, 5, 6], 7),
    ([1, 2, 3, 4, 5, 6], 9),
    ([1, 2, 3, 4, 5, 6], 7),
    ([1, 2, 3, 4, 5, 6], 8),
    (list(range(int(1e7))), 129765)
]:
    result = find_sum_components(array, s)
    assert result != -1
    assert result[0] + result[1] == s
