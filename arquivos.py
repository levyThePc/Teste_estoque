def leiaStr(mensagem):
    while True:  # Laço infinito
        entrada = input(mensagem)  # Solicita a entrada do usuário
        # Verifica se a entrada contém apenas letras e espaços
        if all(char.isalpha() or char.isspace() for char in entrada):
            return entrada  # Retorna a entrada se for válida
        else:
            print("Por favor, digite apenas letras e espaços. Números não são permitidos.")

# Exemplo de uso
resultado = leiaStr("Digite uma string (somente letras e espaços): ")
print(f"A string digitada foi: {resultado}")

        