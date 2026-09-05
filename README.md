# Quantum-Error-Correction-Simulator

A Monte Carlo simulation pipeline for the 3-qubit bit-flip Quantum Error Correction (QEC) architecture built using Python and Qiskit. This repository accompanies the data and methodology presented in our paper.

> **A note on this project:** This was one of my first projects in quantum physics and quantum computing. The problem is fairly straightforward, but it was assigned to me by my research mentor as an early research exercise. Looking back, it was a useful introduction to quantum error correction, Qiskit, Monte Carlo methods, and working with noisy quantum systems.

## Features
- Fully authentic Monte Carlo error injection across a noisy quantum channel.
- Compares Physical Fidelity, Theoretical Fidelity, Naive Statevector Fidelity, and Corrected Sim. Fidelity.
- Avoids inline simulator-quirk bugs by correctly implementing partial trace isolation on the data registers.

## Prerequisites
Ensure you have Python and the required quantum libraries installed:
```bash
pip install qiskit numpy
