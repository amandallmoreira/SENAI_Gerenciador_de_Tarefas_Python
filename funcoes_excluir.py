from funcoes_arquivo import salvar_tarefas_em_arquivo
from funcoes_configuracao import exibir_opcao_invalida

#DELETAR
def deletar_tarefa(id_tarefa_deletar, tarefas):
    #Começa com a tarefa não deletada
    deletou = False
    for tarefa in tarefas:
        #Se o id da tarefa a ser deletada for igual ao id digitado pelo usuario
        # a tarefa será removida
        if tarefa["id"] == id_tarefa_deletar:            
            tarefas.remove(tarefa)
            # atualiza o arquivo
            salvar_tarefas_em_arquivo(tarefas)
            deletou = True
            print("\nDeletada com sucesso.")
    if not deletou:
        #Caso o id da tarefa não corresponda ao digitado pelo usuario
        exibir_opcao_invalida()
