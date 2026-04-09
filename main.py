from consulta import buscar_empresa_por_cnpj, listar_empresas
from relatorio import gerar_relatorio_txt
from utils import limpar_cnpj


def exibir_menu():
    print("\n=== Sistema de Consultas Empresariais ===")
    print("1. Listar empresas")
    print("2. Buscar empresa por CNPJ")
    print("3. Gerar relatório por CNPJ")
    print("4. Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            empresas = listar_empresas()
            if not empresas:
                print("\nNenhuma empresa encontrada.")
                continue

            print("\nEmpresas cadastradas:")
            for i, empresa in enumerate(empresas, start=1):
                print(f"{i}. {empresa['nome']} | CNPJ: {empresa['cnpj']} | Cidade: {empresa['cidade']}")

        elif opcao == "2":
            cnpj = input("Digite o CNPJ: ").strip()
            cnpj_limpo = limpar_cnpj(cnpj)

            empresa = buscar_empresa_por_cnpj(cnpj_limpo)

            if empresa:
                print("\nEmpresa encontrada:")
                print(f"Nome: {empresa['nome']}")
                print(f"CNPJ: {empresa['cnpj']}")
                print(f"Cidade: {empresa['cidade']}")
                print(f"Segmento: {empresa['segmento']}")
            else:
                print("\nEmpresa não encontrada.")

        elif opcao == "3":
            cnpj = input("Digite o CNPJ para gerar relatório: ").strip()
            cnpj_limpo = limpar_cnpj(cnpj)

            empresa = buscar_empresa_por_cnpj(cnpj_limpo)

            if empresa:
                caminho_arquivo = gerar_relatorio_txt(empresa)
                print(f"\nRelatório gerado com sucesso: {caminho_arquivo}")
            else:
                print("\nEmpresa não encontrada. Relatório não gerado.")

        elif opcao == "4":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()