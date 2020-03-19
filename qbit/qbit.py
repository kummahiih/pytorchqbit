"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

import numpy as np
import random
from category_equations import from_operator, debug
import functools

"""
Representation of single qubit basic states and operations for self study
Author: Pauli Rikula
"""

# some dark python magic for custom function representation
class _reprwrapper(object):
    def __init__(self, repr, func):
        self._repr = repr
        self._func = func
        functools.update_wrapper(self, func)
    def __call__(self, *args, **kw):
        return self._func(*args, **kw)
    def __repr__(self):
        return self._repr(self._func)

# some dark python magic for custom function representation
def _withrepr(reprfun):
    def _wrap(func):
        return _reprwrapper(reprfun, func)
    return _wrap

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


class Circuit:
    """
    Unresponsible and misleading circuit representation which hides the essential details and can not simulate the 
    quantum catalystic behaviour needed by the quantum inteference.

    >>> I, O, C, G, CG = Circuit().operators()

    I is circuit identity element
    O is circuit termiinal element
    C is circuit connector
    G is Gate
    Cg is connected gate ( Cg(x) == C(G(x)))

    Example: circuit, which always collapses to True
    >>> m = G(Measure)
    >>> c = CG(One) * C(m)
    >>> c
    C(|1>_2) * C(M_1)

    This makes the connections between the gates
    >>> c.evaluate()

    Then collapse the circuit
    >>> m.evaluate()
    True

    This circuit collapses always to False
    >>> m = G(Measure)
    >>> c = CG(Zero) * CG(H) * CG(PauliZ) * CG(H) * CG(PauliX) * C(m)
    >>> c
    C(|0>_4) * C(H_5) * C(Z_6) * C(H_7) * C(X_8) * C(M_3)

    >>> c.evaluate()
    >>> m.evaluate()
    False

    The underlying machinery lets you to make simpple manipulations with the circuits

    >>> a = G(Measure)
    >>> b = G(One)
    >>> C(a) * C(b) == C(a) * C(b)
    True

    """
    def __init__(self):
        self.g_cnt = 0

    def operators(self1):
        class BitGate:
            def __init__(self, item):
                self1.g_cnt += 1
                self._item = item
                self.source = None
                self.sink = None
                self.value = None
                self.id = self1.g_cnt
                
            def __repr__(self): return "%s_%d" % (self._item.__repr__(), self.id)

            def __lt__(self, other):
                return self.id.__lt__(other.id)

            def connect(self, other):
                assert other.source is None
                assert self.sink is None
                other.source = self
                self.sink = other

            def evaluate(self):
                if self.value is not None:
                    return self.value
                if self.source is None:
                    return self._item()
                if self._item is Measure:
                    return Measure(self.source.evaluate())
                self.value = np.matmul(self._item(), self.source.evaluate())
                return self.value
    
        I, O, C = from_operator(lambda a,b: a.connect(b))
        def Cg(i):
            return C(BitGate(i))

        return I, O, C, BitGate, Cg



if __name__ == "__main__":
    import doctest
    doctest.testmod()

