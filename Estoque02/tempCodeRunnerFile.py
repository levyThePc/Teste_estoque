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