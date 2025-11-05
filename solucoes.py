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
    # TODO: implementar a lógica (Gustavo)
    pass
