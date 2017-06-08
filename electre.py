#Tugas Decision Support System
#Fajar Ulin Nuha 
#Natasha CS

import numpy as np

def rank(array, reverse=False):
    mult = 1 if reverse else -1
    temp = (mult*array).argsort()
    ranks = np.empty(len(array), int)
    ranks[temp] = np.arange(len(array))
    return ranks

#alt_index = ["Civic", "Saturn", "Escort", "Miata"]
#A = np.array([(4, 3, 5), (2, 5, 4), (1, 2, 3), (3, 3, 2)], dtype= float)
alt_index = ["Paket A", "Paket B", "Paket C", "Paket D", "Paket E"]
A = np.array([(3,3,3,2), (4,4,3,3), (4,5,3,2), (3,4,4,1), (4,5,4,2)], dtype= float)
m = len(A[0])
n = len(A)
W = np.array([(2,4,3,1)], dtype = float)
W_i = W * np.identity(m)

#step 2
smsq = np.sum(A**2, axis=0)
rss = np.sqrt(smsq)
R = A/rss

#step 3
V = R.dot(W_i)

#step 4
IC = []
ID = []
for i, alt in enumerate(V):
    tempC = alt <= V
    tempC[i] = np.zeros(len(alt))
    tempD = alt > V
    tempD[i] = np.zeros(len(alt))
    IC.append(tempC)
    ID.append(tempD)

#step 5
C = np.empty([n,n])
for i,alt in enumerate(IC):
    arr = alt * W
    C[:,i] = np.sum(arr, axis=1)

#step 6
D = np.empty([n,n], dtype=float)
for i,alt in enumerate(ID):
    diff = np.abs(V - V[i])
    diff[i] = 1.0
    diffD = diff * alt
    D[:,i] = np.max(diffD, axis=1)\
    / np.max(diff, axis=1)

#step 7
Cbar = np.sum(C) / (n * (n-1))
F = C >= Cbar

#step 8
Gbar = np.sum(D) / (n * (n-1))
G = D >= Gbar

#step 9
AggM = F & G
Agg = np.sum(AggM, axis=1)

DiffM = C - D
CDiff = DiffM > DiffM.T
S = np.sum(CDiff, axis=1)

NC = np.sum(C, axis=1) - np.sum(C, axis=0)
ND = np.sum(D, axis=1) - np.sum(D, axis=0)
print 'Agg', [alt_index[i] for i in rank(Agg)]
print 'S', [alt_index[i] for i in rank(S)]
print 'NC', [alt_index[i] for i in rank(NC)]
print 'ND', [alt_index[i] for i in rank(ND, reverse=True)]
