idade = int(input("Digite sua idade: "))

if idade <= 0:
    print("Idade inválida. Deve ser Maior que 0.")
elif idade >= 18 and (idade <= 65):
    print("Idade obrigatória.")
else:
    print("Idade facultativa.")
