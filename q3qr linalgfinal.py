import numpy as np
#QR decomposition
a=np.array([[5,-2],[-2,8]])
f= np.linalg.qr(a)
print(f)
#eigh
g= np.linalg.eigh(a)
print(g)
#SVD
b=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
h=np.linalg.svd(b)
print(h)