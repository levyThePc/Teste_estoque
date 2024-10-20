class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def remover_estoque(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            return True
        else:
            return False

    def __str__(self):
        return f"{self.nome} - Preço: R${self.preco:.2f} - Estoque: {self.quantidade}"

class Loja:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print("Produtos disponíveis na loja:")
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. {produto}")

    def selecionar_produto(self, indice):
        if 0 < indice <= len(self.produtos):
            return self.produtos[indice - 1]
        else:
            print("Produto inválido.")
            return None

class Carrinho:
    def __init__(self):
        self.itens = []

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
                print(f"\33[34m {produto.nome} - Quantidade: {qtd} - Preço total: R${produto.preco * qtd:.2f}\33[0m")
                total += produto.preco * qtd
            print(f"Total a pagar: R${total:.2f}")

# Simulação da loja
def main():
    loja = Loja()
    
    # Adicionando produtos à loja
    loja.adicionar_produto(Produto("Teclado", 100.00, 10))
    loja.adicionar_produto(Produto("Mouse", 50.00, 15))
    loja.adicionar_produto(Produto("Monitor", 800.00, 5))
    loja.adicionar_produto(Produto("Cadeira Gamer", 1200.00, 3))
    
    carrinho = Carrinho()
    
    while True:
        print("\n--- Menu da Loja ---")
        loja.listar_produtos()
        opcao = input("\33[32m Digite o número do produto que deseja comprar ou 'finalizar' para encerrar: \33[0m")

        if opcao.lower() == "finalizar":
            break
        elif opcao.isdigit():
            indice_produto = int(opcao)
            produto_selecionado = loja.selecionar_produto(indice_produto)

            if produto_selecionado:
                quantidade = int(input(f"Quantas unidades de {produto_selecionado.nome} você deseja comprar? "))
                carrinho.adicionar_item(produto_selecionado, quantidade)
        else:
            print("Opção inválida.")

    carrinho.exibir_carrinho()

if __name__ == "__main__":
    main()


