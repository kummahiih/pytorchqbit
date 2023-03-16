# pypytorchqbit
Quantum bit and the usual gates in torch tensors straight from the Wikipedia.
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
    tensor([[0.+0.j],
            [1.+0.j],
            [0.+0.j],
            [0.+0.j]])
    >>> two = apply(one, SWAP())
    >>> Measure.one(two)
    2
    >>> two
    tensor([[0.+0.j],
            [0.+0.j],
            [1.+0.j],
            [0.+0.j]])


    
## Quantum bit definitions

### Zero
Qubit that evaluates as zero every single time

    >>> Zero
    |0>
    >>> Zero()
    tensor([[1.+0.j],
            [0.+0.j]])
    >>> Measure.one(Zero())
    0

    
### One
Qubit that evaluates as one every single time

    >>> One
    |1>
    >>> One()
    tensor([[0.+0.j],
            [1.+0.j]])
    >>> Measure.one(One())
    1

    
### Plus
Qubit that evaluates as one and zero evenly

    >>> Plus
    |+>
    >>> Plus()
    tensor([[0.7071+0.j],
            [0.7071+0.j]])

    
### Minus
Qubit that evaluates as one and zero evenly

    >>> Minus
    |->
    >>> Minus()
    tensor([[ 0.7071+0.j],
            [-0.7071+0.j]])

    
### Measure
Simulates the measure process of the qubit

    >>> Measure.one(One())
    1

    
### Combine
Use Kronecker product of two arrays to combine qubits.

    >>> Combine(Zero(),Zero())
    tensor([[1.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j]])


    >>> from functools import reduce
    >>> reduce(Combine, [One(), Zero(), Zero()])
    tensor([[0.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j],
            [1.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j]])
    >>> Combine(One(), Zero(), Zero())
    tensor([[0.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j],
            [1.+0.j],
            [0.+0.j],
            [0.+0.j],
            [0.+0.j]])

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
    tensor([[1.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j]])
    >>> Identity(2)
    tensor([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])


    
### H
Hadamard gate

    >>> H
    H
    >>> H()
    tensor([[ 0.7071+0.j,  0.7071+0.j],
            [ 0.7071+0.j, -0.7071+0.j]])

    
### PauliX
Pauli X gate

    >>> PauliX
    X
    >>> PauliX()
    tensor([[0.+0.j, 1.+0.j],
            [1.+0.j, 0.+0.j]])

    
### PauliY
Pauli Y gate

    >>> PauliY
    Y
    >>> PauliY()
    tensor([[0.+0.j, -0.-1.j],
            [0.+1.j, 0.+0.j]])

    
### PauliZ
Pauli Z gate

    >>> PauliZ
    Z
    >>> PauliZ()
    tensor([[ 1.+0.j,  0.+0.j],
            [ 0.+0.j, -1.+0.j]])

    
### Phase
Phase (S, P) gate

    >>> Phase
    P
    >>> Phase()
    tensor([[1.+0.j, 0.+0.j],
            [0.+0.j, 0.+1.j]])

    
### R
R is the custom phase shift gate

    >>> from math import pi
    >>> R(pi/4)
    R(0.7853981633974483)
    >>> R(pi/4)()
    tensor([[1.0000+0.0000j, 0.0000+0.0000j],
            [0.0000+0.0000j, 0.7071+0.7071j]])


    
### CNOT
CNOT is the Controlled Not gate (CX)

    >>> CNOT
    CX
    >>> CNOT()
    tensor([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j],
            [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]])

    
### CPauliZ
CPauliZ is the Controlled Pauli Z gate (CZ)

    >>> CPauliZ
    CZ
    >>> CPauliZ()
    tensor([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
            [ 0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j],
            [ 0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
            [ 0.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]])

    
### SWAP
SWAP is the qbit swap gate

    >>> SWAP
    SWAP
    >>> SWAP()
    tensor([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])

    
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

    >>> P2 = Pn(2)
    >>> P2
    P2
    >>> p2 = list(P2())
    >>> len(p2)
    1024
    >>> p2[0]
    tensor([[-1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
            [ 0.+0.j, -1.+0.j,  0.+0.j,  0.+0.j],
            [ 0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j],
            [ 0.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]])

    >>> p2[1]
    tensor([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
            [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])


p2 is a group, so these apply:

Associativy:

    >>> import random
    >>> all_products = [apply(a,b) for a in p2 for b in p2]
    >>> all([ any([equal(p, c) for c in p2]) for p in random.sample(all_products, 1000)])
    True

Identity:

    >>> equal(Identity(2), p2[1])
    True
    >>> i2 = p2[1]
    >>> all([ equal(apply(a, i2), a) for a in p2])
    True

Inverse element:

    >>> all([ any([equal(apply(a, b), i2) for b in p2]) for a in random.sample(p2, 20)])
    True

    
## Stabilizer codes

### S_5_1_3
S_5_1_3 error correction code encodes one logical qubit into five physical qubits.
    S_5_1_3 protects against an arbitrary single-qubit error and it has code distance three codes.

    >>> S_5_1_3
    S_5_1_3

    >>> S_5_1_3.g1()
    tensor([[ 0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j],
            [ 1.+0.j,  0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j, -1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j]])

    >>> S_5_1_3.g2()
    tensor([[ 1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j],
            [ 0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j, -1.+0.j,  1.+0.j,  0.+0.j]])

    >>> S_5_1_3.g3()
    tensor([[ 0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
            [ 1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j, -1.+0.j]])

    >>> S_5_1_3.g4()
    tensor([[ 1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j],
            [ 0.+0.j, -1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j,  1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]])

    