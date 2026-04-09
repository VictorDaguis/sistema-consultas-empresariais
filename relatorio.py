from datetime import datetime


def gerar_relatorio_txt(empresa):
    nome_arquivo = f"relatorio_{empresa['cnpj']}.txt"

    conteudo = (
        "=== RELATÓRIO EMPRESARIAL ===\n"
        f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
        f"Nome: {empresa['nome']}\n"
        f"CNPJ: {empresa['cnpj']}\n"
        f"Cidade: {empresa['cidade']}\n"
        f"Segmento: {empresa['segmento']}\n"
    )

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    return nome_arquivo