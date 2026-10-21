def pesquisar_objeto(objetos):
    print("\n===== PESQUISAR OBJETO =====")

    pesquisa = input("Digite o nome do objeto: ").strip().lower()

    if not pesquisa:
        print("Digite um nome para pesquisar.")
        return

    encontrados = [
        objeto for objeto in objetos
        if pesquisa in objeto["nome"].lower()
    ]

    if not encontrados:
        print("\nNenhum objeto encontrado.")
        return

    for objeto in encontrados:
        print("\n-------------------------")
        print("Nome:", objeto["nome"])
        print("Descrição:", objeto["descricao"])
        print("Local:", objeto["local"])
        print("Data:", objeto["data"])
        print(
            "Status:",
            "Devolvido" if objeto["devolvido"] else "Disponível"
        )