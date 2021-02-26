
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [20, 5, 100, 33, 10]

title = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(title)

plt.xlabel(eixox)
plt.ylabel(eixoy)

# liga os pontos, altera a cor da linha e o estilo da linha
plt.plot(x, y, color="#000000", linestyle="--")

# mostra os pontos, aplica a legenda, muda a cor dos pontos, altra o marcador e tamanho
plt.scatter(x, y, label="Principais pontos", color="k", marker=".", s=z)

plt.legend()

# salvando na resolucao comum
plt.savefig("img/format_png.png")

# salvando em pdf(resolucao melhor)
plt.savefig("img/format_pdf.pdf")

# salvando em PNG alterando dados de DPI
plt.savefig("img/format_png_300dpi.png", dpi=300)
