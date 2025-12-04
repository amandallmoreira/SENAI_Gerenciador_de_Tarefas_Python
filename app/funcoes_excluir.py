from app.funcoes_arquivo import salvar_tarefas_em_arquivo
from app.funcoes_configuracao import exibir_opcao_invalida

def deletar_tarefa(id_tarefa_deletar, tarefas):
    """Recebe o id da tarefa a ser deletada e a lista de tarefas e a remove"""
    deletou = False
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa_deletar:            
            tarefas.remove(tarefa)
            # atualiza o arquivo
            salvar_tarefas_em_arquivo(tarefas)
            deletou = True
            print("\nDeletada com sucesso.")
    if not deletou:
        exibir_opcao_invalida()
