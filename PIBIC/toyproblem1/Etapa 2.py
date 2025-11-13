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


def get_axis_mean(ax: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe_ax_mean = pd.DataFrame()
    dataframe_ax_std = pd.DataFrame()

    for col in dataframe: 
        if col.endswith(ax):
            if col.startswith("mean"):
                dataframe_ax_mean[col] = dataframe[col]
            else: 
                dataframe_ax_std[col] = dataframe[col]
    
    dataframe_ax_mean = dataframe_ax_mean.mean(axis = 1 )
    dataframe_ax_std = dataframe_ax_std.mean(axis = 1 )
        
    return pd.DataFrame({f"mean_media_{ax}": dataframe_ax_mean, f"mean_Desviopadrao_{ax}": dataframe_ax_std})

def get_axis_sum(ax: str, dataframe: pd.DataFrame) -> pd.DataFrame: 
    dataframe_ax_std = pd.DataFrame()

    for col in dataframe: 
        if col.endswith(ax):
            if col.startswith("std"):
                dataframe_ax_std[col] = dataframe[col]
            
    dataframe_ax_sum_std = dataframe_ax_std.sum(axis = 1 )

    return pd.DataFrame({f"soma_std_{ax}":dataframe_ax_sum_std})


           
eixos = ("X", "Y", "Z")

sum_std_ax = pd.DataFrame()
mean_std = pd.DataFrame()
for ax in eixos:
    mean_std = get_axis_mean(ax, features).join(mean_std)
    sum_std_ax = get_axis_sum(ax, features).join(sum_std_ax)

print(sum_std_ax)






