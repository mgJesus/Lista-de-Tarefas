import os

def limpar_tela():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def pular_linha():
    print(      )

perguntar = input('Deseja adicionar uma tarefa na sua lista?\nR:')


def adicionar_item(lista_de_tarefas):

    tarefa = input('Qual tarefa vc deseja adicionar a sua lista?\nR:')
    lista_de_tarefas.append(tarefa)
    limpar_tela()
    
def main():
    lista_de_tarefas = []

    while True:
        limpar_tela()
    
        adicionar_item(lista_de_tarefas)

        continuar = input('Deseja adicionar mais alguma coisa?\nR:')
        limpar_tela()

        if continuar.upper() != 'SIM':  
            break
        
    if lista_de_tarefas:
        print('\nLISTA DE TAREFA')
        for i, lista_de_tarefas in enumerate(lista_de_tarefas, start=1):
            print(f'{i} {lista_de_tarefas}')
                

if __name__ == "__main__":
    main()