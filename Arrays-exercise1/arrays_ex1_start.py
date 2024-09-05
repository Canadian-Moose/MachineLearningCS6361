#! /usr/bin/env python3
# Natasha Rovelli
# CS6361 Array - Exercise 1
# Due: 9.4.24

import numpy as np

# 1
def is_square(X):
    # get the shape 
    shape = X.shape
    # return false if 1 dimension 
    if len(shape) < 1: return False
    # compare width to other dimensions
    # return false if don't match 
    w = shape[0]
    for dim in shape:
        if dim != w: return False
    # everything matches
    return True

# 2
def max_loop(X):
    # initialize negative infinity 
    mx = -np.inf
    # loop through outer array
    for a in X:
        # find max of each inner array
        # replace if larger than mx
        mx = max(np.max(a), mx)
    return mx

# 3
def argmax_loop(X):
    # initialize index to 0 and max to first entry
    amx = 0
    mx = X[0]
    # iterate through length of array
    for i in range(1, len(X)):
        # if greater, update variables 
        if X[i] > mx:
            mx = X[i]
            amx = i
    return amx

# 4
def sum_loop(X):
    # initialize sum
    s = 0
    # find the shape 
    shape = X.shape
    # multiply dimensions for num elements
    dim = np.prod(shape)
    # reshape to single dimension 
    a = X.reshape(dim,)
    # sum the array 
    s = np.sum(a)
    return s

# 5
def diagonal(X):
    # find the shape of X
    shape = X.shape
    # slice the diagnonal
    d = X[[i for i in range(shape[0])],[i for i in range(shape[0])]]
    return d

# 6
def count_digits(X):
    count = np.zeros(10,dtype=np.int16)
    # find the shape 
    shape = X.shape
    # multiply dimensions for num elements
    dim = np.prod(shape)
    # reshape to single dimension 
    a = X.reshape(dim,)
    # remove negative numbers 
    a = a[a >= 0]
    # remove numbers over 9
    a = a[a <= 9]
    # count the digits
    count = np.bincount(a)
    return count

# 7
def dot(x1,x2):
    # Multiply the arrays 
    mult = x1 * x2
    # sum the result 
    dot = np.sum(mult)
    return dot

# 8
def euclidean_dist(x1,x2):
    # Numpy euclidian distance 
    dist = np.linalg.norm(x1 - x2)
    return dist

# 9
def manhattan_dist(x1,x2):
    # calculate absolute value of distances 
    diff = np.abs(x1 - x2)
    # sum the result 
    dist = np.sum(diff)
    return dist

# 10
def accuracy(p,y):
    # compare for difference 
    comp = p == y
    # divide the correct by the total 
    acc = len(comp[comp == True]) / len(comp)
    return acc

# 11
def mse(p,y):
    # Numpy Mean Squared Error 
    mse = np.square(np.subtract(y, p)).mean()
    return mse

# 12
def select_features(X,n):
    # calculate variance 
    var = np.var(X, axis=0)
    # get the indexs of highest variance 
    sel = np.argsort(var)[-n:]
    return X[:, sel]

# 13
def select_instances(X,f,t):
    # select instances of feature f that are > t
    return X[X[:, f] > t]

# 14
def nearest_neighbor(X,x):
    # initialize index and distance
    nn, dist = 0, np.inf
    # for each index compare distance 
    for i in range(0, len(X)):
        d = euclidean_dist(X[i], x)
        # replace dist and index if closer 
        if d < dist:
            dist, nn = d, i
    return nn

# 15
def nearest_neighbors(X1,X2):
    # reshape X1 for broadcasting 
    x = X1.reshape(X1.shape[0], 1, X1.shape[1])
    # calculate the differences between rows
    # stored in 3rd axis 
    dist = np.linalg.norm(x - X2, axis=2)
    # find the nearest neighbor for each row 
    d = np.argmin(dist, axis=0)
    return np.array(d)

#------------------------------------------------------------#

