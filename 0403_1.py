# Regression(Linear/Logistic)
# (X, Y), Theta*X, Logistix(Thdta*X), Softmax
# Logit -> X=log p/(1-p)
#         Theta*X = log p/(1-p)
#         p = Bernouii
#         mu(x) -> Logistic
# X = { x1, x2, x3, x4 .., xn }
# Theta = { t1, t2, t3, ... , tn}
#      -> x1t1 + x2t2 + ... + xntn
# x1*x2
# -----> x2
# d c1



import numpy as np

import matplotlib.pyplot as plt

X = np.linspace(np.pi, np.pi*2, 100)
Y = np.cos(X)

plt.plot(X, Y)

X = np.linspace(np.pi, np.pi*2, 100)
Y = np.cos(X)
Y[np.cos(X) > 0] = 1

plt.plot(X, Y)

# h = 1e-5
# theta = np.random.rand(2)
# X = np.c_[np.ones(len(X)), X]
# epoch = 10000

# for _ in range(epoch):
#     X.dot(theta)
#     break

X = np.linspace(np.pi, np.pi*2, 100)
Y = np.cos(X)
Y[np.cos(X) > 0] = 1
X = np.c_[np.ones(len(X)), X]

h = 1e-5
theta = np.random.rand(2)
epoch = 10000

SE = lambda truey, predy : (truey - predy) **2

print(theta)

for _ in range(epoch):
#    for x, t in xip(X, Y): #Extreme
    theta = theta + h*2*X.T.dot(Y - X.dot(theta))
    break

plt.scatter(X[:,1], Y)
plt.plot(X[:,1], X.dot(theta))
theta

np.sum(SE(Y, X.dot(theta))), np.mean(SE(Y, X.dot(theta)))

X = np.linspace(np.pi, np.pi*2, 100)
Y = np.cos(X)
Y[np.cos(X) > 0] = 1
X = np.c_[np.ones(len(X)), X]

h = 1e-5
theta = np.random.rand(2)
epoch = 20000

SE = lambda truey, predy : (truey - predy) **2

print(theta)
print(np.sum(SE(Y, X.dot(theta))), np.mean(SE(Y, X.dot(theta))))

for _ in range(epoch):
    theta = theta + h*2*X.T.dot(Y - X.dot(theta))



trainingSet = [(1, 'Chinese Bejing Chinese', 'yes'), (2, 'Chinese Chinese Shanghai', 'yes'), (3, 'Chinese Macao', 'yes'), (4, 'Tokyo Japan Chinese', 'no')]
testSet = [(5, 'Chinese Chinese Chinese Tokyo Japan')]

# Vectorize (Boolean)

[d[1].lower().split() for d in trainingSet]

V = list(set('\n'.join([d[1] for d in trainingSet]).lower().split()))

V

X = np.zeros((4, len(V)))

for i, d in enumerate(trainingSet):
    for t in d[1].lower().split():
        if t in V:
            j = V.index(t)
            X[i, j] = 1
X



Y = np.zeros((4,))

for i, d in enumerate(trainingSet):
    if d[2] == 'yes':
        Y[i] = 1
Y

newX = np.c_[np.ones(len(X)), X]

h = 1e-5
theta = np.random.rand(newX.shape[-1])
epoch = 20000

SE = lambda truey, predy : (truey - predy) **2

history = list()

print(theta)
print(np.sum(SE(Y, newX.dot(theta))), np.mean(SE(Y, newX.dot(theta))))

for i, _ in enumerate(range(epoch)):
    theta = theta + h*2*newX.T.dot(Y - newX.dot(theta))

    if i % 1000 == 0:
        history.append(np.mean(SE(Y, newX.dot(theta))))

plt.plot(history)

T = np.zeros((len(testSet), len(V)))

for i, d in enumerate(testSet):
    for t in d[1].lower().split():
        if t in V:
            j = V.index(t)
            T[i, j] = 1
T

np.c_[np.ones((1,)), T].dot(theta) > .5



# vectorize -> orthogonal
# ; boolean, count, tf-idf, weight..



