

def leiaStr(mensagem):
    while True:  # Laço infinito
        entrada = input(mensagem)  # Solicita a entrada do usuário
        # Verifica se a entrada contém apenas letras e espaços
        if all(char.isalpha() or char.isspace() for char in entrada):
            return entrada  # Retorna a entrada se for válida
        else:
            print(
                "\33[31m Por favor, digite apenas letras e espaços. Números e caracteres especiais não são permitidos.\33[0m")


def leiaint(msg=0):
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






def convert(valor):
    if isinstance(valor, float):
        return str(f'{valor}')


def converter_float_para_string(valor):
    """Converte um float para string, substituindo '.' por ','."""
    if isinstance(valor, float):
        # Converte o float para string e substitui '.' por ','
        return str(f'{valor:.1f}').replace(',', '.')


def leiaFloat(msg=0):
    while True:
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

lista_alunos = [
    {"nome": "João", "nota": 6.5, "série":9},
    {"nome": "Maria", "nota": 8.0 , "série":9},
    {"nome": "Carlos", "nota": 3.5 , "série":9},
    {"nome": "Ana", "nota": 7.2 , "série":9},
    {"nome": "Lucas", "nota": 5.0 , "série":9},
]

aluno = {}

def adc_aluno(nm,nt,serie):
    aluno["nome"] = nm
    aluno["nota"] = nt
    aluno["série"] = serie
    
    
    
    return None

def situacao_aluno(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 4:
        return "Recuperação"
    else:
        return "Reprovado"
# aluno['situacao'] = situacao_aluno()
# Adiciona a situação ao dicionário
   

while True:
    no =leiaStr('Nome: ')
    nt = leiaFloat('Nota: ')
    ser =  leiaint ('Série: ')
    aluno['situacao'] = situacao_aluno(nt)
    
    
    adc_aluno(no,nt ,ser)
    res = ' '
    while res not in 'SN':
        res = leiaStr('Adcionar mais aluno? [S/N]').strip().upper()[0]
        if res == 'S':
            print('ok')
        else:
            print()
    break

lista_alunos.append(aluno)
for c , v in enumerate(lista_alunos):
    print(f'{c}:{v}')

