from solucoes import sao_anagramas

def test_sao_anagramas():
    assert sao_anagramas("amor", "roma") == True
    assert sao_anagramas("A gentleman", "Elegant man") == True
    assert sao_anagramas("gato", "cabra") == False
    print("Todos os testes passaram!")


if __name__ == "__main__":
    test_sao_anagramas()