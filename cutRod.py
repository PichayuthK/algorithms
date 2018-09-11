rod = [1, 5, 8, 12, 14, 16, 17, 20, 24, 27 ]
rod.insert(0,0)
n = len(rod)

import sys
sys.setrecursionlimit(100000)

counter = 0

def cutrod(L):
    global counter 
    counter = counter + 1
    if(L <= 0):
        return 0
    else:
        mx = 0
        for i in range(1,n):
            if(i <= L):
                result = rod[i] + cutrod(L-i)
                mx = max(mx, result)
        return mx

print cutrod(n-1)
print 'Recursion round: ', counter