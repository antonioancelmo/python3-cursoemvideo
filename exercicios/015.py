dias = int(input("Quantoa dias alugados? "))
km = float(input("Quantos Km rodados? "))

valor_dias = dias * 60
valor_km = km * 0.15
total = valor_dias + valor_km
print("O total a pagar é de R${:.2f}".format(total))
