# pyqbit

## Circuit

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

    
## Zero
Qubit that evaluates as zero every single time

    >>> Zero()
    |0>
    >>> Zero()()
    array([[1],
           [0]])
    >>> Measure().MeasureOne(Zero()())
    False

    
## One
Qubit that evaluates as one every single time

    >>> One()
    |1>
    >>> One()()
    array([[0],
           [1]])
    >>> Measure().MeasureOne(One()())
    True
    
    
## Plus
Qubit that evaluates as one and zero evenly

    >>> Plus()
    |+>
    >>> Plus()()
    array([[0.70710678],
           [0.70710678]])
    
    
## Minus
Qubit that evaluates as one and zero evenly

    >>> Minus()
    |->
    >>> Minus()()
    array([[ 0.70710678],
           [-0.70710678]])
    
    
## Measure

    >>> isinstance(Measure(), Measure)
    True

    
## Combine
Use Kronecker product of two arrays to combine qubits.

    >>> Combine(Zero()(),Zero()())
    array([[1],
           [0],
           [0],
           [0]])

    >>> Combine(One()(), Combine(Zero()(),Zero()()))
    array([[0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0]])

    
## Identity
Identity gate
    
    >>> Identity()
    Identity
    >>> Identity()()
    array([[1, 0],
           [0, 1]])

    
## H
Hadamard gate

    >>> H()
    H
    >>> H()()
    array([[ 0.70710678,  0.70710678],
           [ 0.70710678, -0.70710678]])

    
## PauliX
Pauli X gate

    >>> PauliX()
    X
    >>> PauliX()()
    array([[0, 1],
           [1, 0]])

    
## PauliY
Pauli Y gate

    >>> PauliY()
    Y
    >>> PauliY()()
    array([[ 0.+0.j, -0.-1.j],
           [ 0.+1.j,  0.+0.j]])

    
## PauliZ
Pauli Z gate

    >>> PauliZ()
    Z
    >>> PauliZ()()
    array([[ 0,  1],
           [ 0, -1]])

    
## Phase
Phase (S, P) gate

    >>> Phase()
    P
    >>> Phase()()
    array([[1.+0.j, 0.+0.j],
           [0.+0.j, 0.+1.j]])

    
## R
R is the custom phase shift gate

    >>> from math import pi
    >>> R(pi/4)
    R(0.7853981633974483)
    >>> R(pi/4)()
    array([[1.        +0.j        , 0.        +0.j        ],
           [0.        +0.j        , 0.70710678+0.70710678j]])

    
## CNOT
CNOT is the Controlled Not gate (CX)

    >>> CNOT()
    CX
    >>> CNOT()()
    array([[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0]])

    
## CPauliZ
CPauliZ is the Controlled Pauli Z gate (CZ)

    >>> CPauliZ()
    CZ
    >>> CPauliZ()()
    array([[ 1,  0,  0,  0],
           [ 0,  1,  0,  0],
           [ 0,  0,  1,  0],
           [ 0,  0,  0, -1]])

    
## SWAP
SWAP is the qbit swap gate

    >>> SWAP()
    SWAP
    >>> SWAP()()
    array([[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 1]])

    