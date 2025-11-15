import pandas as pd 
import numpy as np 
import matplotlib as plt 

df =pd.read_csv("dados_sujos.csv")
#print(df.shape)
#print(df.columns)

#função suporte
def verificar_colunas(lista_cols: list, df: pd.DataFrame)-> None: 
    """Função de suporte feita para verificar se as colunas que iremos utilizar para manipular o dataframe realmente existem no dataframe.

    Parameters
    ----------
    lista_cols : list
        Lista com o nome de cada coluna que será usada.
    df : pd.Dataframe
        Dataframe que vamos verificar a existência das colunas

    Raises
    ------
    ValueError 
        Caso o Dataframe não possua as colunas requeridas
    TypeError
        Caso a lista_cols não seja uma lista 
        caso não seja possível transformar df em um Dataframe

    Returns
    -------
    None
        A função não retorna nada, apenas levanta exceções se houver problema.

    Examples
    --------
    >>> verificar_colunas(['tempo', 'duration_ms'], df_spotify)
    """
    try: 
        df = pd.DataFrame(df)
    except Exception: 
        raise TypeError("Dataset recebido no formato inválido.")
    if not isinstance(lista_cols, list): 
        raise TypeError("Argumento recebido no formato inválido.")
    for col in lista_cols:
        if col not in df.columns :
            raise ValueError("O dataframe recebido não possui as colunas necessárias para a análise")
    return

def limpar_database(df: pd.DataFrame)-> pd.DataFrame:
    """Função que recebe um dataframe de tracks do spotfy e retira os ruidos das amostras. 

    Parameters
    ----------
    df: pd.Dataframe
        Um dataframe com dados de tracks de spotfy com as colunas:  ["artists","track_name", "tempo", "duration_ms","loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence"]
    
    Raises
    ------
    TypeError: 
        Caso não seja possível transformar o imput da função em um Dataframe
    ValueError:
        Caso o dataframe recebido não possua as colunas necessárias. 

    Returns
    -------
    pd.DataFrame
        O DataFrame limpo e convertido.

    Examples
    --------
    >>> df_limpo = limpar_database(df_spotify)
    >>> df_limpo.info()
    """

    try: 
        df = pd.DataFrame(df)
    except Exception: 
        raise TypeError("Argumento recevido no formato inválido.")

    cols = ['artists','track_name', 'tempo', 'duration_ms']
    verificar_colunas(cols, df)
    df[cols] = df[cols].replace(["", "NA", "N/A", 0], None) 
    df = df.dropna(subset=cols)

    cols_num = ["loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence"] 
    verificar_colunas(cols_num, df)
    df[cols_num] = df[cols_num].apply(pd.to_numeric, errors="coerce")

    df[cols_num] = df[cols_num].replace([pd.NA, None], 0 )
    return df

df_limpo = limpar_database(df)
#print(df.shape)

def filtrar_dataset(df: pd.DataFrame)-> pd.DataFrame:
    """
    Função que recebe um dataset do spotfy e filtra categorias que serão utilizadas para nossas análises, retirando músicas com conteúdo explicito, nenhuma popularidade ou duração muito curta.

    Parameters
    ----------
    df : pd.Dataframe
        Dataset do spotfy
    
    Raises
    ------ 
    ValueError 
        Caso o Dataframe não possua as colunas requeridas
    TypeError
        caso não seja possível transformar df em um Dataframe

    Returns
    -------
    pd.DataFrame
        Retorna o DataFrame filtrado

    Examples
    --------
    >>> df_diltrado = filtrar_dataset(df_limpo)
    >>> df_filtrado.info()

    
    """
    cols = ["explicit", "popularity", "duration_ms"]
    verificar_colunas(cols, df)
    df[cols[1:]] = df[cols[1:]].apply(pd.to_numeric, errors="coerce")
    df[cols[1:]] = df[cols[1:]].replace([pd.NA, None], 0 )

    df = df.loc[df["explicit"] == False]
    df = df.loc[df["popularity"] != 0]
    df = df.loc[df["duration_ms"]>90000]

    return df 

df_filtrado = filtrar_dataset(df_limpo)
#print(df.shape)


