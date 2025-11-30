from funcoes_arquivo import salvar_tarefas_em_arquivo
from funcoes_excluir import deletar_tarefa

#Função que marca a conclusão da tarefa
def marcar_concluida(id_tarefa_concluir, tarefas):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa_concluir:
            tarefa["concluida"] = True
            # atualiza o arquivo
            salvar_tarefas_em_arquivo(tarefas)
            print("\nConcluída com sucesso!")            
    opcao = input(
        "Excluir a tarefa concluída? ('1' para sim, 'Enter' para não):")
        #Opção para deletar a tarefa após a sua conclusão
    if opcao == "1":
        deletar_tarefa(int(id_tarefa_concluir))
        input("\nPressione 'Enter' para continuar...")
    else:
        #Retorna ao Menu Inicial
        return