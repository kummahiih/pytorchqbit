#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>

"""
Pauli group related definitions
"""

import typing
import numpy as np
from .gate import (PauliX, PauliY, PauliZ, Identity)


class _P1():
    """P1 is the First Pauli Group done from the cross product of
[-1, 1, -1j, 1j] and [Identity(), PauliX(), PauliY(), PauliZ()]


    >>> P1
    P1
    >>> len(P1())
    16
    >>> (P1()[0] == -1*Identity()).all()
    True
    >>> (P1()[1] ==  1*Identity()).all()
    True
    >>> (P1()[2] == -1j*Identity()).all()
    True
    >>> (P1()[3] ==  1j*Identity()).all()
    True
    >>> (P1()[15] == 1j*PauliZ()).all()
    True

P1 is a group, so these apply:

Associativy:

    >>> all([ any([equal(apply(a,b), c) for c in P1()]) for a in P1() for b in P1()])
    True

Identity:

    >>> equal( Identity(), P1()[1])
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
    def __call__(self) -> typing.List[np.ndarray]:
        return [
            -1  * Identity(), #  0
            1   * Identity(), #  1
            -1j * Identity(), #  2
            1j  * Identity(), #  3
            -1  * PauliX(),   #  4
            1   * PauliX(),   #  5
            -1j * PauliX(),   #  6
            1j  * PauliX(),   #  7
            -1  * PauliY(),   #  8
            1   * PauliY(),   #  9
            -1j * PauliY(),   # 10
            1j  * PauliY(),   # 11
            -1  * PauliZ(),   # 12
            1   * PauliZ(),   # 13
            -1j * PauliZ(),   # 14
            1j  * PauliZ()    # 15
            ]

P1 = _P1()
