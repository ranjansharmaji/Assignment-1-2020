import numpy as np
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([[1,2,3,4,5]])
x=np.zeros(5)
#correct solution
cs=np.array([[7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]])
i=1
while i>=1:
    D=np.diag(A)
    R=A-np.diagflat(D)
    for j in range(5):
        x[j]=(b[0,j]-np.dot(x,R[j]))/D[j]
    if np.amax(abs(cs-x))<0.01:
        break
    i=i+1
print(x)
print(i)
 