
from datetime import datetime


def cadastrar_objeto():
    print("\n===== CADASTRAR OBJETO =====")

    nome = input("Nome do objeto: ").strip()
    descricao = input("Descrição do objeto: ").strip()
    local = input("Local onde foi perdido/encontrado: ").strip()

    if not nome or not descricao or not local:
        print("\nTodos os campos são obrigatórios.")
        return None

    while True:
        data = input("Data (DD/MM/AAAA): ").strip()

        try:
            data_objeto = datetime.strptime(data, "%d/%m/%Y").date()
            hoje = datetime.now().date()

            try:
                limite = hoje.replace(year=hoje.year - 1)
            except ValueError:
                limite = hoje.replace(year=hoje.year - 1, day=28)

            if data_objeto > hoje:
                print("A data não pode ser futura!")
                continue

            if data_objeto < limite:
                print("A data não pode ser anterior a um ano!")
                continue

            break

        except ValueError:
            print("Data inválida! Digite uma data existente no formato DD/MM/AAAA.")

    objeto = {
        "nome": nome,
        "descricao": descricao,
        "local": local,
        "data": data,
        "devolvido": False
    }

    print("\nObjeto cadastrado com sucesso!")
    return objeto
