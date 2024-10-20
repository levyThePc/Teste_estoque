class Elevador:
    def __init__(self, andar_atual=1):
        self.andar_atual = andar_atual

    def mover_para_andar(self, andar):
        if 1 <= andar <= 10:
            if andar == self.andar_atual:
                print(f"Você já está no andar {andar}.")
            else:
                print(f"Movendo do andar {self.andar_atual} para o andar {andar}...")
                self.andar_atual = andar
                print(f"O elevador chegou ao andar {andar}.")
        else:
            print("Andar inválido! Escolha um número entre 1 e 10.")



def painel_elevador():
    elevador = Elevador()
    while True:
        print(f"\nVocê está no andar {elevador.andar_atual}.")
        andar = input("Escolha o andar (1-10) ou digite 'sair' para finalizar: ")

        if andar.lower() == 'sair':
            print("Encerrando o painel do elevador. Até logo!")
            break
        elif andar.isdigit():
            elevador.mover_para_andar(int(andar))
        else:
            print("Entrada inválida! Tente novamente.")

# Inicia o painel do elevador
painel_elevador()



   
    
   
            
    








        