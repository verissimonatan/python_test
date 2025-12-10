'''def test_multiply():
    # Define o primeiro número
    a = 2
    # Define o segundo número
    b = 3
    # Realiza a operação de multiplicação
    multiply = a * b
    # Verifica se o usuário obtém o resultado esperado
    assert multiply == 6'''


# Função que inverte uma string
def reverse_string(word):
    return ''.join(reversed(word))


# Teste. Verificação da função reverse_string
def test_reverse_string():
    input_str = "TripleTen"

    # Realize a operação inversa
    reversed_str = reverse_string(input_str)

    # Verifique se a string invertida corresponde ao resultado esperado
    assert reversed_str == "neTelpirT"

    print("Teste Aprovado! " + input_str + " invertido é " + reversed_str)