from qiskit import QuantumCircuit, QuantumRegister

a = QuantumRegister(1, name="a")
b = QuantumRegister(1, name="b")
o = QuantumRegister(1, name="o")
circuit = QuantumCircuit(a, b, o)

circuit.ccx(a, b, o)
circuit.cx(a, b)

from qiskit.visualization import circuit_drawer

circuit_drawer(circuit, filename="half_adder.pdf", output="latex")