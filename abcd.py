"""File to print a random integer"""
# Import packages
import numpy as np

if __name__ == '__main__':
    high_num = int(input("Enter upper limit of number"))
    if high_num > 0:
        a = np.random.randint(0, high_num)
        print(f"Number is {a}")
    else:
        raise ValueError("Upper limit should be greater than 0")
