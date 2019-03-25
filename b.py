"""
This module takes two version numbers as defined by Semantic versioning and 
returns wether a given version number is newer older or the same a reference
version. Version numbers supported are of type
    Major.Minor.Patch

The delimiter defaults to "." but can be supplied and must be the same in all
occurences for a given test.

For convinience this module can be called from the command line as such
    python b.py 1.2ba.2a 1.2b.2
    python b.py 1_2ba_2a 1_2b_2 _
"""

import re

def compare_versions(v1, v2, delimiter='.'):
    """Takes two version numbers of format Major.Minor.Patch and returns wether
    one is equal 0, smaller -1 of larger 1 than the other
    
    arguments v1, v2:
        version of format Major.Minor.Patch"""
    val1 = _get_version_elements(v1, delimiter)
    val2 = _get_version_elements(v2, delimiter)
    return _compare_versions_aslist(val1, val2)

def _compare_versions_aslist(v1 ,v2):
    """Compare two lists [major, minor, patch]
    return relationship as:
        -1 v1 is smaller than v2
        0 v1 is equal to v2
        1 v1 is larger than v2
    """
    # if lists are identical the versions are the same
    if v1 == v2:
        return 0

    lv1 = len(v1)
    lv2 = len(v2)

    # if different value is found return relationship (larger 1 or smaller -1)
    for i in range(min(lv1, lv2)):
        value1 = list(filter(None, re.split("[0-9]+", v1[i]))) + list(filter(None, re.split("[a-zA-Z]+", v1[i])))
        value2 = list(filter(None, re.split("[0-9]+", v2[i]))) + list(filter(None, re.split("[a-zA-Z]+", v2[i])))
        if value1 > value2:
            return 1
        if value1 < value2:
            return -1

    # first values in list were identical: longest list is of newer version
    if lv1 > lv2:
        return 1
    return -1

def _get_version_elements(v, delimiter='.'):
    """parse version string and return in list as [Marjo, Minor, Patch]
    
    arguement version number: 1.1a.2
    returns: list such as: [1, '1a', 1]
    """
    return v.split(delimiter)

def _brakedown_version_element(element):
    """Take version eleement and return list with int and string components
    argument version_element: alphanumeric value such as:
        10
        5a
    returns: list with elements such as:
        [10]
        [5, 'a']
    """
    return list(filter(None, re.split("[a-zA-Z]+", element))) + list(filter(None, re.split("[0-9]+", element)))

if __name__ == '__main__':
    import sys
    OUTPUT = ['is SMALLER than', 'is EQUAL to', 'is LARGER than']
    if len(sys.argv) != 3 and len(sys.argv) !=4:
        print('Usage: python __name__.py version1 version2')
    elif len(sys.argv) == 4:
        result = compare_versions(sys.argv[1], sys.argv[2], '_')
        print(sys.argv[1], OUTPUT[result + 1], sys.argv[2])
    elif len(sys.argv) == 3:
        result = compare_versions(sys.argv[1], sys.argv[2])
        print(sys.argv[1], OUTPUT[result + 1], sys.argv[2])

