
import matplotlib.pyplot as plt

# dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]


title = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# montando o gráfico
plt.bar(x, y)

# exibindo o gráfico
plt.show()
