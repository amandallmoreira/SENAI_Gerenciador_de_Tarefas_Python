# import funcoes internas python
import os
from datetime import datetime, date, time

# import funcoes do sistema
from app.funcoes_datetime import verificar_data_semana
import art

# lista que armazena o conjunto de tarefas
tarefas = []


# Caminho da pasta onde este arquivo está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Sobe um nível
RAIZ = os.path.dirname(BASE_DIR)
# Caminho da pasta arq dentro da raiz
PASTA_ARQ = os.path.join(RAIZ, "arq")


def caminho_arquivo(nome):
    """Recebe o nome do arquivo e retorna o caminho absoluto para o mesmo"""
    return os.path.join(PASTA_ARQ, nome)


# id para número das tarefas
# tenta ler o arquivo id_tarefa.txt para atribuir o valor lido na variável id_tarefa
# se o arquivo não existir (primeira vez que o app é executado),
# atribui o valor 1 à variável id_tarefa
try:
    with open(caminho_arquivo("id_tarefa.txt"), "r") as arq:
        id_tarefa = int(arq.read().strip())
except:
    id_tarefa = 1

# limpa a tela


def limpar_tela():
    """Função que apaga todos os dados digitados no console realizando uma limpeza da tela com a finalidade de despoluição visual."""
    os.system('cls')


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


def exibir_opcao_invalida():
    print("=== Opção Inválida! ===")

# def exibir_tarefa(tarefa):
#     print(f'\n=== Tarefa {tarefa["id"]} ===')
#     print(f'Título: {tarefa["titulo"]}')
#     print("Itens:")
#     for item in tarefa["item"]:
#         print(f'- {item}')
#     print("Status: Concluída" if tarefa["concluida"] == True else "Status: Pendente")


def exibir_tarefa(tarefa):
    dia_semana = ["Domingo", "Segunda-feira", "Terça-feira",
                  "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
    mes = ["jan", "fev", "mar", "abr", "mai", "jun",
           "jul", "ago", "set", "out", "nov", "dez"]

    print(f'\n=== Tarefa {tarefa["id"]} ===')
    print(f'{tarefa["titulo"]}:')
    for item in tarefa["item"]:
        print(f'- {item}')
    # verifica se data diferente de vazia
    if tarefa["data"] != date(datetime.min.year, datetime.min.month, datetime.min.day):
        data_formatada = tarefa["data"].strftime("%d/%m/%Y")  # 15/01/2026
        data_exibida = "Em " + data_formatada  # Em 15/01/2026
        # verifica se a data está na próxima semana (< 7)
        if verificar_data_semana(tarefa["data"]):
            semana_formatada = tarefa["data"].strftime(
                "%A")  # dia da semana: Monday
            if semana_formatada == "Sunday":
                semana_formatada = dia_semana[0]
            elif semana_formatada == "Monday":
                # dia da semana: segunda-feira
                semana_formatada = dia_semana[1]
            elif semana_formatada == "Tuesday":
                semana_formatada = dia_semana[2]
            elif semana_formatada == "Wednesday":
                semana_formatada = dia_semana[3]
            elif semana_formatada == "Thursday":
                semana_formatada = dia_semana[4]
            elif semana_formatada == "Friday":
                semana_formatada = dia_semana[5]
            else:
                semana_formatada = dia_semana[6]

            mes_formatado = tarefa["data"].month
            mes_formatado = mes[mes_formatado-1]
            dia_formatado = tarefa["data"].day

            data_exibida = semana_formatada + ", " + \
                str(dia_formatado) + "/" + \
                mes_formatado  # Segunda-feira, 05/dez

        if tarefa["hora"] != time(datetime.min.hour, datetime.min.minute):
            hora_formatada = tarefa["hora"].strftime("%H:%M")
            print(data_exibida, " às ", hora_formatada)
        else:
            print(data_exibida)
    print("Status: Concluída" if tarefa["concluida"]
          == True else "Status: Pendente")