s = set()
for d in trainingSet:
    print(d)
    for w in d[1].lower().split():
        s.add(w)
        print(s)

import sys
print(sys.version)

!Python --version



X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[1]])

def dataLoader(d, n=1):
    for i in range(len(d)//n):
        yield d[i*n:i*n+n]

[_ for _ in dataLoader(X, 1)]

[_ for _ in dataLoader(X, 3)]

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[1]])

def dataLoader(x, y, n=1):
    for i in range(len(x)//n):
        yield (x[i*n:i*n+n], y[i*n:i*n+n])

W = np.random.rand(X.shape[-1], Y.shape[-1])

def dataLoader(x, y, n=1):

    _x = np.random.permutation(x)
    _y = np.random.permutation(y)

    for i in range(len(x)//n):
        yield (_x[i*n:i*n+n], _y[i*n:i*n+n])

[_ for _ in dataLoader(X, Y, n=1)]

np.array([1,1]) + 1

def dataLoader(x, y, n=1):

#    _x = np.random.permutation(x)
#    _y = np.random.permutation(y)

    for i in range(len(x)//n):
        yield (x[i*n:i*n+n], y[i*n:i*n+n])

[_ for _ in dataLoader(X, Y, n=1)]

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.mean(dLoss)*1
        dW = x.T @ dLoss / N
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

X@W+B > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.mean(dLoss)*1
        dW = x.T @ dLoss
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.mean(dLoss)*1
        dW = x.T @ dLoss
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
#        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.sum(dLoss)*1
        dW = x.T @ dLoss
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.sum(dLoss)*1
        dW = x.T @ dLoss
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
#        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

N = 4

W = np.random.rand(X.shape[-1]+1, Y.shape[-1])

lr = 1e-5
epoch = 100000

J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        x = np.c_[np.ones(N), x]
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dW = x.T @ dLoss
        W = W - lr*dW

    if epoch % 100 == 0:
#        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, np.c_[np.ones(len(X)), X]@W)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
np.c_[np.ones(len(X)), X]@W > .5



def dataLoader(x, y, n=1):
    # Shuffling
#     [i for i in range(len(x))]
    D = np.random.permutation(np.c_[x,y])

    # Batch
    for i in range(len(x)//n):
        yield (D[i*n:i*n+n,:-1], D[i*n:i*n+n,-1:])

[_ for _ in dataLoader(X, Y, n=1)]

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.mean(dLoss)*1
        dW = x.T @ dLoss / N
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

X@W+B > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.mean(dLoss)*1
        dW = x.T @ dLoss
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.mean(dLoss)*1
        dW = x.T @ dLoss
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
#        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.sum(dLoss)*1
        dW = x.T @ dLoss
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

W = np.random.rand(X.shape[-1], Y.shape[-1])
B = np.random.rand(Y.shape[-1])

lr = 1e-5
epoch = 100000

N = 4
J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W + B
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dB = np.sum(dLoss)*1
        dW = x.T @ dLoss
        B = B- lr*dB
        W = W - lr*dW

    if epoch % 100 == 0:
#        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, X@W+B)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

N = 4

W = np.random.rand(X.shape[-1]+1, Y.shape[-1])

lr = 1e-5
epoch = 100000

J = lambda y, _y : (y-_y)**2

acc = list()
loss = list()

for i in range(epoch):
    for x, y in dataLoader(X, Y, 4):
        x = np.c_[np.ones(N), x]
        # x.shape
        # w.shape
        # x * W
        Yhat = x @ W
        dLoss = -2*(y- Yhat)  # Yhat-Y = -(Y-Yhat)
        dW = x.T @ dLoss
        W = W - lr*dW

    if epoch % 100 == 0:
#        acc.append(sum([y == _y for y, _y in zip (Y, X@W+B)]))
        loss.append(np.sum(J(Y, np.c_[np.ones(len(X)), X]@W)))

plt.plot(acc)
plt.plot(loss)
plt.ylim(0,1)

plt.plot(loss)
X@W > .5

