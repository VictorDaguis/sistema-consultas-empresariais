import json


ARQUIVO_DADOS = "exemplo_dados.json"


def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: arquivo de dados não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: arquivo JSON inválido.")
        return []
    except Exception as erro:
        print(f"Erro inesperado ao carregar dados: {erro}")
        return []


def listar_empresas():
    return carregar_dados()


def buscar_empresa_por_cnpj(cnpj):
    empresas = carregar_dados()

    for empresa in empresas:
        if empresa["cnpj"] == cnpj:
            return empresa

    return None