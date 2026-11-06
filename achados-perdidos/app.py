
from cadastro import cadastrar_objeto
from pesquisa import pesquisar_objeto
from listar import listar_objetos
from devolucao import devolver_objeto


def menu():
    print("\n===== ACHADOS E PERDIDOS =====")
    print("1 - Cadastrar objeto")
    print("2 - Pesquisar objeto")
    print("3 - Ver objetos cadastrados")
    print("4 - Devolver objeto")
    print("5 - Sair")

    return input("\nEscolha uma opção: ").strip()


def iniciar_sistema():
    objetos = []

    while True:
        opcao = menu()

        if opcao == "1":
            objeto = cadastrar_objeto()

            if objeto is not None:
                objetos.append(objeto)
            input("Aperte ENTER para continuar...")

        elif opcao == "2":
            pesquisar_objeto(objetos)
            input("Aperte ENTER para continuar...")

        elif opcao == "3":
            listar_objetos(objetos)
            input("Aperte ENTER para continuar...")

        elif opcao == "4":
            devolver_objeto(objetos)
            input("Aperte ENTER para continuar...")

        elif opcao == "5":
            print("\nSistema encerrado!")
            break

        else:
            print("\nOpção inválida! Escolha uma opção de 1 a 5.")
            input("Aperte ENTER para continuar...")


if __name__ == "__main__":
    iniciar_sistema()
