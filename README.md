# Waterflow

Waterflow is a Python script that simulates water flow through a matrix. 
Given an initial position in the matrix, the script calculates the path of the water as it flows downhill, following the steepest descent until it reaches a local minimum.

## How to run the program

Replace [x_position] and [y_position] with the coordinates of the starting position in the matrix.

- python waterflow.py -x [x_position] -y [y_position]

Example:
- python waterflow.py -x 2 -y 1

## Output

The script prints two matrices:

The original input matrix.
The result matrix, showing the path of the water as it flows downhill.
