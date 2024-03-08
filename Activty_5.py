import time

# Mensagem de boas-vindas
print("Iremos Calcular o Aumento do seu salário ")
print("")

# Validação do Salário
while True:
    try:
        salario = float(input("Digite Seu Salário em Reais: "))
        break
    except ValueError:
        print("Por favor, digite um valor numérico para o salário.")

time.sleep(1)

# Validação do Aumento
while True:
    try:
        
        aumento = float(input("Digite seu Aumento em porcentagem: "))
        break
    # Tratativa para so receber Numeros 
    except ValueError:
        print("Por favor, digite um valor numérico para o aumento.")

time.sleep(1)

# Cálculo do aumento percentual e novo salário
aumento_percentual = salario * aumento / 100
novo_salario = salario + aumento_percentual

time.sleep(1)

# Exibição do resultado
print("")
print(f"Seu Novo Salário é de $ Tu{novo_salario:.2f}")


# Importar 'os' e usar o system para o comanda cls simulando Console.Clear()