from app.funcoes_arquivo import salvar_tarefa_em_arquivo

def cadastrar_tarefa(tarefas, id, titulo, itens, data, hora):
    """Recebe a lista de tarefas, id, titulo, a lista de itens, data e hora, gera um novo dicionário e o adiciona à lista de tarefas e o salva em arquivo para consistência dos dados"""   
    # controle do status da tarefa: concluída(True), pendente(False)
    concluida = False
    # dicionario que armazena temporariamente cada tarefa
    tarefa = {}
    # alimento o dicionário tarefa com os dados das variáveis informados pelo usuário
    # {chave: valor, chave: valor, chave: ["", "", ""], chave:valor, chave:valor, chave:valor},
    tarefa["id"] = id # int global
    tarefa["titulo"] = titulo # str
    tarefa["item"] = itens # list
    tarefa['data'] = data # date
    tarefa['hora'] = hora # time
    tarefa["concluida"] = concluida # bool    
    # alimenta a lista de tarefas com o dicionário gerado no passo anterior
    tarefas.append(tarefa)
    print("\nTarefa adicionada.")
    # salvar tarefa em arquivo
    salvar_tarefa_em_arquivo(tarefa)