#This factorization takes the form A = U S V^t
#where U is an m × m orthogonal matrix, V is an n × n orthogonal matrix, and S is an
#m × n matrix whose only nonzero elements lie along the main diagonal
import numpy as np
def svd(A):
   # here m=5
    #n=3
    #S matrix
    #here AA^t eigen value needed which are diagonal element of S in decreasing order
    E,F=np.linalg.eigh(np.dot(np.transpose(A),A))
    #E eigen value V eigen vector
    Ed=np.argsort(E)[::-1]
    E=E[Ed]
    F=F[:,Ed]
    S=np.zeros((5,3))
    for i in range(3):
        S[i,i]=np.sqrt(E[i])
    #V matrix
    V=np.zeros((3,3))
    for i in range(3):
        V[:,i]=F[:,i]           #ith coloum is eigen vector of AA^t
    #U matrix
    U=np.zeros((5,5))
    for i in range(3):
        U[:,i]=np.dot(A,V[:,i])/S[i,i]
    for j in range(3,5):
        U[:,j]=np.zeros(5)
        U[:,j][0]=1
        c=np.zeros(5)
        for k in range(j):
            c=c+np.dot(np.transpose(U[:,k]),U[:,j])*U[:,k]
        U[:,j]=U[:,j]-c
        U[:,j]=U[:,j]/np.linalg.norm(U[:,j])
    return U,S,np.transpose(V)
A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
RR=svd(A)
print(RR)
    
        
    
