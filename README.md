# Análise de Dados de Filmes

Este repositório contém um script em Python que realiza a análise de dados de um conjunto de filmes. O script lê um arquivo CSV contendo metadados de filmes, filtra filmes adultos, remove valores nulos, e cria várias visualizações para entender melhor os dados.

## Funcionalidades

- Leitura de um arquivo CSV contendo metadados de filmes.
- Filtragem de filmes marcados como "adult".
- Remoção de valores nulos.
- Visualização da distribuição das avaliações dos filmes.
- Separação e explosão da coluna de gêneros.
- Contagem e visualização da frequência dos gêneros dos filmes.

## Pré-requisitos

- Python 3.x
- Bibliotecas `pandas`, `seaborn` e `matplotlib` instaladas. Você pode instalar essas bibliotecas usando os seguintes comandos:
  ```bash
  pip install pandas
  pip install seaborn
  pip install matplotlib

1.Clone este repositório ou copie o código para o seu ambiente local.
2.Certifique-se de ter o Python 3.x instalado no seu sistema.
3.Instale as bibliotecas necessárias usando os comandos acima.
4.Coloque o arquivo movies_metadata.csv no mesmo diretório do script ou forneça o caminho correto para o arquivo.
5.Execute o script.

Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Você pode fazer isso abrindo uma issue ou enviando um pull request.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Escolher arquivo csv na pasta para analisar
df = pd.read_csv("movies_metadata.csv")

# Exibir os primeiros registros do DataFrame
print(df.head())

# Filtrar os filmes que são marcados como "adult"
filmes_adult = df[df['adult'] == 'True']

# Exibir os primeiros registros dos filmes adultos
print(filmes_adult.head())

# Remover valores nulos
df.dropna(inplace=True)

# Exibir informações do DataFrame
df.info()

# Plotar histograma das avaliações dos filmes
sns.histplot(df['vote_average'], bins=10)
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribuição das Avaliações dos Filmes')
plt.show()

# Separar os gêneros em colunas individuais
df["genres"] = df["genres"].str.split("|")

# Exibir os primeiros registros após a separação dos gêneros
print(df.head())

# Explodir a coluna de gêneros para que cada gênero tenha sua própria linha
df = df.explode("genres")

# Exibir os primeiros registros após a explosão dos gêneros
print(df.head())

# Contar a frequência de cada gênero
generos_contagem = df["genres"].value_counts()

# Exibir a contagem dos gêneros
print(generos_contagem)

# Plotar gráfico de barras horizontais dos gêneros
generos_contagem.plot.barh()
plt.xlabel('Frequency')
plt.ylabel('Genres')
plt.title('Frequência dos Gêneros dos Filmes')
plt.show()

# Plotar gráfico de pizza dos gêneros
generos_contagem.plot.pie(autopct="%1.1f%%", startangle=90, counterclock=False)
plt.title('Distribuição dos Gêneros dos Filmes')
plt.ylabel('')
plt.show()

# Plotar gráfico de barras dos gêneros
generos_contagem.plot.bar()
plt.xlabel('Genres')
plt.ylabel('Frequency')
plt.title('Frequência dos Gêneros dos Filmes')
plt.show()
