#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""
Representation of single qubit basic states
"""

import random
import torch
import numpy as np


def convert_to_complex(lits_form:list) -> torch.Tensor:
    """
    >>> convert_to_complex([[1, 0], [0, 0+1j]])
    tensor([[1.+0.j, 0.+0.j],
            [0.+0.j, 0.+1.j])
    """
    arr = np.array(lits_form)
    real_part = np.real(arr)
    imaginary_part = np.imag(arr)
    real_tensor = torch.tensor(real_part, dtype=torch.float32)
    imaginary_tensor = torch.tensor(imaginary_part, dtype=torch.float32)
    return torch.complex(real_tensor, imaginary_tensor)