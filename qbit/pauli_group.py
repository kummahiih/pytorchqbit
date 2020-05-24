#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>

"""
Pauli group related definitions
"""

import typing
from itertools import product
from functools import reduce
import numpy as np
from .gate import (PauliX, PauliY, PauliZ, Identity, apply)


class _P1():
    """P1 is the First Pauli Group done from the cross product of
[-1, 1, -1j, 1j] and [Identity(), PauliX(), PauliY(), PauliZ()]


    >>> P1
    P1
    >>> p1 = list(P1())
    >>> len(p1)
    16
    >>> equal(p1[0], -1*Identity())
    True
    >>> equal(p1[1], 1*Identity())
    True
    >>> equal(p1[2], -1j*Identity())
    True
    >>> equal(p1[3], 1j*Identity())
    True
    >>> equal(p1[15], 1j*PauliZ())
    True

p1 is a group, so these apply:

Associativy:

    >>> all([ any([equal(apply(a,b), c) for c in P1()]) for a in P1() for b in P1()])
    True

Identity:

    >>> equal( Identity(), p1[1])
    True

    >>> all([ equal(apply(a, Identity()), a) for a in P1()])
    True

Inverse element:

    >>> all([ any([equal(apply(a, b), Identity()) for b in P1()]) for a in P1() ])
    True

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'P1'
    def __call__(self) -> typing.Iterator[np.ndarray]:
        return map(lambda x: x[0] * x[1], product([Identity(), PauliX(), PauliY(), PauliZ()], [-1, 1, -1j, 1j]))

P1 = _P1()

