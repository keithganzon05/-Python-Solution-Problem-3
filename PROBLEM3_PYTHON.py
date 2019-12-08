import numpy as np

print("Enter the values 0f the matrix (Left to Right) : ") 
datapoints = list(map(int, input().split())) 
rows = int(len(datapoints)/2)
col = 2

datap = len(np.array(datapoints).reshape(rows, col))
datap1 = np.array(datapoints).reshape(rows, col)


def PROBLEM3_PYHTON(datap):
    if datap >= 10:
        print('Polynomials are limited from 1st to 10th degree. Try Again!')
        

    for n in range(datap):
        PXi = np.polyfit(datap1[:,0], datap1[:,1], n)
        polval = np.polyval(PXi, datap1[:,0])
        PYi = np.linalg.norm(datap1[:,1] - polval)
        vector = [n,PYi]
    
        if n==0:
            identifier = vector
    
        elif identifier[1] >= vector[1]:
            deg = vector[0]

    PYi = np.polyfit(datap1[:,0], datap1[:,1], deg)
    print('Coefficients: ',np.around(PYi,2))
    
PROBLEM3_PYHTON(datap)