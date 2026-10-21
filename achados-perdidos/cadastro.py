def cadastrar_objeto():
    print("\n===== CADASTRAR OBJETO =====")

    nome = input("Nome do objeto: ").strip()
    descricao = input("Descrição do objeto: ").strip()
    local = input("Local onde foi perdido/encontrado: ").strip()
    data = input("Data: ").strip()

    if not nome or not descricao or not local or not data:
        print("\nTodos os campos são obrigatórios.")
        return None

    objeto = {
        "nome": nome,
        "descricao": descricao,
        "local": local,
        "data": data,
        "devolvido": False
    }

    print("\nObjeto cadastrado com sucesso!")
    return objeto