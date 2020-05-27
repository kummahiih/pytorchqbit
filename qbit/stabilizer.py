#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>

"""
Quantum error correction code.
"""

import typing
from itertools import product
from functools import reduce
import numpy as np
from .gate import (PauliX, PauliY, PauliZ, Identity, apply)

class _S_5_1_3:
    """S_5_1_3 error correction code encodes one logical qubit into five physical qubits.
    S_5_1_3 protects against an arbitrary single-qubit error and it has code distance three codes.

    >>> S_5_1_3
    S_5_1_3

    >>> S_5_1_3.g1()
    array([[ 0.,  1.,  1.,  0.,  1.,  0.,  0.,  1.,  1.,  0.],
           [ 1.,  0.,  0., -1.,  0., -1.,  1.,  0.,  0.,  1.]])

    >>> S_5_1_3.g2()
    array([[ 1.,  0.,  0.,  1.,  1.,  0.,  1.,  0.,  0.,  1.],
           [ 0.,  1.,  1.,  0.,  0., -1.,  0., -1.,  1.,  0.]])

    >>> S_5_1_3.g3()
    array([[ 0.,  1.,  1.,  0.,  0.,  1.,  1.,  0.,  1.,  0.],
           [ 1.,  0.,  0.,  1.,  1.,  0.,  0., -1.,  0., -1.]])

    >>> S_5_1_3.g4()
    array([[ 1.,  0.,  0.,  1.,  1.,  0.,  0.,  1.,  1.,  0.],
           [ 0., -1.,  1.,  0.,  0.,  1.,  1.,  0.,  0., -1.]])

    """

    def __init__(self):
        pass

    @staticmethod
    def g1() -> np.ndarray:
        return np.hstack([PauliX(), PauliZ(), PauliZ(), PauliX(), Identity()])

    @staticmethod
    def g2() -> np.ndarray:
        return np.hstack([Identity(), PauliX(), PauliZ(), PauliZ(), PauliX()])

    @staticmethod
    def g3() -> np.ndarray:
        return np.hstack([PauliX(), Identity(), PauliX(), PauliZ(), PauliZ()])

    @staticmethod
    def g4() -> np.ndarray:
        return np.hstack([PauliZ(), PauliX(), Identity(), PauliX(), PauliZ()])

    def __repr__(self):
        return 'S_5_1_3'

#NOT READY
S_5_1_3 = _S_5_1_3()

