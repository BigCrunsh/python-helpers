from __future__ import absolute_import  # to get builtin lib and not local
import itertools as _itertools


def groupby(iterable, key=None):
    """
    Create an iterator which returns (key, sub-iterator) grouped by each value of key(value).

    The itertools groupby requires the iterable to be sorted by the key. This is a short hand.

    Args:
        iterable (iterable): iterable to be sorted.
        key (func): value of key function is used to group

    Returns:
        itertools.groupby: iterator that returns consecutive keys and groups from the iterable
    """
    if key is None:
        key = lambda x: x
    return _itertools.groupby(sorted(iterable, key=key), key=key)