if __name__ == "__main__":

    print('Question 1')
    A1 = np.array([[10, 70, 40], [ 0, 80, 60], [50, 30, 20]])
    A2 = np.arange(20).reshape(4,5)
    A3 = np.arange(16).reshape(4,4)
    A4 = np.arange(25).reshape(5,5)
    A5 = np.arange(16).reshape(4,4,1)
    A6 = np.arange(22)
    for X in [A1,A2,A3,A4,A5,A6]:
        print('X =')
        print(X)
        print('is_square(X) = ',is_square(X))

    print('\nQuestion 2')
    np.random.seed(2)
    for i in range(2):
        X = np.random.randint(0,100,20)
        print('X =')
        print(X)
        print('max_loop(X) = ',max_loop(X))
        X = np.random.randint(0,100,size=(3,8))
        print('X =')
        print(X)
        print('max_loop(X) = ',max_loop(X))
        X = np.random.randint(0,100,size=(2,3,6))
        print('X =')
        print(X)
        print('max_loop(X) = ',max_loop(X))

    print('\nQuestion 3')
    np.random.seed(3)
    for i in range(4):
        X = np.random.randint(-20,21,5+2*i)
        print('X =',X)
        print('argmax_loop(X) = ',argmax_loop(X))

    print('\nQuestion 4')
    np.random.seed(4)
    for i in range(1):
        X = np.random.randint(0,5,5)
        print('X = ',X)
        print('sum_loop(X) = ',sum_loop(X))
        X = np.random.randint(0,5,size=(3,4))
        print('X =')
        print(X)
        print('sum_loop(X) = ',sum_loop(X))
        X = np.random.randint(0,5,size=(2,3,4))
        print('X =')
        print(X)
        print('sum_loop(X) = ',sum_loop(X))

    print('\nQuestion 5')
    np.random.seed(5)
    for i in range(2,6):
        X = np.random.randint(0,10,size = (i,i))
        print('X =')
        print(X)
        print('diagonal(X) =',diagonal(X))

    print('\nQuestion 6')
    np.random.seed(6)
    A1 = np.random.randint(0,10,size = 12)
    A2 = np.random.randint(-9,10,size = 12)
    A3 = np.random.randint(-15,16,size = (4,8))
    A4 = np.random.randint(-15,16,size = (4,3,2))
    for X in [A1,A2,A3,A4]:
        print('X =')
        print(X)
        print('count_digits(X) = ',count_digits(X))

    print('\nQuestion 7')
    np.random.seed(7)
    for i in range(2,5):
        x1 = np.random.randint(-3,4,size = i)
        x2 = np.random.randint(-3,4,size = i)
        print(f'dot({x1},{x2}) = {dot(x1,x2)}')

    print('\nQuestion 8')
    np.random.seed(8)
    for i in range(2,5):
        x1 = np.random.randint(-3,4,size = i)
        x2 = np.random.randint(-3,4,size = i)
        print(f'euclidean_dist({x1},{x2}) = {euclidean_dist(x1,x2):6.4f}')

    print('\nQuestion 9')
    np.random.seed(9)
    for i in range(2,5):
        x1 = np.random.randint(-3,4,size = i)
        x2 = np.random.randint(-3,4,size = i)
        print(f'manhattan_dist({x1},{x2}) = {manhattan_dist(x1,x2)}')

    print('\nQuestion 10')
    np.random.seed(10)
    for i in range(3,7):
        p = np.random.randint(0,2,size = i)
        y = np.random.randint(0,2,size = i)
        y[i-1] = p[i-1]
        print(f'accuracy({p},{y}) = {accuracy(p,y):6.4f}')

    print('\nQuestion 11')
    np.random.seed(11)
    for i in range(2,5):
        p = np.random.randint(0,4,size = i)
        y = np.random.randint(0,4,size = i)
        print(f'mse({p},{y}) = {mse(p,y):6.4f}')

    print('\nQuestion 12')
    np.random.seed(12)
    X = np.random.randint(0,10,size = (10,5))
    print('X =')
    print(X)
    print('feature variances:',np.var(X,axis=0))
    for n in range(1,6):
        print(f'select_features(X,{n}) = \n{select_features(X,n)}')

    print('\nQuestion 13')
    np.random.seed(13)
    X = np.random.randint(0,10,size = (8,5))
    print('X =')
    print(X)
    thr = [3.5, 5.5, 6.5, 7.5, 8.5]
    for f in range(5):
        t = thr[f]
        print(f'select_instances(X,{f},{t}) = \n{select_instances(X,f,t)}')

    print('\nQuestion 14')
    np.random.seed(14)
    for s in [2,3]:
        X = np.random.randint(0,10,size = (5,s))
        print('X =')
        print(X)
        for i in range(5):
            x = np.random.randint(0,10,size = s)
            print(f'nearest_neighbor(X,{x}) = {nearest_neighbor(X,x)}')

    print('\nQuestion 15')
    np.random.seed(15)
    for s in [2,3]:
        X1 = np.random.randint(0,10,size = (5+s,s))
        print('X1 =')
        print(X1)
        X2 = np.random.randint(0,10,size = (5,s))
        print('X2 =')
        print(X2)
        print(f'nearest_neighbors(X1,X1) = {nearest_neighbors(X1,X1)}')
        print(f'nearest_neighbors(X1,X2) = {nearest_neighbors(X1,X2)}')



