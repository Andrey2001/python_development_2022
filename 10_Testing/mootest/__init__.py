#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""The moo module."""

# python -m doctest -v mootest/__init__.py


def moo(mes="", moo="moo", moos=1, sep=", "):
    """
        Say smth an moo moos times

        :param mes: Message to say
        :param moo: What to moo
        :param moos: # of moos
        :param sep: Moo separator

    >>> moo()
    ', moo'
    >>> moo("Hello")
    'Hello, moo'
    >>> moo("Hi", haha, 5)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'haha' is not defined
    >>> moo("Hi", "haha", 5)
    'Hi, haha, haha, haha, haha, haha'
    >>> moo("Hello", "dude")
    'Hello, dude'
    >>> moo("Hello", "dude", 3)
    'Hello, dude, dude, dude'
    """

    return f"{mes}, {(sep.join([moo] * int(moos)))}"
