import os 
import time 
while True:
    time.sleep(2)
    os.system('cls')
    print("Calculadora:")
    print("1. Soma")
    print("2. Multiplicação")
    print("3. Subtração")
    print("4. Divisão")
    print("5. Sair")

    op = input("Escolha uma operação (1-5): ")

    if op == "5":
        print("Saindo do programa...")
        break
    elif op in ["1", "2", "3", "4"]:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")
            continue

        if op == "1":
            result = num1 + num2
            time.sleep(2)
            print("Resultado:", result)
        elif op == "2":
            result = num1 * num2
            time.sleep(2)
            print("Resultado:", result)
        elif op == "3":
            result = num1 - num2
            time.sleep(2)
            print("Resultado:", result)
        elif op == "4":
            if num2 != 0:
                result = num1 / num2
                time.sleep(2)
                print("Resultado:", result)
            else:
                print("Não é possível dividir por zero.")
    else:
        time.sleep(2)
        print("Opção inválida.")
        
