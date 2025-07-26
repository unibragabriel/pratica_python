def menu():
    print("=== CALCULADORA ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "5":
        print("Encerrando a calculadora...")
        break

    if escolha in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                resultado = num1 + num2
                operacao = "Soma"
            elif escolha == "2":
                resultado = num1 - num2
                operacao = "Subtração"
            elif escolha == "3":
                resultado = num1 * num2
                operacao = "Multiplicação"
            elif escolha == "4":
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2
                operacao = "Divisão"

            print(f"{operacao} de {num1} e {num2} é: {resultado}\n")

        except ValueError:
            print("Erro: Por favor, digite números válidos.\n")
    else:
        print("Opção inválida. Tente novamente.\n")
