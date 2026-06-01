import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity

def run_naive_simulation():
    # 1. User Inputs
    try:
        p = float(input("Enter the physical error probability (p, between 0 and 1): "))
        if not (0.0 <= p <= 1.0):
            raise ValueError("Probability must be between 0 and 1.")
        
        trials = int(input("Enter the number of Monte Carlo trials (e.g., 1000): "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # 2. Setup Registers
    data_reg = QuantumRegister(3, name='data')
    ancilla_reg = QuantumRegister(2, name='ancilla')
    syn_reg = ClassicalRegister(2, name='syndrome')
    
    # Configure simulator to density matrix method
    simulator = AerSimulator(method='density_matrix')
    total_naive_fidelity = 0.0
    
    print(f"\nSimulating {trials} trials for p = {p}... Please wait.")
    
    # 3. Monte Carlo Loop
    for _ in range(trials):
        qc = QuantumCircuit(data_reg, ancilla_reg, syn_reg)
        
        # --- STAGE 1: ENCODING ---
        qc.h(data_reg[0]) 
        qc.cx(data_reg[0], data_reg[1])
        qc.cx(data_reg[0], data_reg[2])
        
        # --- STAGE 2: NOISE INJECTION ---
        for qubit in data_reg:
            if np.random.rand() <= p:
                qc.x(qubit)
                
        # --- STAGE 3: SYNDROME EXTRACTION ---
        qc.cx(data_reg[0], ancilla_reg[0])
        qc.cx(data_reg[1], ancilla_reg[0])
        
        qc.cx(data_reg[1], ancilla_reg[1])
        qc.cx(data_reg[2], ancilla_reg[1])
        
        qc.measure(ancilla_reg[0], syn_reg[0])
        qc.measure(ancilla_reg[1], syn_reg[1])
        
        # --- STAGE 4: RECOVERY OPERATION ---
        with qc.if_test((syn_reg, 1)):   
            qc.x(data_reg[0])
        with qc.if_test((syn_reg, 3)):   
            qc.x(data_reg[1])
        with qc.if_test((syn_reg, 2)):   
            qc.x(data_reg[2])
            
        # --- STAGE 5: NAIVE FIDELITY EVALUATION ---
        ideal_circuit = QuantumCircuit(data_reg, ancilla_reg)
        ideal_circuit.h(data_reg[0])
        ideal_circuit.cx(data_reg[0], data_reg[1])
        ideal_circuit.cx(data_reg[0], data_reg[2])
        ideal_global_sv = Statevector.from_instruction(ideal_circuit)
        
        qc.save_density_matrix()
        
        result = simulator.run(qc, shots=1).result()
        
        simulated_global_rho = result.data(0)['density_matrix']
        
        trial_fidelity = state_fidelity(ideal_global_sv, simulated_global_rho)
        total_naive_fidelity += trial_fidelity

    # 4. Output Average Result
    avg_naive_fidelity = total_naive_fidelity / trials
    print("\n--- Simulation Results ---")
    print(f"Physical Error Probability (p): {p}")
    print(f"Total Trials Executed: {trials}")
    print(f"Average Naive Sim. Fidelity (Global): {avg_naive_fidelity:.4f}")
    print("--------------------------")

if __name__ == "__main__":
    run_naive_simulation()
