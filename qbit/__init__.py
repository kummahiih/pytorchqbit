"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

"""
   Numeric representations of quantum bits and gates and tools to make simple qbit simulations
"""


__all__ = [
   'Zero',
   'One',
   'Plus',
   'Minus',
   'Measure',
   'H',
   'PauliX',
   'PauliY',
   'PauliZ',
   'Phase',
   'R',
   'CNOT',
   'CPauliZ',
   'SWAP',
   'Apply',
   'Identity',
   'Combine']

from .qbit import Zero, One, Plus, Minus, Measure, Combine
from .gate import Identity, H, PauliX, PauliY, PauliZ, Phase, R, CNOT, CPauliZ, SWAP, Apply
