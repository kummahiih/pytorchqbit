"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>

   Numeric representations of quantum bits and gates
"""


__all__ = [
   'Zero',
   'One',
   'Plus',
   'Minus',
   'Measure',
   'Circuit',
   'H',
   'PauliX',
   'PauliY',
   'PauliZ',
   'Phase',
   'R',
   'CNOT',
   'CPauliZ',
   'SWAP',
   'Identity',
   'Combine']

from .qbit import Zero, One, Plus, Minus, Measure, Combine
from .gate import Identity, H, PauliX, PauliY, PauliZ, Phase, R, CNOT, CPauliZ, SWAP
from .circuit import Circuit
