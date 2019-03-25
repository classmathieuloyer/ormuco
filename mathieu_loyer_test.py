"""
This module runs a series of test cases on modules a and b of the Ormuco
questions.

Usage: python2 test.py or python3 test.py
tests for a.py output if lines are overlaping
tests for b.py output -1, 0 or 1 according to if the first of two version
numbers is smaller than, equal to or larger than the second one.

For details of modules a and b refer to their respective files.
"""

import time
import a
import b
import c


def _test_module(f, test_cases):
    """Runs test_cases with function f on origin module

    arguments
        f: module with function to run test_cases on
        test_cases: list with test values to run into module function f

    """
    print('## Testing %s' % f.__name__)
    for t in test_cases:
        print('Testing %s with values: %s' % (f.__name__, str(t)))
        print(f(t[0], t[1]))
    print()


test_cases_a = [
        ([0, 10],[10, 20]), 
        ([-10, -9],[-1, -2]), 
        ([-10, -5],[-7, 2]), 
        ([-5, -10],[2, -7]), 
        ([-10, 10],[1, 2]),
        ]

test_cases_b = [
        ('1.1.1', '1.1.1'),
        ('1.1.1', '1.1.1', '.'),
        ('1_1_1', '1_1_2', '_'),
        ('1_1_2', '1_1_1', '_'),
        ('1_2_1', '1_1_2', '_'),
        ('1_10_1', '1_5_20', '_'),
        ('0.1.1', '1.1.1'),
        ('1.1az.1', '1.1b.1'),
        ('1a.1.1', '1.2d.1'),
        ('1abc.1def.1abc', '1abc.2def.1abc')
        ]

test_cases_c = [
    ('t1', 1),
    ('t2', 2),
    ('t3', 3),
    ('t4', 4),
    ('t5', 5),
    ('t6', 6),
    ('t7', 7)
        ]

_test_module(a.are_lines_overlaping, test_cases_a)
_test_module(b.compare_versions, test_cases_b)

# test c.py
max_cached_items = 5
stale_delay = 2  # in seconds

print('## Testing lru (c.py)')
print('Setting up lru with max 5 items and expiry time of 2 seconds')
lru = c.Lru(max_cached_items, stale_delay)
for k, v in test_cases_c:
    print('Adding element in lru')
    lru.set_value(k, v)
    print('Current values in lru %s' % lru.get_values())
print('wainting for 1 second')
time.sleep(1)
lru.set_value('t6', 6)
print('waiting for initial values to expire')
time.sleep(1)
print('Current values in lru %s' % lru.get_values())

