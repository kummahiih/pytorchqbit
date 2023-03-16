#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>

"""
Quantum error correction code.
"""

import typing
from itertools import product
from functools import reduce
import torch
from .gate import (PauliX, PauliY, PauliZ, Identity, apply)

class _S_5_1_3:
    """S_5_1_3 error correction code encodes one logical qubit into five physical qubits.
    S_5_1_3 protects against an arbitrary single-qubit error and it has code distance three codes.

    >>> S_5_1_3
    S_5_1_3

    >>> S_5_1_3.g1()
    tensor([[ 0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j],
            [ 1.+0.j,  0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j, -1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j]])

    >>> S_5_1_3.g2()
    tensor([[ 1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j],
            [ 0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j, -1.+0.j,  1.+0.j,  0.+0.j]])

    >>> S_5_1_3.g3()
    tensor([[ 0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
            [ 1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j, -1.+0.j]])

    >>> S_5_1_3.g4()
    tensor([[ 1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j],
            [ 0.+0.j, -1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]])

    """

    def __init__(self):
        pass

    @staticmethod
    def g1() -> torch.Tensor:
        return torch.hstack([PauliX(), PauliZ(), PauliZ(), PauliX(), Identity()])

    @staticmethod
    def g2() -> torch.Tensor:
        return torch.hstack([Identity(), PauliX(), PauliZ(), PauliZ(), PauliX()])

    @staticmethod
    def g3() -> torch.Tensor:
        return torch.hstack([PauliX(), Identity(), PauliX(), PauliZ(), PauliZ()])

    @staticmethod
    def g4() -> torch.Tensor:
        return torch.hstack([PauliZ(), PauliX(), Identity(), PauliX(), PauliZ()])

    def __repr__(self):
        return 'S_5_1_3'

#NOT READY
S_5_1_3 = _S_5_1_3()

