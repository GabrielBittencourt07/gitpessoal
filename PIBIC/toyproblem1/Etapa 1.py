import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import Tentativa_de_fazer_com_OO as mod

if __name__ == "__main__":

    dados = mod.DadosIMU(pd.read_csv("df_filt.csv"))
    teste = mod.DadosIMU(pd.read_csv("df_test.csv"))

    print(dados.amostras_posições())
    print(dados.amostras_caes())

    # dados_group = dados.groupby("Subject").count()
    # print(dados_group)
    # print(dados_group.describe())
    # dados_group = dados.groupby("Position").count()
    # print(dados_group)
    # print(dados_group.describe())
    # Body shake tem muito menos dados que o restante das categorias. Por outro lado, standing foi a categoria de maior quantidade de dados. A média geral é de 60380. 
    # print(dados.info())

    y_train = dados["Position"]
    x_train = mod.DadosIMU(dados).dados_num() # Ao aplicar funções da minha classe que retornam um DataFrame (dados_num() é um exemmplo disso) o objeto deixa de se referir a minha classe e passa a ser um DataFrame
    # print(x_train.amostras_caes()) # Não da KeyError como eu esperava, mas sim AttributeError já que x_train é um DataFrame e não um DadosIMU 

    y_teste = teste["Position"]
    x_teste = mod.DadosIMU(teste).dados_num()

    rf = RandomForestClassifier(
        n_estimators=100,       # número de árvores
        random_state=42,        # para reprodutibilidade
        n_jobs=-1               # usa todos os núcleos disponíveis
    )

    rf.fit(x_train, y_train)

    y_pred = rf.predict(x_teste)
    print("Acurácia:", accuracy_score(y_teste, y_pred))
    print(classification_report(y_teste, y_pred))
