import numpy as np
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([[1,2,3,4,5]])
x=np.zeros(5)
w=1.25
cs=np.array([[7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]])
D=np.diag(A)
R=A-np.diagflat(D)
U=np.triu(R)
L=np.tril(R)
LL=np.dot(1.25,L)
bb=np.dot(1.25,b)
DD=np.dot(-0.25,D)
UU=np.dot(1.25,U)
i=1
#while i>=1:
   # x=(np.dot((DD+UU),x)+bb)/(D-LL)
    #if np.amax(abs(cs-x))<0.01:
     #   break
    #i=i+1
#print(x)
    
#this code is running in infinite loop so another method required.
while i>=1:
    for j in range(5):
        r=b[0,j]-np.dot(x,R[j])-D[j]*x[j]
        x[j]=x[j]+w*(r/D[j])
    if np.amax(abs(x-cs))<0.01:
        break
    i=i+1
print(x)
print(i)

         


    
    
    