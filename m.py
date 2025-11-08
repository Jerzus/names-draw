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
    shuffled_names = random.sample(names, len(names))
    pairs = list(zip(names, shuffled_names))
    return pairs

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