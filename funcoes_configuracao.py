# import funcoes internas python
import os

# import funcoes do sistema
from funcoes_configuracao import * #TODO Estamos em funcoes_configuracao
import art

# lista que armazena o conjunto de tarefas
tarefas = []

# id para número das tarefas
# tenta ler o arquivo id_tarefa.txt para atribuir o valor lido na variável id_tarefa
# se o arquivo não existir (primeira vez que o app é executado),
# atribui o valor 1 à variável id_tarefa
try:
    with open("id_tarefa.txt", "r") as arq:
        id_tarefa = int(arq.read().strip())
except:
    id_tarefa = 1

# limpa a tela
def limpar_tela():
    """Função que apaga todos os dados digitados no console realizando uma limpeza da tela com a finalidade de despoluição visual."""
    os.system('cls')

#imprime a Arte do menu
def imprimir_art():
    print(art.gtp)
    print("Por Amanda, Fabiana e Marcone")
    print("-" * 50)


def exibir_concluidas():
    global tarefas
    """Função que verica e exibe o número total de tarefas e o total de tarefas concluídas"""
    contador_concluidas = 0
    for tarefa in tarefas:
        if tarefa["concluida"] == True:
            contador_concluidas += 1
    print(" " * 40, "Pronto pra organizar seu dia?")
    print(" " * 40, f"Status: {contador_concluidas}/{len(tarefas)} concluídas")

# imprime menu
def imprimir_menu():
    """Função que imprime a logo, uma linha abaixo da logo e apresenta o menu com as opções para o usuário."""
    imprimir_art()
    exibir_concluidas()
    print("=== Suas Tarefas ===")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Concluir")
    print("4. Excluir")
    print("0. Sair")

#imprime opção invalida caso o usuario digite uma opção errada
def exibir_opcao_invalida():
    print("=== Opção Inválida! ===")

#exibe a Tarefa cadastrada com o Status Pendente
def exibir_tarefa(tarefa):
    print(f'\n=== Tarefa {tarefa["id"]} ===')
    print(f'Título: {tarefa["titulo"]}')
    print("Itens:")
    for item in tarefa["item"]:
        print(f'- {item}')    
    print("Status: Concluída" if tarefa["concluida"] == True else "Status: Pendente")   