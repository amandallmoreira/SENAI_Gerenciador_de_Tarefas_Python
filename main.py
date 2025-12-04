from datetime import date, datetime, time

# import funcoes do projeto
from app.funcoes_adicionar import cadastrar_tarefa
from app.funcoes_arquivo import salvar_tarefas_em_arquivo, carregar_tarefas_do_arquivo, salvar_id_tarefa_em_arquivo
from app.funcoes_excluir import deletar_tarefa
from app.funcoes_listar import listar_tarefas
from app.funcoes_concluir import marcar_concluida
from app.funcoes_configuracao import tarefas, id_tarefa, limpar_tela, exibir_tarefa, imprimir_menu, imprimir_art, exibir_opcao_invalida
from app.funcoes_datetime import cadastrar_data, cadastrar_hora, gerar_data_vazia, gerar_hora_vazia
import art

# variável para controle do loop
continuar_programa = True

# carregar tarefas do arquivo caso exista
carregar_tarefas_do_arquivo(tarefas)
# fluxo do programa
while continuar_programa:
    # limpa a tela no Windows
    limpar_tela()
    # função para imprimir a logo e o menu
    imprimir_menu()
    # captura a opcao do usuario
    opcao = input("Escolha uma opção: ")
    # cadastrar nova tarefa
    if opcao == "1":
        # limpa a tela no Windows e imprime a logo adicionar
        limpar_tela()
        print(art.adicionar)
        # captura os dados da tarefa com input e os armazena em variáveis
        print("=== Nova Tarefa ===")
        id = id_tarefa
        id_tarefa += 1
        salvar_id_tarefa_em_arquivo(id_tarefa)
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

        # verifica se o usuário dejesa inserir data e/ou hora no cadastro da tarefa    
        opcao_data = input("\nDigite 'd' para data ou 'Enter' para concluir: ").lower()
        # caso o usuário resolva adicionar data à tarefa
        if opcao_data == "d":
            # opcao do usuario para data
            data = cadastrar_data()
            # controle para evitar inserir hora quando o usuário não inseriu data
            # para inserir hora é obrigatório inserir data           
            if data != gerar_data_vazia():  # 0001-01-01
                # verifica se o usuário deseja inserir hora no cadastro da tarefa
                opcao_hora = input("\nDigite 'h' para hora ou 'Enter' para concluir: ").lower()
                if opcao_hora == 'h':
                    # opcao do usuário para hora
                    hora = cadastrar_hora() # 10:30:00
                else:
                    # gera hora vazia caso o usuário prefira não inserir hora
                    hora = gerar_hora_vazia() # 00:00:00
            else:
                # gera hora vazia caso o usuário decida não inserir a data                
                hora = gerar_hora_vazia() # 00:00:00
        # caso o usuário decida não inserir data e/ou hora é gerado data e hora vazia para controle
        else:            
            data = gerar_data_vazia() # 0001-01-01
            hora = gerar_hora_vazia() # 00:00:00

        # função para gerar a lista de tarefas
        cadastrar_tarefa(tarefas, id, titulo, itens, data, hora)
        input("\nPressione Enter para continuar...")

    # listar tarefa
    elif opcao == "2":
        limpar_tela()
        print(art.listar)
        listar_tarefas(tarefas)

    # marcar tarefa como concluída
    elif opcao == "3":
        limpar_tela()
        print(art.concluir)
        # controle das tarefas que não foram concluídas
        tarefas_a_concluir = []
        for tarefa in tarefas:
            if tarefa["concluida"] == False:  # tarefas pendentes
                # add na lista o id das tarefas pendentes
                tarefas_a_concluir.append(str(tarefa["id"]))
                # exibe as tarefas que não foram concluídas
                exibir_tarefa(tarefa)
        if tarefas_a_concluir == []:
            # imprimir_art()
            print("\nNenhuma tarefa pendente.")
            input("\nPressione 'Enter' para continuar...")
        else:
            op_usuario_concluir = input("\nNúmero da tarefa: ")
            # verifica se usuário escolheu tarefa constante da lista
            if op_usuario_concluir in tarefas_a_concluir:
                marcar_concluida(int(op_usuario_concluir), tarefas)
            else:
                # informa erro se opcao não estiver na lista
                exibir_opcao_invalida()
                input("\nPressione 'Enter' para continuar...")

    # deletar tarefa
    elif opcao == "4":
        limpar_tela()
        print(art.excluir)
        #print("=== Digite o número da tarefa ou 't' para todas ===")
        tarefas_a_deletar = []
        for tarefa in tarefas:
            # add na lista o idd de todas as tarefas existentes
            tarefas_a_deletar.append(str(tarefa["id"]))
            # exibe as tarefas
            exibir_tarefa(tarefa)
        if tarefas_a_deletar == []:
            # imprimir_art()
            print("\nNenhuma tarefa encontrada.")
            input("\nPressione 'Enter' para continuar...")
        else:
            print("\n=== Digite o número da tarefa ou 't' para todas ===")
            op_usuario_deletar = input("\nNúmero da tarefa: ").lower()
            # verifica se usuário escolheu tarefa constante da lista
            if op_usuario_deletar == "t":
                limpar_tela()
                print(art.excluir)
                print("=== Atenção ===")
                print("A exclusão de todas as tarefas não poderá ser desfeita.")
                confirmacao = input(
                    "Digite 't' para excluir todas ou 'Enter' para desistir: ").lower()
                if confirmacao == 't':
                    tarefas.clear()
                    salvar_tarefas_em_arquivo(tarefas)
                    print("\nTodas as tarefas foram excluídas.")
                    input("\nPressione 'Enter' para continuar...")
            elif op_usuario_deletar in tarefas_a_deletar:
                deletar_tarefa(int(op_usuario_deletar), tarefas)
            else:
                # informa erro se opcao não estiver na lista
                exibir_opcao_invalida()
                input("\nPressione 'Enter' para continuar...")

    # sair do programa
    elif opcao == "0":
        if tarefas != []:
            salvar_tarefas_em_arquivo(tarefas)
        continuar_programa = False
        print(art.tchau)

    # nenhuma das opções anteriores
    else:
        exibir_opcao_invalida()
