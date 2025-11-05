from solucoes import sao_anagramas, valida_cpf

def test_sao_anagramas():
    assert sao_anagramas("amor", "roma") == True
    assert sao_anagramas("A gentleman", "Elegant man") == True
    assert sao_anagramas("gato", "cabra") == False
    print("Todos os testes passaram!")

def test_valida_cpf():
    assert valida_cpf("12345678909") == True
    assert valida_cpf("") == False
    assert valida_cpf("111111111111") == False
    assert valida_cpf("12345678977") == False
    print("Todos os testes passaram!")


if __name__ == "__main__":
    test_sao_anagramas()
    test_valida_cpf()