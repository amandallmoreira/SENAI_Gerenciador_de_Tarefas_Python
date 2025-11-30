from funcoes_arquivo import salvar_tarefas_em_arquivo
from funcoes_configuracao import exibir_opcao_invalida

def deletar_tarefa(id_tarefa_deletar, tarefas):
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
