#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>


import pytorchqbit

README =  "# pypytorchqbit" + "\n"
README += "Quantum bit and the usual gates in torch tensors straight from the Wikipedia."
README += '\n## apply'+ "\n" + pytorchqbit.apply.__doc__
README += '\n## Quantum bit definitions\n'
README += '\n### Zero'+ "\n" + pytorchqbit.Zero.__doc__
README += '\n### One'+ "\n" + pytorchqbit.One.__doc__
README += '\n### Plus'+ "\n" + pytorchqbit.Plus.__doc__
README += '\n### Minus'+ "\n" + pytorchqbit.Minus.__doc__
README += '\n### Measure'+ "\n" + pytorchqbit.Measure.__doc__
README += '\n### Combine'+ "\n" + pytorchqbit.Combine.__doc__
README += '\n### equal'+ "\n" + pytorchqbit.equal.__doc__
README += '\n## Quantum gates\n'
README += '\n### Identity'+ "\n" + pytorchqbit.Identity.__doc__
README += '\n### H'+ "\n" + pytorchqbit.H.__doc__
README += '\n### PauliX'+ "\n" + pytorchqbit.PauliX.__doc__
README += '\n### PauliY'+ "\n" + pytorchqbit.PauliY.__doc__
README += '\n### PauliZ'+ "\n" + pytorchqbit.PauliZ.__doc__
README += '\n### Phase'+ "\n" +  pytorchqbit.Phase.__doc__
README += '\n### R'+ "\n" + pytorchqbit.R.__doc__
README += '\n### CNOT'+ "\n" + pytorchqbit.CNOT.__doc__
README += '\n### CPauliZ'+ "\n" + pytorchqbit.CPauliZ.__doc__
README += '\n### SWAP'+ "\n" + pytorchqbit.SWAP.__doc__
README += '\n## Pauli group\n'
README += '\n### P1'+ "\n" + pytorchqbit.P1.__doc__
README += '\n### Pn'+ "\n" + pytorchqbit.Pn.__doc__
README += '\n## Stabilizer codes\n'
README += '\n### S_5_1_3'+ "\n" + pytorchqbit.S_5_1_3.__doc__


with open('README.md', 'wt') as readme_file:
    readme_file.write(README)