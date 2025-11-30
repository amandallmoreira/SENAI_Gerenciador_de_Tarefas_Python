from funcoes_configuracao import limpar_tela, exibir_tarefa
import art

def imprimir_menu_listar_tarefas():
    """Imprime o menu da opção listar do menu principal"""    
    print("1. Todas")
    print("2. Concluídas")
    print("3. Pendentes")
    print("0. Voltar")

def listar_tarefas(tarefas):    
    if tarefas == []:
        print("\nNenhuma tarefa encontrada.")
        input("\nPressione 'Enter' para continuar...")
    else:        
        imprimir_menu_listar_tarefas()
        op = input("Escolha uma opção: ")
        
        # listar todas as tarefas        
        if op == "1":
            limpar_tela()
            print(art.tarefas)            
            for tarefa in tarefas:
                exibir_tarefa(tarefa)
            input("\nPressione 'Enter' para continuar...")

        # listar apenas as concluídas        
        elif op == "2":
            limpar_tela()
            print(art.concluidas)
            concluidas = 0            
            for tarefa in tarefas:
                if tarefa["concluida"] == True:
                    concluidas += 1
                    exibir_tarefa(tarefa)
            if concluidas == 0:
                print("\nNenhuma tarefa concluída.")
            input("\nPressione 'Enter' para continuar...")

        # listar apenas as não concluídas
        elif op == "3":          
            limpar_tela()
            print(art.pendentes)  
            nao_concluida = 0            
            for tarefa in tarefas:
                if tarefa["concluida"] == False:
                    nao_concluida += 1
                    exibir_tarefa(tarefa)
            if nao_concluida == 0:
                print("\nNenhuma tarefa pendente.")
            input("\nPressione 'Enter' para continuar...")

        # retornar sem listar
        else:
            return