'''
Expected Output:

Question 1
X =
[[10 70 40]
 [ 0 80 60]
 [50 30 20]]
is_square(X) =  True
X =
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
is_square(X) =  False
X =
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
is_square(X) =  True
X =
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
is_square(X) =  True
X =
[[[ 0]
  [ 1]
  [ 2]
  [ 3]]

 [[ 4]
  [ 5]
  [ 6]
  [ 7]]

 [[ 8]
  [ 9]
  [10]
  [11]]

 [[12]
  [13]
  [14]
  [15]]]
is_square(X) =  False
X =
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21]
is_square(X) =  False

Question 2
X =
[40 15 72 22 43 82 75  7 34 49 95 75 85 47 63 31 90 20 37 39]
max_loop(X) =  95
X =
[[67  4 42 51 38 33 58 67]
 [69 88 68 46 70 95 83 31]
 [66 80 52 76 50  4 90 63]]
max_loop(X) =  95
X =
[[[79 49 39 46  8 50]
  [15  8 17 22 73 57]
  [90 62 83 96 43 32]]

 [[26  8 76 10 40 34]
  [60  9 70 86 70 19]
  [56 82  1 68 40 81]]]
max_loop(X) =  96
X =
[61 70 97 18 84 90 87 22 43 52 74 72 90 99 91 96 16 55 21 43]
max_loop(X) =  99
X =
[[93 80 40 70 74 37 59 17]
 [15 30 77 26 39 63 20 22]
 [59 49 27  0 62 40 58 92]]
max_loop(X) =  93
X =
[[[36 63 75 50 73  7]
  [49 82  1 79 91 96]
  [49 40 46 59 73 78]]

 [[94 95 32 16 21 43]
  [58 98 21 49 63 83]
  [92 51 97  8 86 88]]]
max_loop(X) =  98

Question 3
X = [  4 -17 -12 -20   1]
argmax_loop(X) =  0
X = [ -1 -10 -10   1  18  12   0]
argmax_loop(X) =  4
X = [  9  19  -6   6  -3   6   2 -18 -18]
argmax_loop(X) =  1
X = [-19   6 -15  20  13   9   4 -13  13  -5  17]
argmax_loop(X) =  3

Question 4
X =  [2 1 0 0 2]
sum_loop(X) =  5
X =
[[1 2 4 1]
 [0 4 2 4]
 [2 4 3 0]]
sum_loop(X) =  27
X =
[[[1 0 2 0]
  [1 2 2 0]
  [0 3 2 1]]

 [[0 4 3 2]
  [3 2 1 2]
  [1 0 1 1]]]
sum_loop(X) =  34

Question 5
X =
[[3 6]
 [6 0]]
diagonal(X) = [3 0]
X =
[[9 8 4]
 [7 0 0]
 [7 1 5]]
diagonal(X) = [9 0 5]
X =
[[7 0 1 4]
 [6 2 9 9]
 [9 9 1 2]
 [7 0 5 0]]
diagonal(X) = [7 2 1 0]
X =
[[0 4 4 9 3]
 [2 4 6 9 3]
 [3 2 1 5 7]
 [4 3 1 7 3]
 [1 9 5 7 0]]
diagonal(X) = [0 4 1 7 0]

Question 6
X =
[9 3 4 0 9 1 9 1 4 1 8 2]
count_digits(X) =  [1 3 1 1 2 0 0 0 1 3]
X =
[ 3 -7 -4  6  9  2 -4 -4  8 -5 -4  7]
count_digits(X) =  [0 0 1 1 0 0 1 1 1 1]
X =
[[-13 -13   4   6  13  13  -4  10]
 [-10   3  11  -1   8  -7 -10  -9]
 [ -5  11  -5 -12   6  -4 -14   3]
 [-12   7  -6  12  -6   9   1  -5]]
count_digits(X) =  [0 1 0 2 1 0 2 1 1 1]
X =
[[[-12  -8]
  [-11  -4]
  [  9 -14]]

 [[ -3   3]
  [-11 -14]
  [  0 -10]]

 [[  0  14]
  [  6  12]
  [ -9 -14]]

 [[ -6  13]
  [  1 -10]
  [ -5  -7]]]
count_digits(X) =  [2 1 0 1 0 0 1 0 0 1]

Question 7
dot([ 1 -2],[3 0]) = 3
dot([ 0  1 -2],[ 3 -3 -2]) = 1
dot([ 3 -1 -1 -3],[ 3  1 -3  1]) = 8

Question 8
euclidean_dist([0 1],[-2 -2]) = 3.6056
euclidean_dist([ 2 -1 -3],[ 0 -3 -3]) = 2.8284
euclidean_dist([ 2  2  1 -2],[ 0 -1  0  1]) = 4.7958

Question 9
manhattan_dist([3 1],[3 2]) = 1
manhattan_dist([ 3 -3  0],[ 3  2 -2]) = 7
manhattan_dist([ 3  1  0 -3],[-1 -2 -3  2]) = 15

Question 10
accuracy([1 1 0],[1 0 0]) = 0.6667
accuracy([1 0 1 1],[0 1 1 1]) = 0.5000
accuracy([0 1 0 0 0],[0 0 1 0 0]) = 0.6000
accuracy([1 1 0 0 1 0],[0 1 0 0 0 0]) = 0.6667

Question 11
mse([1 3],[0 3]) = 0.5000
mse([1 3 1],[0 1 3]) = 3.0000
mse([2 0 1 0],[0 1 0 1]) = 1.7500

Question 12
X =
[[6 1 2 3 3]
 [0 6 1 4 5]
 [9 2 6 0 5]
 [8 2 9 3 4]
 [3 1 7 0 2]
 [6 2 0 4 6]
 [9 0 0 9 8]
 [9 6 1 8 4]
 [0 4 1 5 5]
 [3 4 5 5 0]]
feature variances: [11.61  3.96  9.56  7.69  4.36]
select_features(X,1) =
[[6]
 [0]
 [9]
 [8]
 [3]
 [6]
 [9]
 [9]
 [0]
 [3]]
select_features(X,2) =
[[2 6]
 [1 0]
 [6 9]
 [9 8]
 [7 3]
 [0 6]
 [0 9]
 [1 9]
 [1 0]
 [5 3]]
select_features(X,3) =
[[3 2 6]
 [4 1 0]
 [0 6 9]
 [3 9 8]
 [0 7 3]
 [4 0 6]
 [9 0 9]
 [8 1 9]
 [5 1 0]
 [5 5 3]]
select_features(X,4) =
[[3 3 2 6]
 [5 4 1 0]
 [5 0 6 9]
 [4 3 9 8]
 [2 0 7 3]
 [6 4 0 6]
 [8 9 0 9]
 [4 8 1 9]
 [5 5 1 0]
 [0 5 5 3]]
select_features(X,5) =
[[1 3 3 2 6]
 [6 5 4 1 0]
 [2 5 0 6 9]
 [2 4 3 9 8]
 [1 2 0 7 3]
 [2 6 4 0 6]
 [0 8 9 0 9]
 [6 4 8 1 9]
 [4 5 5 1 0]
 [4 0 5 5 3]]

Question 13
X =
[[2 0 0 6 2]
 [4 9 3 4 2]
 [6 5 9 4 2]
 [0 3 5 3 6]
 [5 1 2 8 8]
 [6 2 4 5 7]
 [3 5 8 3 8]
 [5 1 8 1 7]]
select_instances(X,0,3.5) =
[[4 9 3 4 2]
 [6 5 9 4 2]
 [5 1 2 8 8]
 [6 2 4 5 7]
 [5 1 8 1 7]]
select_instances(X,1,5.5) =
[[4 9 3 4 2]]
select_instances(X,2,6.5) =
[[6 5 9 4 2]
 [3 5 8 3 8]
 [5 1 8 1 7]]
select_instances(X,3,7.5) =
[[5 1 2 8 8]]
select_instances(X,4,8.5) =
[]

Question 14
X =
[[8 6]
 [7 9]
 [6 0]
 [8 9]
 [7 6]]
nearest_neighbor(X,[0 7]) = 4
nearest_neighbor(X,[4 0]) = 2
nearest_neighbor(X,[6 4]) = 4
nearest_neighbor(X,[5 5]) = 4
nearest_neighbor(X,[8 5]) = 0
X =
[[9 8 7]
 [3 4 8]
 [1 6 0]
 [9 5 6]
 [2 1 7]]
nearest_neighbor(X,[8 3 1]) = 3
nearest_neighbor(X,[9 1 5]) = 3
nearest_neighbor(X,[8 9 5]) = 0
nearest_neighbor(X,[3 9 9]) = 1
nearest_neighbor(X,[4 2 0]) = 2

Question 15
X1 =
[[8 5]
 [5 7]
 [0 7]
 [5 6]
 [1 7]
 [0 4]
 [9 7]]
X2 =
[[5 3]
 [6 8]
 [2 1]
 [1 0]
 [5 2]]
nearest_neighbors(X1,X1) = [0 1 2 3 4 5 6]
nearest_neighbors(X1,X2) = [3 1 5 5 3]
X1 =
[[2 1 8]
 [5 6 9]
 [2 8 6]
 [8 8 3]
 [4 7 2]
 [0 5 7]
 [3 8 5]
 [3 1 0]]
X2 =
[[8 7 5]
 [8 1 2]
 [8 3 1]
 [3 7 2]
 [7 2 0]]
nearest_neighbors(X1,X1) = [0 1 2 3 4 5 6 7]
nearest_neighbors(X1,X2) = [3 7 3 4 7]
'''
