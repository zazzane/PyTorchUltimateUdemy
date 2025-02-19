import os

# Path to the requirements file
requirements_file = 'requirements_py3.txt'

# Read the requirements file
with open(requirements_file, 'r') as file:
    lines = file.readlines()

# Add each dependency to the Poetry project
for line in lines:
    dependency = line.strip()
    if dependency:
        os.system(f'poetry add {dependency}')