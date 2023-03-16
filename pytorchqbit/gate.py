
#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>

"""
Quatum gates from https://en.wikipedia.org/wiki/Quantum_logic_gate
"""

from math import e
import torch
from .convert import convert_to_complex


class _Identity():
    """Identity gate

    >>> Identity
    Identity
    >>> Identity()
    tensor([[1.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j]])
    >>> Identity(2)
    tensor([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])


    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'Identity'
    def __call__(self, n:int = 1) -> torch.Tensor:
        return convert_to_complex(torch.eye(2*n))

Identity = _Identity()

class _H():
    """Hadamard gate

    >>> H
    H
    >>> H()
    tensor([[ 0.7071+0.j,  0.7071+0.j],
            [ 0.7071+0.j, -0.7071+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'H'
    def __call__(self) -> torch.Tensor:
        return (2**-0.5)*convert_to_complex([[1, 1], [1, -1]])

H = _H()

class _PauliX():
    """Pauli X gate

    >>> PauliX
    X
    >>> PauliX()
    tensor([[0.+0.j, 1.+0.j],
            [1.+0.j, 0.+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'X'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([[0, 1], [1, 0]])

PauliX = _PauliX()

class _PauliY():
    """Pauli Y gate

    >>> PauliY
    Y
    >>> PauliY()
    tensor([[0.+0.j, -0.-1.j],
            [0.+1.j, 0.+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'Y'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([
            [0, -1j],
            [1j, 0]])

PauliY = _PauliY()

class _PauliZ():
    """Pauli Z gate

    >>> PauliZ
    Z
    >>> PauliZ()
    tensor([[ 1.+0.j,  0.+0.j],
            [ 0.+0.j, -1.+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'Z'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([
            [1, 0],
            [0, -1]])

PauliZ = _PauliZ()

class _Phase():
    """Phase (S, P) gate

    >>> Phase
    P
    >>> Phase()
    tensor([[1.+0.j, 0.+0.j],
            [0.+0.j, 0.+1.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'P'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([[1, 0], [0, 0+1j]])

Phase = _Phase()

class R:
    """R is the custom phase shift gate

    >>> from math import pi
    >>> R(pi/4)
    R(0.7853981633974483)
    >>> R(pi/4)()
    tensor([[1.0000+0.0000j, 0.0000+0.0000j],
            [0.0000+0.0000j, 0.7071+0.7071j]])


    """
    def __init__(self, phase_shift):
        self._phase_shift = phase_shift
    def __repr__(self):
        return 'R(%s)'%self._phase_shift
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([[1, 0], [0, e**((0 + 1j) * self._phase_shift)]])


class _CNOT:
    """CNOT is the Controlled Not gate (CX)

    >>> CNOT
    CX
    >>> CNOT()
    tensor([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j],
            [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'CX'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]])

CNOT = _CNOT()

class _CPauliZ:
    """CPauliZ is the Controlled Pauli Z gate (CZ)

    >>> CPauliZ
    CZ
    >>> CPauliZ()
    tensor([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
            [ 0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j],
            [ 0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
            [ 0.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'CZ'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1]])

CPauliZ = _CPauliZ()

class _SWAP:
    """SWAP is the qbit swap gate

    >>> SWAP
    SWAP
    >>> SWAP()
    tensor([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'SWAP'
    def __call__(self) -> torch.Tensor:
        return convert_to_complex([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]])

SWAP = _SWAP()

def apply(state: torch.Tensor, gate: torch.Tensor) -> torch.Tensor:
    """Apply gate to a state

For example this chain evaluates to zero:

    >>> from functools import reduce
    >>> s = reduce( apply, [Zero(), H(), PauliZ(), H(), PauliX()])
    >>> Measure.one(s)
    0

Swap places of a bit

    >>> one = Combine(Zero(), One())
    >>> Measure.one(one)
    1
    >>> one
    tensor([[0.+0.j],
            [1.+0.j],
            [0.+0.j],
            [0.+0.j]])
    >>> two = apply(one, SWAP())
    >>> Measure.one(two)
    2
    >>> two
    tensor([[0.+0.j],
            [0.+0.j],
            [1.+0.j],
            [0.+0.j]])


    """

    return torch.matmul(gate, state)
