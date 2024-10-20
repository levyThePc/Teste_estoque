from time import sleep
import json
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
            return n


def carregar_dados_json(nome_arquivo):
    """Carrega dados de um arquivo JSON."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return None

# Nome do arquivo JSON
nome_arquivo = 'estoque.json'

# Carregando os dados
dados_estoque = carregar_dados_json(nome_arquivo)

if dados_estoque is not None:
    print("Dados carregados com sucesso")
    #print(dados_estoque)
else:
    print("Nenhum dado foi carregado.")

def exibir_menu():
    print("\33[35m \n=== Menu de Controle de Estoque === \33[0m")
    print("\33[33m 1. Adicionar Produto \33[0m")
    print("\33[33m 2. Listar Produtos \33[0m")
    print("\33[33m 3. Atualizar Produto \33[0m")
    print("\33[33m 4. Remover Produto \33[0m")
    print("\33[31m 0. Sair \33[0m")
    print("===================================")

def salvar_estoque(estoque, nome_arquivo='estoque.json'):
    """Salva o dicionário de estoque em um arquivo JSON."""
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(estoque, arquivo, ensure_ascii=False, indent=4)
    print(f"Dados salvo no arquivo '{nome_arquivo}' com sucesso!")

def carregar_estoque(nome_arquivo='estoque.json'):
    """Carrega o dicionário de estoque de um arquivo JSON, se existir."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}  # Retorna um dicionário vazio se o arquivo não existir

def adicionar_produto(estoque='<produto>'):
    nome = input("Digite o nome do produto: ")
    quantidade = leiaint("Digite a quantidade: ")
    preco = leiaFloat("Digite o preço: ")
    estoque[nome] = {'quantidade': quantidade, 'preco': preco}
    print(f"Produto '{nome}' adicionado com sucesso!")
    salvar_estoque(estoque)  # Salva após adicionar

def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    print("\n=== Lista de Produtos ===")
    for nome, detalhes in estoque.items():
        print(f"Produto: {nome}, Quantidade: {detalhes['quantidade']}, Preço: R${detalhes['preco']:.2f}")

def atualizar_produto(estoque):
    for nome, detalhes in estoque.items():
        print(f"Produto: {nome}, Quantidade: {detalhes['quantidade']}, Preço: R${detalhes['preco']:.2f}")
    nome = input("Digite o nome do produto a ser atualizado: ")
    if nome in estoque:
        quantidade = int(input("Digite a nova quantidade: "))
        preco = float(input("Digite o novo preço: "))
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f"Produto '{nome}' atualizado com sucesso!")
        salvar_estoque(estoque)  # Salva após atualizar
    else:
        print(f"Produto '{nome}' não encontrado.")

def remover_produto(estoque):
    for nome, detalhes in estoque.items():
        print(f"Produto: {nome}, Quantidade: {detalhes['quantidade']}, Preço: R${detalhes['preco']:.2f}")
    nome = input("Digite o nome do produto a ser removido: ")
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso!")
        salvar_estoque(estoque)  # Salva após remover
    else:
        print(f"Produto '{nome}' não encontrado.")

def main():
    estoque = carregar_estoque()  # Carrega o estoque ao iniciar
    while True:
        exibir_menu()
        opcao = input(" \33[32m Escolha uma opção:  \33[0m")
        
        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            listar_produtos(carregar_dados_json(nome_arquivo))
        elif opcao == '3':
            atualizar_produto(estoque)
        elif opcao == '4':
            remover_produto(estoque)
        elif opcao == '0':
            sleep(1)
            print("\33[31m Encerrando do sistema...\33[0m")
            sleep(1.5)
            print('\33[32m Sistema Encerrado, até Logo 👋\33[0m')
            break
        else:
            print(" \33[31m Opção inválida. Tente novamente. \33[0m")

# Executa o sistema
if __name__ == "__main__":
    main()
input()