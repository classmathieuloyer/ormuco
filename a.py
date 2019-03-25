"""
This module will take two sets of two numbers. Each set will represent the 
start and end of a non zero length line on the x axis. The module will return 
a boolean indicating if the lines represented by the two sets of two values 
overlap.
Example: are_lines_overlaping((-10,-5.2), (-7,0)) will return true.
"""

def are_lines_overlaping(l1, l2):
    """Return if two lines are overlaping

    arguments:
    l1, l2 -- lines on x axis of non zero length"""
    return max(min(l1,l2)) > min(max(l1, l2))


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 5:
        print('Test usage: python __name__.py x1 x2 x3 x4')
    else:    
        l1 = [float(sys.argv[1]), float(sys.argv[2])]
        l2 = [float(sys.argv[3]), float(sys.argv[4])]
        print('Lines overlaping?:', are_lines_overlaping(l1, l2))
