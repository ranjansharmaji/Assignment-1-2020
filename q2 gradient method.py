import numpy as np
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([[1,2,3,4,5]])
x=np.zeros(5)

cs=np.array([[7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]])
D=np.diag(A)
R=A-np.diagflat(D)
U=np.triu(R)
L=np.tril(R)
#So for any vector v not 0 we have g(x + ˆtv) < g(x) unless 
#<v, b − Ax> = 0,, in which case g(x) = g(x + ˆtv) and <x, y>= x^t*t
#so v=b-np.dot(x,A)
#t(k)=<V(k),b − Ax(k−1)>/<v(k), Av(k)>
i=1
while i>=1:
    v=b-np.dot(x,A)
    f=np.dot(v,A)
    t=np.dot(v,np.transpose(v))/np.dot(v,np.transpose(f))
    x=x+t*v
    if np.amax(abs(x-cs))<0.01:
         break
    i=i+1
print(x)
print(i)
     
     
     


    