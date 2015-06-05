import sys


if sys.version_info[0] < 3:
    raise TypeError("Must be using Python 3")


def test():
    """ Print foo
    >>> test()
    'foo'
    """
    return 'foo'


def _test():
    import doctest
    (failure_count, test_count) = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if failure_count:
        exit(-1)


if __name__ == '__main__':
    _test()
