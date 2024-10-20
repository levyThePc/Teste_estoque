

estoque_produto = {}
novo_estoque = estoque_produto

def exibir_menu():
    print("=" * 30)
    print("\33[32m         MENU          \33[0m")
    print("=" * 30)
    print("\33[33m 1. Adicionar Produto \33[0m")
    print("\33[33m 2. Escolher Produto \33[0m")
    print("\33[33m 3. Vizualizar Estoque \33[0m")
    print("\33[31m 0. Sair \33[0m")
    print("=" * 30)
    
def converter_float_para_string(valor):
    """Converte um float para string, substituindo '.' por ','."""
    if isinstance(valor, float):
        # Converte o float para string e substitui '.' por ','
        return str(f'{valor:.2f}').replace('.', ',')

    else:
        raise ValueError("O valor deve ser um float.")

def leiaint(msg = 0):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            
            print('\33[31m ERRO!! Digite um número inteiro válido.\33[0m')
            
            continue
        except KeyboardInterrupt:
            print('\33[36m O usuário preferio não digitar seus dados \33[0m')
            print('Volte logo')
            return 0
        else:
            return n
def leiaFloat(msg = 0):
    while  True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[31m ERRO!! Digite um número real válido. \33[0m')
            continue
            
        except KeyboardInterrupt:
            
            print('\33[36m O usuário preferio não digitar seus dados \33[0m')
            print('Volte logo')
            return 0
        else:
            return converter_float_para_string(n)



def cadastrar_prod(nome,estoque=0,preco=0):
    
    estoque_produto["nome"] = nome
    estoque_produto["preço R$"] = preco
    estoque_produto["estoque"] = estoque
    
def escolha_menu(opc_s):
    while True:
        if opc_s == 1:
            n = str(input('Nome do Produto: '))
            qtd = leiaint('Quantidade: ')
            pre_pro = leiaFloat('Preço:')
            cadastrar_prod(n,qtd,pre_pro)

        if opc_s == 2:
            tam = len(estoque_produto['nome'])
            for n in enumerate(estoque_produto):
                print(f"{n} Produto:{estoque_produto['nome']},Estoque:{estoque_produto['estoque']},Preço:{estoque_produto['preço R$']}")

        if opc_s == 3:
            for chave,valor in estoque_produto.items():
                print(f'{chave}:{valor}')
                break
        
        else:
            break

        



       
    

while True:
    exibir_menu()
    esc = leiaint('Sua Opção>>> ')
    escolha_menu(esc)
    if escolha_menu(0):
        break
   