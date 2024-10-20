'''Sistema de Loja
Desenvolva um sistema de gerenciamento de uma loja. Crie uma classe Produto com atributos como nome, preco e quantidade_em_estoque.
 Crie uma classe Loja que gerencie os produtos.

Tarefas:

Crie métodos para adicionar produtos, vender produtos e exibir o estoque.
Adicione uma funcionalidade para reabastecer o estoque de um produto específico.'''

class Produto:
    def __init__(self,nome='<produto>',preco=0,quantidade_em_estoque=0):
        self.nome_produto = nome
        self.preco = preco
        self.quant_estq = quantidade_em_estoque

    def adicionar_produtos(self,qtd):
        if qtd <= self.quant_estq:
            self.quant_estq -= qtd
            return True
        else:
            return False
    def __str__(self):
        return f'{self.nome_produto} - Preço:{self.preco:.2f}- Estoque: {self.quant_estq}'


class Loja:
    def __init__(self):
        self.produtos =[]
    
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
    
    def lista_produtos(self):
        print('Produtos Disponiveis na Loja:')
        for i,produtos in enumerate(self.produtos, start=1):
            print(f"{i}.{produtos}")
    
    def selecionar_produto(self, indice):
        if 0 < indice <= len(self.produtos):
            return self.produtos[indice-1]
        else:
            print('Produto inválido.')
            return None

class Carrinho:
    def __init__(self):
        self.itens= []
    def adicionar_item(self, produto, quantidade):
        if produto.remover_estoque(quantidade):
            self.itens.append((produto, quantidade))
            print(f"{quantidade} unidade(s) de {produto.nome} adicionado(s) ao carrinho.")
        else:
            print(f"Estoque insuficiente para {produto.nome}.")
    def exibir_carrinho(self):
        if not self.itens:
            print("O carrinho está vazio.")
        else:
            print("Itens no carrinho:")
            total = 0
            for produto, qtd in self.itens:
                print(f"{produto.nome} - Quantidade: {qtd} - Preço total: R${produto.preco * qtd:.2f}")
                total += produto.preco * qtd
            print(f"Total a pagar: R${total:.2f}")

#Simulação Da Loja

def main():
    loja = Loja()

    #Adicionar Produtos à Loja
    loja.adicionar_produtos(Produto("Teclado", 100.00, 10))
    loja.adicionar_produtos(Produto('Mouse',50.00, 15))
    loja.adicionar_produtos(Produto('Monitor',800.00,5))
    loja.adicionar_produtos(Produto('Cadeira Gamer',1200.00,3))

    carrinho = Carrinho()

    while True:
        print('\n---Menu Da Loja---')
        loja.lista_produtos()
        opcao = input('Digite o produto que deseja  comprar ou (Finalizar) para encerrar:  ')
        if opcao.lower() == 'finalizar':
            break
        elif opcao.isdigit():
            indice_produto = int(opcao)
            produto_selecionado = loja.selecionar_produto(indice_produto)

            if produto_selecionado:
                quantidade = int(input(f'Quantas unidades de {produto_selecionado} você deseja comprar?'))
                carrinho.adiconar_item(produto_selecionado, quantidade)
            else:
                print('Opção Inválida')

    carrinho.exibir_carrinho()
if __name__ == "__main__":
    main()
    



        
        
        


        