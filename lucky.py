# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""


def longest_lucky_series(series: str) -> str:
    max_series = ''
    max_len = 0
    current_series = ''
    for x in series:
        if x in ['5', '6']:
            current_series += x
        else:
            series_len = len(current_series)
            if series_len > max_len and set(current_series) not in [{'5'}, {'6'}]:
                max_len = series_len
                max_series = current_series
                current_series = ''
    else:
        series_len = len(current_series)
        if series_len > max_len and set(current_series) not in [{'5'}, {'6'}]:
            max_series = current_series

    if not max_series:
        max_series = '0'

    return max_series


assert longest_lucky_series('56565565659') == '5656556565'
assert longest_lucky_series('5656556565') == '5656556565'
assert longest_lucky_series('566436') == '566'
assert longest_lucky_series('55555') == '0'
assert longest_lucky_series('666') == '0'
assert longest_lucky_series('666564566666756565655') == '56565655'
