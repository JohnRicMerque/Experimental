import numpy as np

values = np.loadtxt('values.txt', delimiter=',', ndmin= 2)

nrows,ncols = values.shape
print(f"Found scores of {nrows} student(s) on {ncols} subject(s)")

for r in range(nrows):
    for c in range(ncols):
        score = values[r][c]
        if score < 50:
            print(f"Student #{r+1} fails subject #{c+1} with score {score}")