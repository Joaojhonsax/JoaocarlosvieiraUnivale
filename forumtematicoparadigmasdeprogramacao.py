dias = int(input('Quantos dias o carro foi alugado?  '))
km = float(input('Quantos quilometros foram rodados?  '))
pagamento = (dias * 60) + (km * 0.15)
print(f'O valor total a pagar é de R${pagamento}')
