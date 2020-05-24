
#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>

"""
Quatum gates from https://en.wikipedia.org/wiki/Quantum_logic_gate
"""

from math import e
import numpy as np

class _Identity():
    """Identity gate

    >>> Identity
    Identity
    >>> Identity()
    array([[1, 0],
           [0, 1]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'Identity'
    def __call__(self) -> np.ndarray:
        return np.array([[1, 0], [0, 1]])

Identity = _Identity()

class _H():
    """Hadamard gate

    >>> H
    H
    >>> H()
    array([[ 0.70710678,  0.70710678],
           [ 0.70710678, -0.70710678]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'H'
    def __call__(self) -> np.ndarray:
        return (2**-0.5)*np.array([[1, 1], [1, -1]])

H = _H()

class _PauliX():
    """Pauli X gate

    >>> PauliX
    X
    >>> PauliX()
    array([[0, 1],
           [1, 0]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'X'
    def __call__(self) -> np.ndarray:
        return np.array([[0, 1], [1, 0]])

PauliX = _PauliX()

class _PauliY():
    """Pauli Y gate

    >>> PauliY
    Y
    >>> PauliY()
    array([[ 0.+0.j, -0.-1.j],
           [ 0.+1.j,  0.+0.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'Y'
    def __call__(self) -> np.ndarray:
        return np.array([
            [0, -1j],
            [1j, 0]])

PauliY = _PauliY()

class _PauliZ():
    """Pauli Z gate

    >>> PauliZ
    Z
    >>> PauliZ()
    array([[ 1,  0],
           [ 0, -1]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'Z'
    def __call__(self) -> np.ndarray:
        return np.array([
            [1, 0],
            [0, -1]])

PauliZ = _PauliZ()

class _Phase():
    """Phase (S, P) gate

    >>> Phase
    P
    >>> Phase()
    array([[1.+0.j, 0.+0.j],
           [0.+0.j, 0.+1.j]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'P'
    def __call__(self) -> np.ndarray:
        return np.array([[1, 0], [0, 0+1j]])

Phase = _Phase()

class R:
    """R is the custom phase shift gate

    >>> from math import pi
    >>> R(pi/4)
    R(0.7853981633974483)
    >>> R(pi/4)()
    array([[1.        +0.j        , 0.        +0.j        ],
           [0.        +0.j        , 0.70710678+0.70710678j]])

    """
    def __init__(self, phase_shift):
        self._phase_shift = phase_shift
    def __repr__(self):
        return 'R(%s)'%self._phase_shift
    def __call__(self) -> np.ndarray:
        return np.array([[1, 0], [0, e**((0 + 1j) * self._phase_shift)]])


class _CNOT:
    """CNOT is the Controlled Not gate (CX)

    >>> CNOT
    CX
    >>> CNOT()
    array([[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'CX'
    def __call__(self) -> np.ndarray:
        return np.array([
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
    array([[ 1,  0,  0,  0],
           [ 0,  1,  0,  0],
           [ 0,  0,  1,  0],
           [ 0,  0,  0, -1]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'CZ'
    def __call__(self) -> np.ndarray:
        return np.array([
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
    array([[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 1]])

    """
    def __init__(self):
        pass
    def __repr__(self):
        return 'SWAP'
    def __call__(self) -> np.ndarray:
        return np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]])

SWAP = _SWAP()

def apply(state: np.ndarray, gate: np.ndarray) -> np.ndarray:
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
    array([[0],
           [1],
           [0],
           [0]])
    >>> two = apply(one, SWAP())
    >>> Measure.one(two)
    2
    >>> two
    array([[0],
           [0],
           [1],
           [0]])


    """

    return np.matmul(gate, state)
