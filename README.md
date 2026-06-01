# Quantum-Error-Correction-Simulator

A Monte Carlo simulation pipeline for the 3-qubit bit-flip Quantum Error Correction (QEC) architecture built using Python and Qiskit. This repository accompanies the data and methodology presented in our paper.

## Features
- Fully authentic Monte Carlo error injection across a noisy quantum channel.
- Compares Physical Fidelity, Theoretical Fidelity, Naive Statevector Fidelity, and Corrected Sim. Fidelity.
- Avoids inline simulator-quirk bugs by correctly implementing partial trace isolation on the data registers.

## Prerequisites
Ensure you have Python and the required quantum libraries installed:
```bash
pip install qiskit numpy
