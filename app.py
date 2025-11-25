# import funcoes do projeto
from funcoes import *

# variável para controle do loop
continuar_programa = True

# fluxo do programa
while continuar_programa:    
    
    # função para imprimir a logo e o menu    
    imprimir_menu()

    # captura a opcao do usuario
    opcao = input("Digite sua opção: ")

    # cadastrar tarefa
    if opcao == "1":        
        #limpa a tela no Windows
        limpar_tela()
        
        # captura os dados da tarefa com input e os armazena em variáveis
        print("\n*** DADOS DA TAREFA ***")
        
        # captura o título da tarefa com input e o armazena na variável 'titulo'
        titulo = input("Digite o titulo: ").title()

        # controle para impedir título vazio: interrompe o fluxo e retorna ao menu
        if titulo == "":
            print("\n*** Título obrigatório - Tarefa não cadastrada! ***")            
            input("\nPressione Enter para continuar...")
            limpar_tela()
            continue

        # lista de itens: recebe cada item cadastrado pelo usuário
        itens = []
        
        # variável controle sair do loop do 'item'
        maisItens = True
        
        print("*** Digite o item ou 0 para sair. ***\n")

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
            print("\n*** Item obrigatório - Tarefa não cadastrada! ***")            
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
        for tarefa in tarefas:                    
                print(f"\n*** TAREFA {tarefa["numero"]} ***")
                print(tarefa["Título"])
                for elemento in tarefa["Item"]:
                    print(f'- {elemento}')                
        numero_tarefa = int(input("\nDigite a tarefa que quer marcar como concluída: "))
        marcar_concluida(numero_tarefa)
        input("\nPressione Enter para continuar...")        

    # deletar tarefa
    elif opcao == "4":
        limpar_tela()
        for tarefa in tarefas:                    
                print(f"\n*** TAREFA {tarefa["numero"]} ***")
                print(tarefa["Título"])
                for elemento in tarefa["Item"]:
                    print(f'- {elemento}')
                if tarefa["concluida"] == True:    
                    print("Concluída: ✔")        
                else:
                    print("Concluída: ❌")
        numero_tarefa = int(input("\nDigite a tarefa que quer deletar: "))
        deletar_tarefa(numero_tarefa)
        input("\nPressione Enter para continuar...")        

    # sair do programa
    elif opcao == "0":
        continuar_programa = False

    # nenhuma das opções anteriores
    else:
        print("Opção inválida")

    #limpa a tela no Windows
    limpar_tela()
