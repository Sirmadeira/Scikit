import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import pandas as pd
from matplotlib import style
style.use("ggplot")

def Build_Data_Set(features = ["DE Ratio",
                               "Trailing P/E"]):
#Aviso nao e o mesmo dataset que limpamos isso daki e uma limpeza muito mais avancada que eu tive q fazer, 
#para possibilitar a db
    data_df = pd.read_csv("key_stats.csv")
    data_df = data_df[:100]

    X = np.array(data_df[features].values)
# Essa linha basicamente pega as features definidas, e acrescenta elas a uma lista
    y = (data_df["Status"]
         .replace("underperform",0)
         .replace("outperform",1)
         .values.tolist())
# Essa linha serve para transforma o status de underperformm para outperform, para 0 ou 1 dependendo da sua acao,
# logo em seguida insere eles em uma lista


    return X,y

def Analysis():
    X, y = Build_Data_Set()

    clf = svm.SVC(kernel="linear", C= 1.0)
    clf.fit(X,y)
    
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(min(X[:, 0]), max(X[:, 0]))
# Como voce poder ver aqui a gente nao sabe o maximo ou minimo e a gente redefine eles, pela magia np
    yy = a * xx - clf.intercept_[0] / w[1]

    h0 = plt.plot(xx,yy, "k-", label="non weighted")

    plt.scatter(X[:, 0],X[:, 1],c=y)
# Codigo magico, bem legal ele pega o elemento 0 desse array, e o que termina com 1 pega o primeiro elemento de cada elemento dentro do  x numpy array
# para entender melhor siga esse raciocinio
#x e uma lista com lista dentro
#x= [[1,7],
#	[1,6],
#	[1,8],]
# Meio que nesse formato
# X[:,0]
# Pega o 1,1,1
# E o X[:, 1] pega o 7,6,8
    plt.ylabel("Trailing P/E")
    plt.xlabel("DE Ratio")
    plt.legend()

    plt.show()
    
Analysis()