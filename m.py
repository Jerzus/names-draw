import random
import sys
import os
import tempfile
import subprocess
import time

def read_names_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            names = [line.strip() for line in file]
        return names
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def shuffle_and_assign(names):
    """
    Shuffle and assign names meeting these conditions:
    - Condition 0: At least 3 persons
    - Condition 1: No self-assignment (person cannot be assigned to themselves)
    - Condition 2: No mutual pairs (if A->B, then B cannot ->A)
    
    APPROACHES:
    
    1. REJECTION SAMPLING (Simple but potentially slow):
       - Randomly shuffle until all conditions are met
       - Check: no self-assignments AND no mutual pairs
       - Pros: Simple, guarantees uniform distribution
       - Cons: Can be slow for large groups, worst-case infinite loop
    
    2. DERANGEMENT + MUTUAL PAIR CHECK (Better):
       - Generate a derangement (permutation with no fixed points)
       - Check for mutual pairs, if found, swap to break them
       - Pros: Faster, guarantees no self-assignments
       - Cons: May need multiple attempts if many mutual pairs
    
    3. ITERATIVE CONSTRUCTION (Most reliable):
       - Build assignments one by one, avoiding invalid choices
       - Track used assignments and forbidden pairs
       - Pros: Always terminates, deterministic approach
       - Cons: More complex, may need backtracking
    
    4. CYCLE-BASED APPROACH (Elegant):
       - Create cycles of length >= 3 (ensures no mutual pairs)
       - Break cycles into assignments
       - Pros: Mathematically elegant, guarantees conditions
       - Cons: More complex implementation
    
    5. SWAP-BASED FIX (Pragmatic):
       - Start with any derangement
       - Detect and fix mutual pairs by swapping assignments
       - Pros: Fast, simple to understand
       - Cons: May need multiple passes
    """
    # Validate condition 0: at least 3 persons
    if len(names) < 3:
        raise ValueError("Need at least 3 persons for assignment")
    
    # APPROACH 5: Swap-based fix (pragmatic and efficient)
    # Step 1: Create a derangement (no self-assignments)
    shuffled = list(names)
    max_attempts = 1000
    attempts = 0
    while attempts < max_attempts:
        random.shuffle(shuffled)
        # Check if it's a derangement (no fixed points)
        if all(names[i] != shuffled[i] for i in range(len(names))):
            break
        attempts += 1
    
    if attempts >= max_attempts:
        raise RuntimeError("Failed to generate derangement after many attempts")
    
    # Step 2: Fix mutual pairs by swapping
    assignment = {names[i]: shuffled[i] for i in range(len(names))}
    
    # Find and fix mutual pairs
    while True:
        mutual_found = False
        for person_a in names:
            person_b = assignment[person_a]
            # Check if A->B and B->A (mutual pair)
            if assignment.get(person_b) == person_a:
                mutual_found = True
                # Find a person C (not A or B) to swap with
                for person_c in names:
                    if person_c != person_a and person_c != person_b:
                        person_d = assignment[person_c]
                        # Swap: A->B becomes A->D, C->D becomes C->B
                        # This breaks the mutual pair A<->B
                        assignment[person_a] = person_d
                        assignment[person_c] = person_b
                        break
                break
        
        if not mutual_found:
            break
    
    return [(name, assignment[name]) for name in names]

def display_pairs(pairs):
    for pair in pairs:
        print(f'{pair[0]} -> {pair[1]}')

def main():
        input_file_path = input("Enter the complete path of the file with names: ")
        if not os.path.exists(input_file_path):
            print(f"The path you provided does not exist and hence, creating a temporary file '{input_file_path}' for you.", end=' ')
            sys.exit(1)
        else:
            names = read_names_from_file(input_file_path)

    pairs = shuffle_and_assign(names)

    print("Secret Santa pairs have been shuffled and assigned:")
    display_pairs(pairs)

if __name__ == "__main__":
    main()