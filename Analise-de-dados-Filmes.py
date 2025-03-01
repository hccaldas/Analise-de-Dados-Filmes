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