#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>



if __name__ == '__main__':
    import doctest
    import qbit

    # by importing these here, there might be some import errors left..
    globs = {
        'Zero': qbit.Zero,
        'One': qbit.One,
        'Plus': qbit.Plus,
        'Minus': qbit.Minus,
        'Measure': qbit.Measure,
        'Combine': qbit.Combine,
        'Identity': qbit.Identity,
        'H': qbit.H,
        'PauliX': qbit.PauliX,
        'PauliY': qbit.PauliY,
        'PauliZ': qbit.PauliZ,
        'Phase':  qbit.Phase,
        'R': qbit.R,
        'CNOT': qbit.CNOT,
        'CPauliZ': qbit.CPauliZ,
        'SWAP': qbit.SWAP,
        'apply': qbit.apply,
        'equal': qbit.equal,
        'P1': qbit.P1,
        'Pn': qbit.Pn
    }
    doctest.testfile(filename="pauli_group.py", module_relative=True, package=qbit, globs=globs)
    doctest.testfile(filename="qbit.py", module_relative=True, package=qbit, globs=globs)
    doctest.testfile(filename="gate.py", module_relative=True, package=qbit, globs=globs)
    doctest.testfile(filename="__init__.py", module_relative=True, package=qbit, globs=globs)
