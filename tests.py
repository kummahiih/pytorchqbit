"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""


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
        'Circuit': qbit.Circuit,
        'H': qbit.H,
        'PauliX': qbit.PauliX,
        'PauliZ': qbit.PauliZ,
        'Identity': qbit.Identity

    }
    
    doctest.testfile(filename="qbit.py", module_relative=True, package=qbit, globs=globs)
    doctest.testfile(filename="gate.py", module_relative=True, package=qbit, globs=globs)
    doctest.testfile(filename="circuit.py", module_relative=True, package=qbit, globs=globs)
    doctest.testfile(filename="__init__.py", module_relative=True, package=qbit, globs=globs)
