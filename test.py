import sys


if sys.version_info[0] < 3:
    raise TypeError("Must be using Python 3")


def test():
    """ Print foo
    >> test()
    foo
    """
    return 'foo'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
