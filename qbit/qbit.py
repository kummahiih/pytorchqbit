#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""
Representation of single qubit basic states
"""

import random
import numpy as np


class _Zero():
    """Qubit that evaluates as zero every single time

    >>> Zero
    |0>
    >>> Zero()
    array([[1],
           [0]])
    >>> Measure.one(Zero())
    0

    """
    def __init__(self):
        pass
    def __repr__(self):
        return '|0>'
    def __call__(self) -> np.ndarray:
        return np.array([[1], [0]])

Zero = _Zero()

class _One():
    """Qubit that evaluates as one every single time

    >>> One
    |1>
    >>> One()
    array([[0],
           [1]])
    >>> Measure.one(One())
    1

    """
    def __init__(self):
        pass
    def __repr__(self):
        return '|1>'
    def __call__(self) -> np.ndarray:
        return np.array([[0], [1]])

One = _One()

class _Plus():
    """Qubit that evaluates as one and zero evenly

    >>> Plus
    |+>
    >>> Plus()
    array([[0.70710678],
           [0.70710678]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return '|+>'
    def __call__(self) -> np.ndarray:
        return (2**-0.5) *(Zero() + One())

Plus = _Plus()

class _Minus():
    """Qubit that evaluates as one and zero evenly

    >>> Minus
    |->
    >>> Minus()
    array([[ 0.70710678],
           [-0.70710678]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return '|->'
    def __call__(self) -> np.ndarray:
        return (2**-0.5) *(Zero() - One())

Minus = _Minus()

def a(array: np.ndarray) -> complex:
    """a**2 is the probability for qbit == False"""
    return array[0][0] + 0j

def b(array: np.ndarray) -> complex:
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
    def one(q_bit: np.ndarray) -> int:
        """Gets a random value according the quantum state weights"""
        return random.choices(range(len(q_bit)), q_bit * q_bit, k=1)[0]

Measure = _Measure()

def Combine(x, y):
    """Use Kronecker product of two arrays to combine qubits.

    >>> Combine(Zero(),Zero())
    array([[1],
           [0],
           [0],
           [0]])


    >>> from functools import reduce
    >>> reduce(Combine, [One(), Zero(), Zero()])
    array([[0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0]])

Each row represents the probability of getting it's index's value as a result

    >>> Measure.one(Combine(Zero(),Zero()))
    0

    >>> Measure.one( Combine(One(), Combine(Zero(),Zero())) )
    4

    """
    return np.kron(x, y)


def equal(x: np.ndarray, y: np.ndarray, atol=1e-10) -> bool:
    """The equal is a test if the two qubit states

    >>> equal(One(), One())
    True
    >>> equal(One(), Zero())
    False

    """

    # maybe there is a np shorthand for this,
    # but at least i can change it from one place if this does not work well
    return np.linalg.norm(x - y) < atol
