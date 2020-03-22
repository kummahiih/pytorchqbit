"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

import numpy as np
from category_equations import from_operator, debug

from .gate import H, Identity, PauliX, PauliZ
from .qbit import One, Zero, Plus, Minus, Measure


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
    >>> m = G(Measure())
    >>> c = CG(One()) * C(m)
    >>> c
    C(|1>_2) * C(M_1)

    This makes the connections between the gates
    >>> c.evaluate()

    Then collapse the circuit
    >>> m.evaluate()
    True

    This circuit collapses always to False
    >>> m = G(Measure())
    >>> c = CG(Zero()) * CG(H()) * CG(PauliZ()) * CG(H()) * CG(PauliX()) * C(m)
    >>> c
    C(|0>_4) * C(H_5) * C(Z_6) * C(H_7) * C(X_8) * C(M_3)

    >>> c.evaluate()
    >>> m.evaluate()
    False

    The underlying machinery lets you to make simpple manipulations with the circuits

    >>> a = G(Measure())
    >>> b = G(One())
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
                if isinstance(self._item, Measure):
                    return self._item.MeasureOne(self.source.evaluate())
                self.value = np.matmul(self._item(), self.source.evaluate())
                return self.value
    
        I, O, C = from_operator(lambda a,b: a.connect(b))
        def Cg(i):
            return C(BitGate(i))

        return I, O, C, BitGate, Cg


