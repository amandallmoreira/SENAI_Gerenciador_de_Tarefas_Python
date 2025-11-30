from funcoes_configuracao import id_tarefa

import os
import art as art

def carregar_tarefas_do_arquivo(tarefas):
    """Carrega tarefas do arquivo 'tarefas.txt', caso exista, e alimenta a lista de tarefas; caso não exista a lista começa vazia."""        
    try:        
        with open("tarefas.txt", "r", encoding="utf-8") as arq:
            # formação de um lista 'tarefas_arquivo' com cada linha do arquivo(cada tarefa) como item            
            tarefas_arquivo = arq.read().split("\n")
            # itera pelos itens da lista 'tarefas_arquivo'            
            for tarefa_arquivo in tarefas_arquivo:                
                tarefa = {}
                # se o item for diferente de vazio entra no if
                if tarefa != "":
                    # separa o item em partes a partir do separador ;
                    dados = tarefa_arquivo.split(";")                
                    # atribui cada parte à chave correspondente no dicionário no type correto    
                    tarefa["id"] = int(dados[0]) # int
                    tarefa["titulo"] = dados[1] # str
                    tarefa["item"] = dados[2].split(":") # list
                    tarefa["concluida"] = True if dados[3] == "True" else False # bool
                    # add a tarefa à lista de tarefas do app                    
                    tarefas.append(tarefa)
                    
    except:
        # caso o arquivo 'tarefas.txt' não exista ou vazio, a lista tarefas inicia vazia        
        tarefas = []

def salvar_id_tarefa_em_arquivo(id_tarefa):
    """Salva no arquivo id_tarefa.txt o valor atual da variável id_tarefa para controle do número das tarefas"""    
    arquivo = "id_tarefa.txt"
    with open(arquivo, "w") as arq:
        arq.write(str(id_tarefa))


def salvar_tarefa_em_arquivo(tarefa):    
    with open("tarefas.txt", "a", encoding="utf-8") as arq:
        numero = tarefa["id"]
        titulo = tarefa["titulo"]
        item = ":".join(tarefa["item"])
        concluida = tarefa["concluida"]
        linha = (f"{numero};{titulo};{item};{concluida};\n")
        arq.write(linha)           


def salvar_tarefas_em_arquivo(tarefas):    
    os.remove("tarefas.txt")
    with open("tarefas.txt", "a", encoding="utf-8") as arq:
        for tarefa in tarefas:
            arq.write(
                f"{tarefa['id']};{tarefa['titulo']};{':'.join(tarefa['item'])};{tarefa['concluida']};\n")    
