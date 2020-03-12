import numpy as np
A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
y0=np.array([1,0,0])
x0=np.array([0,1,0])



def F(A,x_0,y_0,i):
    g=np.dot(y0,np.linalg.matrix_power(A,i+1))
    h=np.dot(y0,np.linalg.matrix_power(A,i))
    p=np.dot(g,x0)
    q=np.dot(h,x0)
    return p/q
i=1
while i>=1:
    x=F(A,x0,y0,i+1)/F(A,x0,y0,i)-1
    if abs(x)<0.01:
        break
    else:
        i=i+1
k=i
        

eigenvalue=F(A,x0,y0,k+1)
eigenvector=np.dot(np.linalg.matrix_power(A,k+1),x0)

print(eigenvalue)
print(eigenvector)