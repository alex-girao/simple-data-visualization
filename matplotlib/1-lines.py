
import matplotlib.pyplot as plt

# dados
x = [1, 2, 5]
y = [2, 3, 7]

# definindo o título do gráfico
plt.title("Gráfico de linhas")

# definindo legendas
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# montando o gráfico
plt.plot(x, y)

# exibindo o gráfico
plt.show()
