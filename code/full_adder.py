from qiskit import QuantumCircuit, QuantumRegister

a = QuantumRegister(1, name="a")
b = QuantumRegister(1, name="b")
cin = QuantumRegister(1, name="cin")
o = QuantumRegister(1, name="o")

circuit = QuantumCircuit(a, b, cin, o)

circuit.ccx(a, b, o)
circuit.cx(a, b)
circuit.ccx(b, cin, o)
circuit.cx(b, cin)
circuit.cx(a, b)

from qiskit.visualization import circuit_drawer

circuit_drawer(circuit, filename="full_adder.pdf", output="latex")