import numpy as np 
import matplotlib.pyplot as plt
from sklearn import svm
from matplotlib import style

style.use("ggplot")

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])

y=[0,1,0,1,0,1]

# Baseamos o nosso sistema linear pelos quais numero sao maiores e quais sao os menores
clf = svm.SVC(kernel='linear', C = 1.0)
# Kerner= linear indica qual seria o tipo, de linha grafica que indica a divisao do grafico
clf.fit(X,y)
# Predicts sao tentativas de  tentar identificar o valor
print(clf.predict([[0.58,0.76]]))
print(clf.predict([[10.58,10.76]]))

# Coeficiente necessarios para demonstrar o valor de divisao
w = clf.coef_[0]
print(w)
# Learning rate, controla o quao rapido esse modelo sera adaptado para o problem,
# nesse caso ele so e utilizado para fazer a divisao entre 1 e 0
a = -w[0] / w[1]
# linspace sera o limite entre a linhas, nesse caso ja sabemos quale pq controlamos o array sendo o minimo 0, e o maximo 12
# para descobrilos so avalar por np
xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]
# Todas essa mecanicas sao necessaria para visualizar graficos, elas geralmente nao sao utilizadas com modelos svc, 
#pq elas tem excesso de features.
# plot do coeficiente
h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c = y)
plt.show()