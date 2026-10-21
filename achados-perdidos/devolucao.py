def devolver_objeto(objetos):
    print("\n===== DEVOLVER OBJETO =====")

    disponiveis = [
        objeto for objeto in objetos
        if not objeto["devolvido"]
    ]

    if not disponiveis:
        print("Não há objetos disponíveis para devolução.")
        return

    for indice, objeto in enumerate(disponiveis, start=1):
        print(f"{indice} - {objeto['nome']} ({objeto['local']})")

    try:
        escolha = int(input("\nEscolha o número do objeto: "))

        if escolha < 1 or escolha > len(disponiveis):
            print("Opção inválida.")
            return

        objeto = disponiveis[escolha - 1]

        print("\nObjeto selecionado:", objeto["nome"])
        confirmacao = input("Confirmar devolução? (s/n): ").strip().lower()

        if confirmacao == "s":
            objeto["devolvido"] = True
            print("Objeto marcado como devolvido!")
        else:
            print("Devolução cancelada.")

    except ValueError:
        print("Digite um número válido.")