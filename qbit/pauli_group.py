#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>

"""
Pauli group related definitions
"""

import typing
from itertools import product
from functools import reduce
import numpy as np
from .gate import (PauliX, PauliY, PauliZ, Identity)


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
#        return [
#            -1  * Identity(), #  0
#            1   * Identity(), #  1
#            -1j * Identity(), #  2
#            1j  * Identity(), #  3
#            -1  * PauliX(),   #  4
#            1   * PauliX(),   #  5
#            -1j * PauliX(),   #  6
#            1j  * PauliX(),   #  7
#            -1  * PauliY(),   #  8
#            1   * PauliY(),   #  9
#            -1j * PauliY(),   # 10
#            1j  * PauliY(),   # 11
#            -1  * PauliZ(),   # 12
#            1   * PauliZ(),   # 13
#            -1j * PauliZ(),   # 14
#            1j  * PauliZ()    # 15
#            ]
#
P1 = _P1()

class Pn:
    """Pn is the n:th Pauli group instance

    >>> p2 = Pn(2)
    >>> p2
    P2
    >>> len(list(p2()))
    256

    """

    def __init__(self, n: int):
        self.n = n

    def __repr__(self):
        return 'P%d'%(self.n)

    def __call__(self) -> typing.Iterator[np.ndarray]:
        if self.n == 1:
            return P1()
        return reduce(product, [P1() for _ in range(self.n)])

