from datetime import datetime
from app.funcoes_configuracao import caminho_arquivo

import os
import art as art


def carregar_tarefas_do_arquivo(tarefas):
    """Carrega tarefas do arquivo 'tarefas.txt', caso exista, e alimenta a lista de tarefas; caso não exista a lista começa vazia."""
    try:
        with open(caminho_arquivo("tarefas.txt"), "r", encoding="utf-8") as arq:
            # formação de um lista 'tarefas_arquivo' com cada linha do arquivo(cada tarefa) como item
            # tarefas_arquivo = lista com cada item = linha do arquivo
            tarefas_arquivo = arq.read().split("\n")
            print(tarefas_arquivo)
            # itera pelos itens da lista 'tarefas_arquivo'
            for tarefa_arquivo in tarefas_arquivo:  # cada linha do arquivo
                tarefa = {}
                # se o item for diferente de vazio entra no if
                if tarefa_arquivo != "":
                    # separa o item em partes a partir do separador ;
                    dados = tarefa_arquivo.split(";")
                    # atribui cada parte à chave correspondente no dicionário no type correto
                    tarefa["id"] = int(dados[0])  # int
                    tarefa["titulo"] = dados[1]  # str
                    tarefa["item"] = dados[2].split(":")  # list
                    tarefa["data"] = datetime.strptime(
                        dados[3], "%Y-%m-%d").date()
                    tarefa['hora'] = datetime.strptime(
                        dados[4], "%H:%M:%S").time()
                    # bool
                    tarefa["concluida"] = True if dados[5] == "True" else False
                    # add a tarefa à lista de tarefas do app
                    tarefas.append(tarefa)
    except:
        # caso o arquivo 'tarefas.txt' não exista ou vazio, a lista tarefas inicia vazia
        tarefas = []


def salvar_id_tarefa_em_arquivo(id_tarefa):
    """Salva no arquivo id_tarefa.txt o valor atual da variável id_tarefa para controle do número das tarefas"""
    arquivo = caminho_arquivo("id_tarefa.txt")
    with open(arquivo, "w") as arq:
        arq.write(str(id_tarefa))


def salvar_tarefa_em_arquivo(tarefa):
    """Recebe uma tarefa no formato dicionário e a adiciona na próxima linha do arquivo"""
    with open(caminho_arquivo("tarefas.txt"), "a", encoding="utf-8") as arq:
        id = tarefa["id"]
        titulo = tarefa["titulo"]
        item = ":".join(tarefa["item"])
        data = tarefa["data"]  # 0001-01-01
        hora = tarefa["hora"]  # 00:00:00
        concluida = tarefa["concluida"]
        linha = (f"{id};{titulo};{item};{data};{hora};{concluida};\n")
        arq.write(linha)


def salvar_tarefas_em_arquivo(tarefas):
    """Recebe a lista de tarefas e a salva no arquivo para consistência de dados """
    os.remove(caminho_arquivo("tarefas.txt"))
    with open(caminho_arquivo("tarefas.txt"), "a", encoding="utf-8") as arq:
        for tarefa in tarefas:
            arq.write(
                f"{tarefa['id']};{tarefa['titulo']};{':'.join(tarefa['item'])};{tarefa['data']};{tarefa['hora']};{tarefa['concluida']};\n"
            )
