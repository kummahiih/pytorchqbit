"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

import numpy as np
import random

"""
Representation of single qubit basic states and operations for self study
"""




class Zero():
    """
    Qubit that evaluates as zero every single time
    >>> Zero()
    |0>
    >>> Zero()()
    array([[1],
           [0]])
    >>> Measure().MeasureOne(Zero()())
    False

    """
    def __init__(self): pass
    def __repr__(self): return '|0>'
    def __call__(self) -> np.array:
        return np.array([[1], [0]])

class One():
    """
    Qubit that evaluates as one every single time
    >>> One()
    |1>
    >>> One()()
    array([[0],
           [1]])
    >>> Measure().MeasureOne(One()())
    True
    
    """
    def __init__(self): pass
    def __repr__(self): return '|1>'
    def __call__(self) -> np.array:
        return np.array([[0], [1]])

class Plus():
    """
    Qubit that evaluates as one and zero evenly
    >>> Plus()
    |+>
    >>> Plus()()
    array([[0.70710678],
           [0.70710678]])
    
    """
    def __init__(self): pass
    def __repr__(self): return '|+>'
    def __call__(self) -> np.array:
        return (2**-0.5) *(Zero()() + One()())

class Minus():
    """
    Qubit that evaluates as one and zero evenly
    >>> Minus()
    |->
    >>> Minus()()
    array([[ 0.70710678],
           [-0.70710678]])
    
    """
    def __init__(self): pass
    def __repr__(self): return '|->'
    def __call__(self) -> np.array:
        return (2**-0.5) *(Zero()() - One()())

def a(array: np.array) -> complex:
    """a**2 is the probability for qbit == False"""
    return array[0][0] + 0j

def b(array: np.array) -> complex:
    """b**2 is the probability for qbit == True"""
    return array[1][0] + 0j

class Measure:
    """
    >>> isinstance(Measure(), Measure)
    True

    """
    def __init__(self): pass
    def __repr__(self): return 'M'
    def MeasureOne(self, q_bit: np.array) -> bool:
        """Measures if one dimensional qbit value is True this time"""
        if random.random() < b(q_bit)**2:
            return True
        return False

def Combine(a, b):
    """
    Use Kronecker product of two arrays to combine qubits.

    >>> Combine(Zero()(),Zero()())
    array([[1],
           [0],
           [0],
           [0]])

    >>> Combine(One()(), Combine(Zero()(),Zero()()))
    array([[0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0]])

    """
    return np.kron(a, b)
