# pyqbit
Quantum bit and the usual gates in numeric forms straight from the Wikipedia.
## apply
Apply gate to a state

For example this chain evaluates to zero:

    >>> from functools import reduce
    >>> s = reduce( apply, [Zero(), H(), PauliZ(), H(), PauliX()])
    >>> Measure.one(s)
    0

Swap places of a bit

    >>> one = Combine(Zero(), One())
    >>> Measure.one(one)
    1
    >>> one
    array([[0],
           [1],
           [0],
           [0]])
    >>> two = apply(one, SWAP())
    >>> Measure.one(two)
    2
    >>> two
    array([[0],
           [0],
           [1],
           [0]])


    
## Quantum bit definitions

### Zero
Qubit that evaluates as zero every single time

    >>> Zero
    |0>
    >>> Zero()
    array([[1],
           [0]])
    >>> Measure.one(Zero())
    0

    
### One
Qubit that evaluates as one every single time

    >>> One
    |1>
    >>> One()
    array([[0],
           [1]])
    >>> Measure.one(One())
    1

    
### Plus
Qubit that evaluates as one and zero evenly

    >>> Plus
    |+>
    >>> Plus()
    array([[0.70710678],
           [0.70710678]])

    
### Minus
Qubit that evaluates as one and zero evenly

    >>> Minus
    |->
    >>> Minus()
    array([[ 0.70710678],
           [-0.70710678]])

    
### Measure
Simulates the measure process of the qubit

    >>> Measure.one(One())
    1

    
### Combine
Use Kronecker product of two arrays to combine qubits.

    >>> Combine(Zero(),Zero())
    array([[1],
           [0],
           [0],
           [0]])


    >>> from functools import reduce
    >>> reduce(Combine, [One(), Zero(), Zero()])
    array([[0],
           [0],
           [0],
           [0],
           [1],
           [0],
           [0],
           [0]])

Each row represents the probability of getting it's index's value as a result

    >>> Measure.one(Combine(Zero(),Zero()))
    0

    >>> Measure.one( Combine(One(), Combine(Zero(),Zero())) )
    4

    
### equal
The equal is a test if the two qubit states

    >>> equal(One(), One())
    True
    >>> equal(One(), Zero())
    False

    
## Quantum gates

### Identity
Identity gate

    >>> Identity
    Identity
    >>> Identity()
    array([[1, 0],
           [0, 1]])

    
### H
Hadamard gate

    >>> H
    H
    >>> H()
    array([[ 0.70710678,  0.70710678],
           [ 0.70710678, -0.70710678]])

    
### PauliX
Pauli X gate

    >>> PauliX
    X
    >>> PauliX()
    array([[0, 1],
           [1, 0]])

    
### PauliY
Pauli Y gate

    >>> PauliY
    Y
    >>> PauliY()
    array([[ 0.+0.j, -0.-1.j],
           [ 0.+1.j,  0.+0.j]])

    
### PauliZ
Pauli Z gate

    >>> PauliZ
    Z
    >>> PauliZ()
    array([[ 1,  0],
           [ 0, -1]])

    
### Phase
Phase (S, P) gate

    >>> Phase
    P
    >>> Phase()
    array([[1.+0.j, 0.+0.j],
           [0.+0.j, 0.+1.j]])

    
### R
R is the custom phase shift gate

    >>> from math import pi
    >>> R(pi/4)
    R(0.7853981633974483)
    >>> R(pi/4)()
    array([[1.        +0.j        , 0.        +0.j        ],
           [0.        +0.j        , 0.70710678+0.70710678j]])

    
### CNOT
CNOT is the Controlled Not gate (CX)

    >>> CNOT
    CX
    >>> CNOT()
    array([[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0]])

    
### CPauliZ
CPauliZ is the Controlled Pauli Z gate (CZ)

    >>> CPauliZ
    CZ
    >>> CPauliZ()
    array([[ 1,  0,  0,  0],
           [ 0,  1,  0,  0],
           [ 0,  0,  1,  0],
           [ 0,  0,  0, -1]])

    
### SWAP
SWAP is the qbit swap gate

    >>> SWAP
    SWAP
    >>> SWAP()
    array([[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 1]])

    
## Pauli group

### P1
P1 is the First Pauli Group done from the cross product of
[-1, 1, -1j, 1j] and [Identity(), PauliX(), PauliY(), PauliZ()]


    >>> P1
    P1
    >>> p1 = list(P1())
    >>> len(p1)
    16
    >>> equal(p1[0], -1*Identity())
    True
    >>> equal(p1[1], 1*Identity())
    True
    >>> equal(p1[2], -1j*Identity())
    True
    >>> equal(p1[3], 1j*Identity())
    True
    >>> equal(p1[15], 1j*PauliZ())
    True

p1 is a group, so these apply:

Associativy:

    >>> all([ any([equal(apply(a,b), c) for c in P1()]) for a in P1() for b in P1()])
    True

Identity:

    >>> equal( Identity(), p1[1])
    True

    >>> all([ equal(apply(a, Identity()), a) for a in P1()])
    True

Inverse element:

    >>> all([ any([equal(apply(a, b), Identity()) for b in P1()]) for a in P1() ])
    True

    
### Pn
Pn is the n:th Pauli group instance

    >>> p2 = Pn(2)
    >>> p2
    P2
    >>> len(list(p2()))
    256

    