"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

import numpy as np
import random

"""
Representation of single qubit basic states
"""



class _Zero():
    """Qubit that evaluates as zero every single time

    >>> Zero
    |0>
    >>> Zero()
    array([[1],
           [0]])
    >>> Measure.One(Zero())
    0

    """
    def __init__(self): pass
    def __repr__(self): return '|0>'
    def __call__(self) -> np.array:
        return np.array([[1], [0]])

Zero = _Zero()

class _One():
    """Qubit that evaluates as one every single time

    >>> One
    |1>
    >>> One()
    array([[0],
           [1]])
    >>> Measure.One(One())
    1
    
    """
    def __init__(self): pass
    def __repr__(self): return '|1>'
    def __call__(self) -> np.array:
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
    def __init__(self): pass
    def __repr__(self): return '|+>'
    def __call__(self) -> np.array:
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
    def __init__(self): pass
    def __repr__(self): return '|->'
    def __call__(self) -> np.array:
        return (2**-0.5) *(Zero() - One())

Minus = _Minus()

def a(array: np.array) -> complex:
    """a**2 is the probability for qbit == False"""
    return array[0][0] + 0j

def b(array: np.array) -> complex:
    """b**2 is the probability for qbit == True"""
    return array[1][0] + 0j

class _Measure:
    """Simulates the measure process of the qubit

    >>> Measure.One(One())
    1

    """
    def __init__(self): pass
    def __repr__(self): return 'M'
    def One(self, q_bit: np.array) -> int:
        """Gets a random value according the quantum state weights"""
        return random.choices(range(len(q_bit)), q_bit * q_bit, k=1)[0]

Measure = _Measure()

def Combine(a, b):
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

    >>> Measure.One(Combine(Zero(),Zero()))
    0

    >>> Measure.One( Combine(One(), Combine(Zero(),Zero())) )
    4

    """
    return np.kron(a, b)
