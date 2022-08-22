largura = float(input("Informe a largura da parede (em metros): "))
altura = float(input("Informe a alturada parede (em metros): "))

area = largura * altura
tinta = area/2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(largura, altura, area))
print("Para pintar essa parede, você precisará de {:.1f} litros de tinha.".format(tinta))