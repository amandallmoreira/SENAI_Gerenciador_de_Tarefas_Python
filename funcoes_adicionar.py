from funcoes_arquivo import salvar_id_tarefa_em_arquivo, salvar_tarefa_em_arquivo

def cadastrar_tarefa(tarefas, id_tarefa, titulo, itens):   
    # controle do status da tarefa: concluída(True), pendente(False)
    concluida = False
    # dicionario que armazena temporariamente cada tarefa
    tarefa = {}
    # alimento o dicionário tarefa com os dados das variáveis informados pelo usuário
    # {chave: valor, chave: valor, chave: ["", "", ""], chave:valor},
    tarefa["id"] = id_tarefa # int global
    tarefa["titulo"] = titulo # str
    tarefa["item"] = itens # list
    tarefa["concluida"] = concluida # bool
    # incrementa id_tarefa para controle do número de cada tarefa e salva o valor em arquivo
    id_tarefa += 1
    salvar_id_tarefa_em_arquivo(id_tarefa)
    # alimenta a lista de tarefas com o dicionário gerado no passo anterior
    tarefas.append(tarefa)
    print("\nTarefa adicionada.")
    # salvar tarefa em arquivo
    salvar_tarefa_em_arquivo(tarefa)