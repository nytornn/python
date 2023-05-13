import math
import numpy as np

while True:
    equation = input("Enter an equation to calculate: ")
    result = np.array(eval(equation))
    print("Result: ", result)