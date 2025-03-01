import pandas as pd # Importar a biblioteca pandas para manipulação de dados
import seaborn as sns # Importar a biblioteca seaborn para visualização de dados
import matplotlib.pyplot as plt # Importar a biblioteca matplotlib para plotar gráficos

# Escolher arquivo csv na pasta para analisar os dados dos filmes (movies_metadata.csv)
df = pd.read_csv("movies_metadata.csv")

# Exibir os primeiros registros do DataFrame (tabela de dados)
print(df.head())

# Filtrar os filmes que são marcados como "adult", ou mudar para qualquer gênero que desejar analisar
filmes_adult = df[df['adult'] == 'True']

# Exibir os primeiros registros dos filmes adultos (ou do gênero escolhido)
print(filmes_adult.head())

# Remover valores nulos do DataFrame (NaN)
df.dropna(inplace=True)

# Exibir informações do DataFrame   (linhas, colunas, tipo de dados, etc)
df.info()

# Plotar histograma das avaliações dos filmes
sns.histplot(df['vote_average'], bins=10) # bins = número de barras do histograma
plt.xlabel('Rating') # Legenda do eixo x
plt.ylabel('Frequency') # Legenda do eixo y 
plt.title('Distribuição das Avaliações dos Filmes') # Título do gráfico 
plt.show() # Exibir o gráfico de histograma das avaliações dos filmes

# Separar os gêneros em colunas individuais
df["genres"] = df["genres"].str.split("|") # Separar os gêneros por "|"

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

# Plotar gráfico de barras horizontais dos gêneros (horizontal)
generos_contagem.plot.barh()
plt.xlabel('Frequency')
plt.ylabel('Genres')
plt.title('Frequência dos Gêneros dos Filmes')
plt.show()

# Plotar gráfico de pizza dos gêneros (com porcentagem)
generos_contagem.plot.pie(autopct="%1.1f%%", startangle=90, counterclock=False)
plt.title('Distribuição dos Gêneros dos Filmes')
plt.ylabel('')
plt.show()

# Plotar gráfico de barras dos gêneros (vertical)
generos_contagem.plot.bar()
plt.xlabel('Genres')
plt.ylabel('Frequency')
plt.title('Frequência dos Gêneros dos Filmes')
plt.show()
