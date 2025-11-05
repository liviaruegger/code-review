def sao_anagramas(string1, string2):
    # TODO: implementar a lógica (Ana)
    pass

def cifra_de_cesar(texto, deslocamento):
    cifrado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            resultado += chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
#adiciona deslocamento
        elif 'A' <= char <= 'Z':
            resultado += chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
#adiciona deslocamento
        else:
#nao muda nada se nao eh letra
            cifrado += char
    return cifrado   

 # TODO: implementar a lógica (Be)
    pass

def valida_cpf(cpf_string):
    # TODO: implementar a lógica (Gustavo)
    pass
