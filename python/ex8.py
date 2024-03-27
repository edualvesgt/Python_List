# Solicita ao usuário a altura e o sexo
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (m para masculino, f para feminino): ")

# Calcula o peso ideal com base no sexo
if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido. Por favor, digite 'm' para masculino ou 'f' para feminino.")
    exit()

# Exibe o peso ideal
print("Seu peso ideal é: {:.2f} kg".format(peso_ideal))