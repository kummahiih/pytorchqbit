"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

import numpy as np
import random
from .reprwrapper import _withrepr

"""
Representation of single qubit basic states and operations for self study
"""


def a(array: np.array) -> complex:
    """a**2 is the probability for qbit == False"""
    return array[0][0] + 0j

def b(array: np.array) -> complex:
    """b**2 is the probability for qbit == True"""
    return array[1][0] + 0j

@_withrepr(lambda x: "M")
def Measure(q_bit: np.array) -> bool:
    """Measures if one dimensional qbit value is True this time"""
    if random.random() < b(q_bit)**2:
        return True
    return False

@_withrepr(lambda x: "|0>")
def Zero() -> np.array:
    """
    Qubit that evaluates as zero every single time
    >>> Zero
    |0>
    >>> Zero()
    array([[1],
           [0]])
    >>> Measure(Zero())
    False

    """
    return np.array([[1], [0]])

@_withrepr(lambda x: "|1>")
def One() -> np.array:
    """
    Qubit that evaluates as one every single time
    >>> One
    |1>
    >>> One()
    array([[0],
           [1]])
    >>> Measure(One())
    True
    
    """
    return np.array([[0], [1]])

@_withrepr(lambda x: "|+>")
def Plus() -> np.array:
    """
    Qubit that evaluates as one and zero evenly
    >>> Plus
    |+>
    >>> Plus()
    array([[0.70710678],
           [0.70710678]])
    
    """
    return (2**-0.5) *(Zero() + One())

@_withrepr(lambda x: "|->")
def Minus() -> np.array:
    """
    Qubit that evaluates as one and zero evenly
    >>> Minus
    |->
    >>> Minus()
    array([[ 0.70710678],
           [-0.70710678]])
    
    """
    return (2**-0.5) *(Zero() - One())

