"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

import numpy as np
from math import pi, e
from .reprwrapper import _withrepr

@_withrepr(lambda x: "Identity")
def Identity() -> np.array:
    """
    Identity gate
    >>> Identity
    Identity
    >>> Identity()
    array([[1, 0],
           [0, 1]])

    """
    return np.array([[1,0],[0, 1]])

@_withrepr(lambda x: "H")
def H() -> np.array:
    """
    Hadamard gate
    >>> H
    H
    >>> H()
    array([[ 0.70710678,  0.70710678],
           [ 0.70710678, -0.70710678]])

    """
    return (2**-0.5)*np.array([[1,1],[1,-1]])

@_withrepr(lambda x: "X")
def PauliX() -> np.array:
    """
    Pauli X gate
    >>> PauliX
    X
    >>> PauliX()
    array([[0, 1],
           [1, 0]])

    """
    return np.array([[0,1],[1,0]])

@_withrepr(lambda x: "Y")
def PauliY() -> np.array:
    """
    Pauli Y gate
    >>> PauliY
    Y
    >>> PauliY()
    array([[ 0.+0.j, -0.-1.j],
           [ 0.+1.j,  0.+0.j]])

    """
    return np.array([[0, -1j],[1j, 0]])


@_withrepr(lambda x: "Z")
def PauliZ() -> np.array:
    """
    Pauli Z gate
    >>> PauliZ
    Z
    >>> PauliZ()
    array([[ 0,  1],
           [ 0, -1]])

    """
    return np.array([[0, 1],[0, -1]])


@_withrepr(lambda x: "P")
def Phase() -> np.array:
    """
    Phase (S, P) gate
    >>> Phase
    P
    >>> Phase()
    array([[1.+0.j, 0.+0.j],
           [0.+0.j, 0.+1.j]])

    """
    return np.array([[1, 0],[0, 0+1j]])


class R:
    """Custom phase shift gate R
    >>> from math import pi
    >>> R(pi/4)
    R(0.7853981633974483)
    >>> R(pi/4)()
    array([[1.        +0.j        , 0.        +0.j        ],
           [0.        +0.j        , 0.70710678+0.70710678j]])

    """
    def __init__(self, phase_shift):
       self._phase_shift = phase_shift
    def __repr__(self): return 'R(%s)'%self._phase_shift
    def __call__(self):
           return np.array([[1, 0],[0, e**((0+1j)*self._phase_shift)]])


