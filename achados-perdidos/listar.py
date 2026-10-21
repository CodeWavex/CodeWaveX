def listar_objetos(objetos):
    print("\n===== OBJETOS CADASTRADOS =====")

    if not objetos:
        print("Nenhum objeto cadastrado.")
        return

    for indice, objeto in enumerate(objetos, start=1):
        print(f"\nObjeto {indice}")
        print("-------------------------")
        print("Nome:", objeto["nome"])
        print("Descrição:", objeto["descricao"])
        print("Local:", objeto["local"])
        print("Data:", objeto["data"])
        print(
            "Status:",
            "Devolvido" if objeto["devolvido"] else "Disponível"
        )