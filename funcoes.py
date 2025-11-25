# import funcoes internas
import os
import art

# lista que armazena o conjunto de tarefas
tarefas = []

# id para número das tarefas
#global numero_tarefa
numero_tarefa = 1


# limpa a tela
def limpar_tela():
    """Função que apaga todos os dados digitados no console realizando uma limpeza da tela com a finalidade de despoluição visual."""
    os.system('cls')

def exibir_concluidas():
    """Função que verica e exibe o número total de tarefas e o total de tarefas concluídas"""
    contador_concluidas = 0
    for tarefa in tarefas:
        if tarefa["concluida"] == True:
            contador_concluidas += 1
    print(" " * 40, "Bem-vindo!!")
    print(" " * 40, f"Tarefas concluídas: {contador_concluidas}/{len(tarefas)}") 

# imprime menu
def imprimir_menu():   
    """Função que imprime a logo, uma linha abaixo da logo e apresenta o menu com as opções para o usuário."""
    print(art.logo)
    print("Por Amanda, Fabiana e Marcone")
    print("-" * 50)
    exibir_concluidas()
    print("*** Gerenciador de Tarefas ***")
    print("1. Cadastrar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("0. Sair")

def cadastrar_tarefa(titulo, itens):
    global numero_tarefa

    # controle de tarefa concluída o não concluída
    concluida = False        

    # dicionario que armazena temporariamente cada tarefa
    tarefa = {}

    # alimento o dicionário tarefa com os dados das variáveis informados pelo usuário      
    # {chave: valor, chave: valor, chave: ["", "", ""], chave:valor},          
    tarefa["numero"] = numero_tarefa    
    tarefa["Título"] = titulo
    tarefa["Item"] = itens    
    tarefa["concluida"] = concluida    

    # incremento para id de cada tarefa
    numero_tarefa += 1
    
    # alimenta a lista de tarefas com o dicionário gerado no passo anterior
    tarefas.append(tarefa)
    print("\n*** Tarefa cadastrada com sucesso! ***")

def imprimir_menu_listar_tarefas():
    print("*** Tarefas Cadastradas ***")
    print("1. Listar todas")
    print("2. Listar concluídas")
    print("3. Listar não concluídas")    
    print("0. Voltar")

def listar_tarefas():     
    if tarefas == []:
        print("\n*** Não há tarefas cadastradas! ***")
        input("\nPressione Enter para continuar...")        
    else:
        limpar_tela()
        imprimir_menu_listar_tarefas()
        op = input("Digite sua opção: ")
        # listar todas as tarefas
        if op == "1":
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
            input("\nPressione Enter para continuar...")        
        # listar apenas as concluídas                
        elif op == "2":
            limpar_tela()
            concluidas = 0
            for tarefa in tarefas:                    
                if tarefa["concluida"] == True:
                    concluidas += 1
                    print(f"\n*** TAREFA {tarefa["numero"]}:  ✔ ***")
                    print(tarefa["Título"])
                    for elemento in tarefa["Item"]:
                        print(f'- {elemento}')
            if concluidas == 0:
                print("\n*** Não há tarefa concluída! ***")       
            input("\nPressione Enter para continuar...")                 
        # listar apenas as não concluídas                
        elif op == "3":
            limpar_tela()
            nao_concluida = 0
            for tarefa in tarefas:                    
                if tarefa["concluida"] == False:
                    nao_concluida += 1
                    print(f"\n*** TAREFA {tarefa["numero"]}:  ❌ ***")
                    print(tarefa["Título"])
                    for elemento in tarefa["Item"]:
                        print(f'- {elemento}')
            if nao_concluida == 0:
                print("\n*** Não há tarefa a ser concluída! ***") 
            input("\nPressione Enter para continuar...")        
    
        # retornar sem listar
        else:
            return            
        
def marcar_concluida(numero_tarefa):    
    for tarefa in tarefas:                 
        if tarefa["numero"] == numero_tarefa:            
            tarefa["concluida"] = True
            print("\n*** Marcada como concluída com sucesso! ***")     

def deletar_tarefa(numero_tarefa):
    deletou = False
    for tarefa in tarefas:         
        if tarefa["numero"] == numero_tarefa:
            deletou = True
            tarefas.remove(tarefa)
            print("\n*** Tarefa deletada com sucesso! ***")
    if not deletou:
        print("\n*** Opção inválida! ***")
                            
        


  
    
