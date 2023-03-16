#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""
Representation of single qubit basic states
"""

import random
import torch
from .convert import convert_to_complex
 


class _Zero():
    """Qubit that evaluates as zero every single time

    >>> Zero
    |0>
    >>> Zero()
    tensor([[1.+0.j],
            [0.+0.j]])
    >>> Measure.one(Zero())
    0

    """
    def __init__(self):
        pass
    def __repr__(self):
        return '|0>'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([[1], [0]])

Zero = _Zero()

class _One():
    """Qubit that evaluates as one every single time

    >>> One
    |1>
    >>> One()
    tensor([[0.+0.j],
            [1.+0.j]])
    >>> Measure.one(One())
    1

    """
    def __init__(self):
        pass
    def __repr__(self):
        return '|1>'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([[0], [1]])

One = _One()

class _Plus():
    """Qubit that evaluates as one and zero evenly

    >>> Plus
    |+>
    >>> Plus()
    tensor([[0.7071+0.j],
            [0.7071+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return '|+>'
    def __call__(self) -> torch.Tensor:
        return (2**-0.5) *(Zero() + One())

Plus = _Plus()

class _Minus():
    """Qubit that evaluates as one and zero evenly

    >>> Minus
    |->
    >>> Minus()
    tensor([[ 0.7071+0.j],
            [-0.7071+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return '|->'
    def __call__(self) -> torch.Tensor:
        return (2**-0.5) *(Zero() - One())

Minus = _Minus()

def a(array: torch.Tensor) -> complex:
    """a**2 is the probability for qbit == False"""
    return array[0][0] + 0j

def b(array: torch.Tensor) -> complex:
    """b**2 is the probability for qbit == True"""
    return array[1][0] + 0j

class _Measure:
    """Simulates the measure process of the qubit

    >>> Measure.one(One())
    1

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'M'
    @staticmethod
    def one(q_bit: torch.Tensor) -> int:
        """Gets a random value according the quantum state weights"""

        return random.choices(range(len(q_bit)), (q_bit * q_bit).real, k=1)[0]

Measure = _Measure()

def Combine(x, y, *rest):
    """Use Kronecker product of two arrays to combine qubits.

    >>> Combine(Zero(),Zero())
    tensor([[1.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j]])


    >>> from functools import reduce
    >>> reduce(Combine, [One(), Zero(), Zero()])
    tensor([[0.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j],
            [1.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j]])
    >>> Combine(One(), Zero(), Zero())
    tensor([[0.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j],
            [1.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j]])

Each row represents the probability of getting it's index's value as a result

    >>> Measure.one(Combine(Zero(),Zero()))
    0

    >>> Measure.one( Combine(One(), Combine(Zero(),Zero())) )
    4

    """
    if len(rest) == 0:
        return torch.kron(x, y)
    return Combine(torch.kron(x, y), *rest)


def equal(x: torch.Tensor, y: torch.Tensor, atol=1e-10) -> bool:
    """The equal is a test if the two qubit states

    >>> equal(One(), One())
    True
    >>> equal(One(), Zero())
    False

    """

    # maybe there is a np shorthand for this,
    # but at least i can change it from one place if this does not work well
    return (torch.linalg.norm(x - y) < atol).item()
