import argparse
import random as r
import numpy as np

import pymp 

def parallelMultiplyMatrix(A:list,B:list,num_threads=2):
    row = len(A)  
    col = len(B[0]) 

    wresult = pymp.shared.array((row,col),dtype=int)

    with pymp.Parallel(num_threads=num_threads) as p:
        for i in p.range(0, row):
            for j in p.range(0, col):
                for k in p.range(0, col):
                    wresult[i][j] += A[i][k] * B[k][j]
    return wresult


def multiplyMatrix(A:list,B:list):
    w = [[0 for i in range(len(A))] for j in range(len(B))]

    row = len(A)
    col = len(B[0])

    for i in range(row):
        for j in range(col):
            for k in range(row):
                w[i][j] += A[i][k] * B[k][j]
    return w

def genRandomMatrix(size=1024,seed=10):

    w = [[r.randint(1,seed) for i in range(size)] for j in range(size)]

    return w


def genMatrix(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values.
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix

def genMatrix2(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values.
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix

def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix.
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ' , end='')
        print('')

def writeToFile(matrix, fileName):
    """
    Writes a matrix out to a file.
    """

    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')

def readFromFile(fileName):
    """
    Reads a matrix from a file.
    """

    matrix = []

    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)

    return matrix

def main():
    """
    Used for running as a script
    """

    parser = argparse.ArgumentParser(description=
        'Generate a 2d matrix and save it to  a file.')
    parser.add_argument('-s', '--size', default=1024, type=int,
        help='Size of the 2d matrix to generate')
    parser.add_argument('-v', '--value', default=1, type=int,
        help='The value with which to fill the array with')
    parser.add_argument('-f', '--filename',
        help='The name of the file to save the matrix in (optional)')

    args = parser.parse_args()

    mat = genMatrix(args.size, args.value)

    if args.filename is not None:
        print(f'Writing matrix to {args.filename}')
        writeToFile(mat, args.filename)

        print(f'Testing file')
        printSubarray(readFromFile(args.filename))
    else:
        printSubarray(mat)

if __name__ == '__main__':
    # execute only if run as a script
    main()
