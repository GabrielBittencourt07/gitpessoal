import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import Tentativa_de_fazer_com_OO as mod

dados = mod.DadosIMU(pd.read_csv("df_filt.csv"))
teste = mod.DadosIMU(pd.read_csv("df_test.csv"))

dados["Timestamp"] = pd.to_datetime(dados["Timestamp"])
dados["segundo"] = dados["Timestamp"].dt.floor("S")

dados = dados.drop(columns=["Type", "Position", "Breed", "Subject", "Timestamp"])

grouped = dados.groupby("segundo")

features = pd.DataFrame()

for col in dados.columns[:-1]:
    _ = grouped[col].describe()
    features[f"mean_{col}"] = _["mean"]
    features[f"std_{col}"] = _["std"]

eixos = ("X", "Y", "Z")

def get_axis(axis: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe_ax_mean = pd.DataFrame()
    dataframe_ax_std = pd.DataFrame()
    for ax in axis:
        for col in dataframe: 
            if col.endswith(ax):
                if col.startswith("mean"):
                    dataframe_ax_mean[col] = dataframe[col]
                else: 
                    dataframe_ax_std[col] = dataframe[col]
    
    dataframe_ax_mean = dataframe_ax_mean.reset_index().groupby("segundo").mean()
        
    return dataframe_ax_mean
           
#for eixo in eixos: 
#    get_axis(eixo, features)

print(get_axis("X", features))






