"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

import numpy as np
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