def calcular_features(df: pd.DataFrame)-> pd.DataFrame:
    """
    Função que calcula algumas features com base em outras colunas do spotfy.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset do spotfy. 
    
    Raises
    ------
    ValueError 
        Caso o Dataframe não possua as colunas requeridas
    TypeError
        caso não seja possível transformar df em um Dataframe

    Returns
    -------
    df : pd.DataFrame
        Dataframe com as features calculadas.

    Examples
    --------
    >>> df_features = calcular_features(df_filtrado)
    >>> df_features.info()
    """
   
    df["nome_display"] = df["artists"] + " - " + df["track_name"]
    
    df["link_spotify"] = "https://open.spotify.com/track/" + df["track_id"]

    df["batidas_totais"] =  (df["duration_ms"]/60000)*df["tempo"] 

    df["tier_popularity"] = pd.cut(df["popularity"], bins=[0, 40, 80, 100], labels=["esquecida", "normal", "hit"], right=True, include_lowest=True)

    return df 

df_features = calcular_features(df_filtrado)
#print(df.shape)

def analisar_generos(df: pd.DataFrame) -> pd.DataFrame: 
    """
    Função responsável por calcular medidas estatísticas (média, media, quantil05, quantil25, mediana, quantil75, quantil95) de cada gênero músical.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset do spotfy. 
    
    Raises
    ------
    ValueError 
        Caso o Dataframe não possua as colunas requeridas
    TypeError
        caso não seja possível transformar df em um Dataframe

    Returns
    -------
    df : pd.DataFrame
        Dataframe apenas com os valores das medidas estatísticas de cada gênero músical.

    Examples
    --------
    >>> df_medidas = analisar_generos(df_features)
    >>> df_medidas.info()
    """
    cols = ["loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "track_genre"] 
    verificar_colunas(cols, df)

    mean = df[cols].groupby("track_genre").mean()
    p05 = df[cols].groupby("track_genre").quantile(0.05)
    p25 = df[cols].groupby("track_genre").quantile(0.25)
    p50 = df[cols].groupby("track_genre").quantile(0.5)
    p75 = df[cols].groupby("track_genre").quantile(0.75)
    p95 = df[cols].groupby("track_genre").quantile(0.95)

    dict_dfs = {"mean": mean, "p05": p05, "p25": p25, "p50": p50, "p75": p75, "p95": p95}

    new_df = pd.DataFrame(index= pd.unique(df["track_genre"]))

    for col in cols[:-1]:
        for nome, sub_df in dict_dfs.items():
            new_df[f"{col}_{nome}"] = sub_df[col]

    return new_df

new_df = analisar_generos(df_features)


def remover_outliers(df_musicas: pd.DataFrame, df_estatisticas: pd.DataFrame) -> pd.DataFrame: 
    """
    Função responsável por retirar as outliers de um dataset do spotfy a partir dos cálculos feitos por analisar_generos() . 

    Parameters
    ----------
    df_musicas : pd.DataFrame
        Dataset do spotfy.
    df_estatisticas: pd.Dataframe
        Dataset oriundo da função analisar_genero().  

    Returns
    -------
    df : pd.DataFrame
        Dataframe filtrado, sem as músicas com outliers.

    Examples
    --------
    >>> df_final = remover_outliers(df_features, df_medidas)
    >>> df_final.info()
    """
    cols = ["loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence"]
    generos = df_estatisticas.index

    df_max = pd.DataFrame(index= generos)
    df_min = pd.DataFrame(index= generos)
    df_min["track_genre"] = generos
    df_max["track_genre"] = generos

    for col in cols:
        df_min[f"P05_{col}"] = df_estatisticas[f"{col}_p05"]
        df_max[f"P95_{col}"] = df_estatisticas[f"{col}_p95"]

    df_lim = pd.merge(df_min, df_max, on="track_genre" )
    df_final = pd.merge(df_musicas, df_lim, how="left")
    
    is_outlier = False
    for col in cols: 
        is_outlier_col = (df_final[col] < df_final[f"P05_{col}"]) | (df_final[col] > df_final[f"P95_{col}"])
        is_outlier =  is_outlier_col | is_outlier 
    #Mpascara Booleana que é True para outliers

    df_final = df_final[~is_outlier]

    for col in cols: 
        df_final = df_final.drop(columns= [f"P05_{col}",f"P95_{col}"] )
    df_final = df_final.drop(columns=["index"])
    return df_final
    
df_final = remover_outliers(df_features, new_df)
#print(df_final.shape)
print(df_final)


