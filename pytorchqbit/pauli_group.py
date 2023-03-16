#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>

"""
Pauli group related definitions
"""

import typing
from itertools import product
from functools import reduce
import torch
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
    def __call__(self) -> typing.Iterator[torch.Tensor]:
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

    >>> P2 = Pn(2)
    >>> P2
    P2
    >>> p2 = list(P2())
    >>> len(p2)
    1024
    >>> p2[0]
    tensor([[-1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
            [ 0.+0.j, -1.+0.j,  0.+0.j,  0.+0.j],
            [ 0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j],
            [ 0.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]])

    >>> p2[1]
    tensor([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])


p2 is a group, so these apply:

Associativy:

    >>> import random
    >>> all_products = [apply(a,b) for a in p2 for b in p2]
    >>> all([ any([equal(p, c) for c in p2]) for p in random.sample(all_products, 1000)])
    True

Identity:

    >>> equal(Identity(2), p2[1])
    True
    >>> i2 = p2[1]
    >>> all([ equal(apply(a, i2), a) for a in p2])
    True

Inverse element:

    >>> all([ any([equal(apply(a, b), i2) for b in p2]) for a in random.sample(p2, 20)])
    True

    """

    def __init__(self, n: int):
        self.n = n

    def __repr__(self):
        return 'P%d'%(self.n)

    def __call__(self) -> typing.Iterator[torch.Tensor]:
        if self.n == 1:
            return P1()
        for items in reduce(product, [P1() for _ in range(self.n)]):
            tensor_part = reduce(torch.kron, items)
            for multiplier in [-1, 1, -1j, 1j]:
                yield multiplier * tensor_part

