def limpar_cnpj(cnpj):
    return "".join(caractere for caractere in cnpj if caractere.isdigit())