#So precisa disso, e tu ja pode comecar.  Aviso: Scikit e para os modelos mais tradicionais,
#keras e para modelos mais inusitados e tensorflow e deep neural tem nada a ver
import matplotlib.pyplot as plt
# Datasets= conjunto de dados svm, support vector machine, basicamente maquinba que define os clusters google!
from sklearn import datasets
from sklearn import svm


# Isso daqui carrega os datasets
digits= datasets.load_digits()

#print(digits.data)
#Exemplo de digitos
#Digits .target seria o numero que eles estao tentando adivinha qual seria
#logo isso seria um supervised learning porque voce direciona a uma conclusao.
#print(digits.target)
#print(digits.images[0])
# N se preocupe com o gamma agora depois explico
# SVC vem de suppor vector classification, ou seja e um svm, feito para classificar a imagem.
clf = svm.SVC(gamma=0.0001, C=100)
# Isso pega todo o conjunto de dados, tanto do dataset quanto do target, e o seu ultimo elemento

print(len(digits.data))
# Exemplo de overfit abaixe o gamma
x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x,y)
# Isso daki seria basicamente a tentativa de interpretar o numero dado nesse caso esto dando o antes do penultimo
print("Predicao do numero dado:",clf.predict(digits.data[[-6]]))
#Cmap e interpolation e para disponibilizar o datase de maneira visual, interpolation pega os mais pertos e destaca eles com certa cor e cmap,
# colore tudo e deixa um pouquinho com menos zomm
plt.imshow(digits.images[-6], cmap= plt.cm.gray_r, interpolation= 'nearest')
plt.show()