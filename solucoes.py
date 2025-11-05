'''
sao_anagramas(string1, string2) recebe duas strings e retorna True se elas forem
anagramas uma da outra, e False caso contrário. (Um anagrama é uma palavra ou
frase formada pelo rearranjo das letras de outra palavra ou frase. Espaços e
diferenças entre maiúsculas e minúsculas devem ser ignorados.)
'''
def sao_anagramas(string1, string2):
    # Remover caixa alta e espaços
    str1 = string1.replace(" ", "").lower()
    str2 = string2.replace(" ", "").lower()

    # Comparar as strings ordenadas
    return sorted(str1) == sorted(str2)

def cifra_de_cesar(texto, deslocamento):
    # TODO: implementar a lógica (Be)
    pass

def valida_cpf(cpf_string):
    # Remover caracteres não numéricos
    cpf = ''.join([c for c in cpf_string if c.isdigit()])

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    # Comparar o calculado com o fornecido
    if digito1 != int(cpf[9]):
        return False

    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    # Comparar o calculado com o fornecido
    if digito2 != int(cpf[10]):
        return False

    return True
