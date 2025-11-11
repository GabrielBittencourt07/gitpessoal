[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/M-dQIkrM)
# Lista 3 - Linguagens de programação

**Objetivo Geral:** Usar a biblioteca `pandas` para realizar limpeza, transformação, filtragem e análise de um conjunto de dados.

**Prazo:** 29/10

**Forma de entrega:** Repositório no GitHub Classroom.

## Organização dos arquivos e questões

Todas as funções pedidas devem ser implementadas em um único arquivo `respostas.py`, que deve estar na **raiz do repositório**.

> ⚠️ **Atenção**: **não** entrege suas funções em um arquivo com outro nome ou divididas vários arquivos ou dentro de uma subpasta. Entregas que não respeitarem essa regra serão penalizadas.

## Contexto

Você foi contratado como Analista de Dados por uma startup de recomendação de músicas. Seu primeiro
grande desafio é trabalhar com uma base de dados de músicas disponíveis no Spotify. Essa base,
infelizmente, está bastante "suja". Ela contém dados inconsistentes, formatos incorretos e outliers
que estão distorcendo as análises.

Seu objetivo é criar um pipeline de limpeza e transformação em Python usando Pandas, estruturado em
quatro funções principais, para preparar os dados para um sistema de Machine Learning.

O dataset já está disponível no repositório da lista. Você pode (e deve) ler a descrição detalhada
de cada coluna no
[Kaggle](https://www.kaggle.com/datasets/melissamonfared/spotify-tracks-attributes-and-popularity).
O dataset fornecido na atividade está "sujo", e pode ser usado para testar as questões 1 e 2.

## Questão 1

```py
limpar_dataset(df: pd.DataFrame) -> pd.DataFrame
```

Esta função deve receber o DataFrame "sujo" e realizar sua limpeza, aplicando os seguintes filtros:

1. Elimine todas as linhas em que as colunas `artists`, `track_name`, `tempo` e `duration_ms` sejam Nulas (`NA`) ou `0`.

2. Converta as colunas de atributos (`loudness`, `speechiness`, `acousticness`, `instrumentalness`, `liveness` e `valence`) para o tipo float, caso elas estejam como string.

3. Para essas mesmas colunas de atributos (`loudness`, `speechiness`, `acousticness`, `instrumentalness`, `liveness` e `valence`), preencha quaisquer valores `NaN` restantes (vindos possívelmente de uma conversão falha) com `0`.

A função deverá retornar o dataframe com as mesmas colunas, mas com os tipos apropriados e linhas inválidas removidas. As demais questões poderão assumir que as colunas do dataframe estarão corretamente tipadas e sem valores nulos.

## Questão 2

```py
filtrar_dataset(df: pd.DataFrame) -> pd.DataFrame
```

Esta função deve eliminar linhas que, apesar de não serem inválidas, não serão contadas no sistema de recomendação.

1. O sistema de recomendação focará apenas em músicas "family friendly" (não-explícitas). Remova todas as músicas onde `explicit` seja `True`.

2. Remova músicas que tenham popularity igual a 0 ou que tenham `duration_ms` inferior a 90 segundos (`duration_ms` < 90000).

A função deverá retornar o dataframe com as mesmas colunas, mas com algumas linhas removidas.

## Questão 3

```py
calcular_features(df: pd.DataFrame) -> pd.DataFrame
```

Com o dataset limpo, sua próxima tarefa é criar novas colunas (features) que serão úteis para a análise e Machine Learning. As colunas que devem ser criadas são:

- `nome_display`: Uma coluna que combine o nome do artista e o nome da música, seguindo o formato `"{artist_name} - {track_name}"` (exemplo: "Queen - Bohemian Rhapsody").

- `link_spotify`: Uma coluna com o link completo para a música, usando o `track_id`, seguindo o formato `"https://open.spotify.com/track/{track_id}"`.

- `batidas_totais`: Uma coluna que estime o número total de batidas na música. A fórmula para calcular essa coluna é dada por: $ Total = \left(\frac{duration\_ms}{60000}\right) \times tempo $ 

- `tier_popularidade`: Uma coluna categórica que diz se a música é `esquecida`, `normal` ou `hit`. Músicas esquecidas são aquelas cuja popularidade está no intervalo $ [0, 40) $, músicas normais são aquelas cuja popularidade está no intervalo $ [40, 80] $ e músicas hits são aquelas cuja popularidade está no intervalo $ (80, 100] $.

A função deve receber o DataFrame "limpo" (com colunas corretamente tipadas e filtradas) e retornar o DataFrame com as novas colunas solicitadas.

> ⚠️ **Atenção**: siga exatamente os nomes de colunas novas fornecidos, incluindo letras maiúsculas e minúsculas. Não remova nenhuma coluna nessa operação, apenas adicione novas.

## Questão 4

```py
analisar_generos(df: pd.DataFrame) -> pd.Dataframe
```

Agora, você precisa entender as características de cada gênero. Esta função deve:

1. Agrupar o DataFrame de acordo com a coluna `track_genre`.

2. Calcular as seguintes estatísticas para cada um dos 6 atributos principais (`loudness`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`), dividos por gênero:

- Média (`mean`)

- Percentil 5% (`quantile(0.05)`)

- Percentil 25% (`quantile(0.25)`)

- Mediana | Percentil 50% (`quantile(0.50)`)

- Percentil 75% (`quantile(0.75)`)

- Percentil 95% (`quantile(0.95)`)

A função deve retornar um novo DataFrame onde os índices são os valores únicos de `track_genre` e as colunas são as estatísticas calculadas (expanda a seção abaixo para ver exatamente os nomes esperados).

<details>
<summary>Colunas esperadas do DataFrame de saída</summary>

    ['loudness_mean', 'loudness_p05', 'loudness_p25', 'loudness_p50', 'loudness_p75', 'loudness_p95', 'speechiness_mean', 'speechiness_p05', 'speechiness_p25', 'speechiness_p50', 'speechiness_p75', 'speechiness_p95', 'acousticness_mean', 'acousticness_p05', 'acousticness_p25', 'acousticness_p50', 'acousticness_p75', 'acousticness_p95', 'instrumentalness_mean', 'instrumentalness_p05', 'instrumentalness_p25', 'instrumentalness_p50', 'instrumentalness_p75', 'instrumentalness_p95', 'liveness_mean', 'liveness_p05', 'liveness_p25', 'liveness_p50', 'liveness_p75', 'liveness_p95', 'valence_mean', 'valence_p05', 'valence_p25', 'valence_p50', 'valence_p75', 'valence_p95']

</details>


> **Dica**: para fazer essa função, leia **atentamente** as documentações de [`Series.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html) e [`DataFrameGroupBy.agg`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html).

> ⚠️ **Atenção**: siga *exatamente* o padrão fornecido para nomear as colunas, incluindo letras maiúsculas e minúsculas. O não cumprimento desses padrões poderão quebrar manipulações futuras dos dados.

## Questão 5

```py
remover_outliers(df_musicas: pd.DataFrame, df_estatisticas: pd.DataFrame) -> pd.DataFrame
```

Esta é a etapa final e mais crítica. Usando as estatísticas que você acabou de gerar, você precisa limpar os outliers. Um outlier é definido como qualquer música que esteja fora do intervalo P05-P95 em qualquer um dos 6 atributos, levando em conta o seu gênero específico.

A função deve receber o DataFrame de músicas "limpo" (`df_musicas`) e o DataFrame de estatísticas de gênero (`df_estatisticas`), no formato calculado na função 4. Seu funcionamento pode ser sumarizado como:

1. Para cada música, verificar seus valores nas 6 colunas (loudness, speechiness, etc.).

2. Comparar esses valores com os limites P05 e P95 do gênero daquela música (que estão no `df_estatísticas`).

3. Se pelo menos um dos 6 atributos da música for menor que o P05 do seu gênero ou maior que o P95 do seu gênero, a música inteira deve ser removida.

4. A função deve retornar o DataFrame final, contendo apenas as músicas "não-outliers".

A função deverá retornar o dataframe de músicas (`df_musicas`) com as mesmas colunas, mas com algumas linhas removidas.

> **Dica**: existem múltiplas formas de fazer essa operação. Recomendamos a leitura da página [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html) da documentação pandas para inspiração em uma das maneiras de fazer a questão.
