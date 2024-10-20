import json




def exibir_menu():
    print("=" * 30)
    print("          MENU          ")
    print("=" * 30)
    print("1. Adicionar Produto")
    print("2. Escolher Produto")
    print("3. Vizualizar Estoque")
    print("0. Sair")
    print("=" * 30)


# Exemplo de uso
exibir_menu()

estoque = {}

def adc_estoque(nome, quantidade, preco):
    estoque["nome"] = nome
    estoque["quantidade"] = quantidade
    estoque["preço"] = preco

def ratira_estoq(produto,quantidade):
    ...



def Opcao_esc(opc=0):
    try:
        while True:
            opc = int(input('Digite sua Opção >>> '))
            if opc not in (0,1,2,3):
                print('opção inválida') 
            if opc == 1:
                n = str(input('Nome: '))
                q = int(input('Quantidade: '))
                p = float(input('Preço: '))
                adc_estoque(n,q,p)
            if opc == 2:
                print('opc 2')
            if opc == 3:
                print('opc 3')
            if opc == 0:
                break  
            if opc not in (0,1,2,3):
                print('opção inválida')          
    except ValueError:
        print(f' inválida')
        
              
Opcao_esc()









