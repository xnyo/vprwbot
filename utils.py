import hashlib
import random

from constants import AESTHETIC_LETTERS, AESTHETIC_SYMBOLS


def md5(s):
    """
    Calculates the md5 hash of a string

    :param s: input string
    :return: md5 of the given string, as `str`
    """
    d = hashlib.md5()
    d.update(s.encode("utf-8"))
    return d.hexdigest()


def clamp(value, min_, max_):
    """
    Clamps `value` between `min_` and `max_`

    :param value: input value
    :param min_: minimum
    :param max_: maximum
    :return: clamped value
    """
    return max(min_, min(value, max_))


def aestheticize(s, spaced=False, symbols=True):
    """
    A E S T H E T I C I Z E S  a string

    :param s: input string
    :param spaced: if `True`, put additional spaces between each letter
    :param symbols: if `True`, append some aesthetic symbols to the string
    :return: aestheticized string
    """
    joiner = " " if spaced else ""
    final_string = joiner.join(AESTHETIC_LETTERS[x] if x in AESTHETIC_LETTERS else x for x in s)
    if symbols:
        final_string += "  " * (2 if spaced else 1 if s else 0)
        final_string += joiner.join(random.choice(AESTHETIC_SYMBOLS) for _ in range(clamp(len(s) // 5, min_=3, max_=7)))
    return final_string


def upperlower(s):
    """
    ReTuRnS S LiKe tHiS

    :param s: input string
    :return: S BuT LiKe tHiS
    """
    return "".join([x.upper() if i % 2 == 0 else x.lower() for i, x in enumerate(s)])
