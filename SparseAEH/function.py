import numpy as np
from numpy.linalg import norm

def RBF_kernel(X, l):
    X = np.array(X)
    Xsq = np.sum(np.square(X), 1)
    R2 = -2. * np.dot(X, X.T) + (Xsq[:, None] + Xsq[None, :])
    return np.exp(-R2 / (2 * l ** 2))

def linear_kernel(X):
    K = np.dot(X, X.T)
    return K / K.max()

def dis(a,b):
    return norm(a-b)

def nearest_neighbours(spatial,k):  #spatial:N*2
    spatial = np.array(spatial)
    N = spatial.shape[0]
    neighbours = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(neighbours[i]) == 0:
                neighbours[i].append((j,dis(spatial[i],spatial[j])))
            else:
                if max(np.abs(spatial[i,0]-spatial[j,0]),np.abs(spatial[i,1]-spatial[j,1])) < neighbours[i][-1][1] or len(neighbours[i])<k:
                    d = dis(spatial[i],spatial[j])
                    ins = k
                    if d < neighbours[i][-1][1] or len(neighbours[i])<k:
                        for index,neighbour in enumerate(neighbours[i]):
                            if neighbour[1] > d:
                                ins = index
                                break
                    if ins == k:
                        neighbours[i].append((j,d))
                    else:
                        neighbours[i].insert(ins,(j,d))
                        if len(neighbours[i])>k:
                            neighbours[i].pop()
    return neighbours

spatial = np.array([[0,0],[2,2],[3,3],[10,10]])
neighbours = nearest_neighbours(spatial,2)
print(neighbours)