#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>


"""
   Torch tensor representations of quantum bits and gates and tools to make simple qbit simulations
"""


__all__ = [
    'convert_to_complex',
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
    'apply',
    'Identity',
    'Combine',
    'equal',
    'P1',
    'Pn',
    'S_5_1_3'
    ]
from .convert import convert_to_complex
from .qbit import Zero, One, Plus, Minus, Measure, Combine, equal
from .gate import Identity, H, PauliX, PauliY, PauliZ, Phase, R, CNOT, CPauliZ, SWAP, apply
from .pauli_group import P1, Pn
from .stabilizer import S_5_1_3