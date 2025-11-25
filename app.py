# import funcoes do projeto
from funcoes import *

# variável para controle do loop
continuar_programa = True

# fluxo do programa
while continuar_programa:
    print(numero_tarefa)

    # salvar número da tarefa para controle
    salvar_em_arquivo_numero_tarefa()    
    
    # função para imprimir a logo e o menu    
    imprimir_menu()

    # captura a opcao do usuario
    opcao = input("Escolha uma opção: ")

    # cadastrar tarefa
    if opcao == "1":        
        #limpa a tela no Windows
        limpar_tela()
        
        # captura os dados da tarefa com input e os armazena em variáveis
        print("\n=== Nova Tarefa ===")
        
        # captura o título da tarefa com input e o armazena na variável 'titulo'
        titulo = input("Informe o titulo: ").title()

        # controle para impedir título vazio: interrompe o fluxo e retorna ao menu
        if titulo == "":
            print("\nTítulo é obrigatório. A tarefa não foi cadastrada.")            
            input("\nPressione Enter para continuar...")
            limpar_tela()
            continue

        # lista de itens: recebe cada item cadastrado pelo usuário
        itens = []
        
        # variável controle sair do loop do 'item'
        maisItens = True
        
        print("\nInforme o item (0 para sair)")

        # loop que alimenta a lista de itens
        while maisItens:
            # captura o item da tarefa com input e o armazena na variável 'item'            
            item = input("Digite o item: ").title()            
            if item == "0":
                maisItens = False
            else:
                # controle para impedir que item vazio seja adicionado à lista de itens
                if item != "":
                    itens.append(item)
        
        # verifica se itens está vazio e interrompe o fluxo caso esteja        
        if itens == []:
            print("\nItem é obrigatório. A tarefa não foi cadastrada.")            
            input("\nPressione Enter para continuar...")
            limpar_tela()
            continue

        # função para gerar a lista de tarefas       
        cadastrar_tarefa(titulo, itens)             
        input("\nPressione Enter para continuar...") 

    # listar tarefa
    elif opcao == "2":        
        listar_tarefas()                

    # marcar tarefa como concluída
    elif opcao == "3":
        limpar_tela()
        # controle das tarefas que não foram concluídas
        tarefas_a_deletar = []
        for tarefa in tarefas:
                if tarefa["concluida"] == False:
                    # add na lista das tarefas que não foram concluídas
                    tarefas_a_deletar.append(str(tarefa["numero"]))        
                    # exibe as tarefas que não foram concluídas            
                    exibir_tarefa(tarefa)
        if tarefas_a_deletar == []:
            imprimir_art()
            print("\nNenhuma tarefa pendente.")
            input("\nPressione 'Enter' para continuar...")
        else:                
            numero_tarefa = input("\nNúmero da tarefa: ")            
            # verifica se usuário escolheu tarefa constante da lista
            if numero_tarefa in tarefas_a_deletar:
                marcar_concluida(numero_tarefa)
            else:
                # informa erro se opcao não estiver na lista
                exibir_opcao_invalida()
                input("\nPressione 'Enter' para continuar...")           
                    
        

    # deletar tarefa
    elif opcao == "4":
        limpar_tela()
        tarefas_a_deletar = []
        for tarefa in tarefas:                
            # add na lista das tarefas que não foram concluídas
            tarefas_a_deletar.append(str(tarefa["numero"]))        
            # exibe as tarefas que não foram concluídas            
            exibir_tarefa(tarefa)
        if tarefas_a_deletar == []:
            imprimir_art()
            print("\nNenhuma tarefa encontrada.")
            input("\nPressione 'Enter' para continuar...")
        else:                
            numero_tarefa = input("\nNúmero da tarefa: ")            
            # verifica se usuário escolheu tarefa constante da lista
            if numero_tarefa in tarefas_a_deletar:
                deletar_tarefa(int(numero_tarefa))
            else:
                # informa erro se opcao não estiver na lista
                exibir_opcao_invalida()
                input("\nPressione 'Enter' para continuar...")                

    # sair do programa
    elif opcao == "0":
        continuar_programa = False

    # nenhuma das opções anteriores
    else:
        exibir_opcao_invalida()

    #limpa a tela no Windows
    limpar_tela()
