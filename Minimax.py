#Minimax Algorithm
#Jack Betcher
#Traverses a binary tree of scores 
def miniMax(depth, index, isMax, scores, limit):
    if depth == limit:
        return scores[index]
    elif isMax:
        return max(miniMax(depth+1, index*2, False, scores, limit),
                       miniMax(depth+1, index*2+1, False, scores, limit))
    else:
        return min(miniMax(depth+1, index*2, True, scores, limit),
                       miniMax(depth+1, index*2+1, True, scores, limit))
def log2(n):
    if n==1:
        return 0
    else:
        return 1+log2(n/2)

#number of elements in scores must be a power of two (binary tree) 
scores = [3,5,2,9,12,5,23,23]
n = len(scores)
h = log2(n)
print miniMax(0 , 0, True, scores, h)
