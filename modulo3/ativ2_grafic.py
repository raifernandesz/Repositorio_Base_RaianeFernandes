import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt





# Criando um grafico sobre minha experiencia profissional 
dados = {
    "Ingles": [7, 7, 6, 6, 7],
    "Programação" : [8, 9, 7, 8, 9],
    "Comunicação": [10, 8, 7, 9, 8],
    "Trabalho em Equipe": [9, 8, 8, 9, 7],
    "Proatividade": [9, 8, 9, 7, 8]
}


df = pd.DataFrame(dados)
plt.figure(figsize=(10, 6))
sns.barplot(data = df)  
plt.title(" Habilidades Profissionais de Raiane Fernandes")
plt.xlabel("Habilidades")
plt.ylabel("Nível de Proficiência (0-10)")
plt.show()
 
