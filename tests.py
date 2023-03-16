#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>



if __name__ == '__main__':
    import doctest
    import pytorchqbit

    # by importing these here, there might be some import errors left..
    globs = {
        'convert_to_complex': pytorchqbit.convert_to_complex,
        'Zero': pytorchqbit.Zero,
        'One': pytorchqbit.One,
        'Plus': pytorchqbit.Plus,
        'Minus': pytorchqbit.Minus,
        'Measure': pytorchqbit.Measure,
        'Combine': pytorchqbit.Combine,
        'Identity': pytorchqbit.Identity,
        'H': pytorchqbit.H,
        'PauliX': pytorchqbit.PauliX,
        'PauliY': pytorchqbit.PauliY,
        'PauliZ': pytorchqbit.PauliZ,
        'Phase':  pytorchqbit.Phase,
        'R': pytorchqbit.R,
        'CNOT': pytorchqbit.CNOT,
        'CPauliZ': pytorchqbit.CPauliZ,
        'SWAP': pytorchqbit.SWAP,
        'apply': pytorchqbit.apply,
        'equal': pytorchqbit.equal,
        'P1': pytorchqbit.P1,
        'Pn': pytorchqbit.Pn,
        'S_5_1_3': pytorchqbit.S_5_1_3
        }
    doctest.testfile(filename="stabilizer.py", module_relative=True, package=pytorchqbit, globs=globs)
    doctest.testfile(filename="pauli_group.py", module_relative=True, package=pytorchqbit, globs=globs)
    doctest.testfile(filename="qbit.py", module_relative=True, package=pytorchqbit, globs=globs)
    doctest.testfile(filename="gate.py", module_relative=True, package=pytorchqbit, globs=globs)
    doctest.testfile(filename="__init__.py", module_relative=True, package=pytorchqbit, globs=globs)
