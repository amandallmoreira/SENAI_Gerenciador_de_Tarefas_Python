# import funcoes internas
import os
import art

# lista que armazena o conjunto de tarefas
tarefas = []

# id para número das tarefas
#global numero_tarefa
with open("numero_tarefa.txt", "r") as arq:
    numero_tarefa = int(arq.read().strip())
    

def salvar_em_arquivo_numero_tarefa():
    global numero_tarefa    
    arquivo = "numero_tarefa.txt"
    with open(arquivo, "w", encoding="utf-8") as arq:        
        linha = f"{numero_tarefa}\n"
        arq.write(linha)


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
    print(" " * 40, "Pronto pra organizar seu dia?")
    print(" " * 40, f"Status: {contador_concluidas}/{len(tarefas)} concluídas") 

# imprime menu
def imprimir_art():
    print(art.logo)
    print("Por Amanda, Fabiana e Marcone")
    print("-" * 50)

def imprimir_menu():   
    """Função que imprime a logo, uma linha abaixo da logo e apresenta o menu com as opções para o usuário."""
    imprimir_art()
    exibir_concluidas()
    print("=== Suas Tarefas ===")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Concluir")
    print("4. Excluir")
    print("0. Sair")

def exibir_opcao_invalida():
    print("=== Opção Inválida! ===")

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
    salvar_em_arquivo_numero_tarefa()
    
    # alimenta a lista de tarefas com o dicionário gerado no passo anterior
    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso.")

    # salvar tarefa em arquivo
    salvar_em_arquivo(tarefa)
    
def salvar_em_arquivo(tarefa):    
    arquivo = "tarefas.txt"
    with open(arquivo, "a", encoding="utf-8") as arq:        
        numero = tarefa["numero"]
        titulo = tarefa["Título"]
        item = tarefa["Item"]
        concluida = tarefa["concluida"]
        linha = f"{numero};{titulo};{item};{concluida}\n"
        arq.write(linha)

def imprimir_menu_listar_tarefas():
    print("=== Tarefas ===")
    print("1. Todas")
    print("2. Concluídas")
    print("3. Pendentes")    
    print("0. Voltar")

def listar_tarefas():     
    if tarefas == []:
        print("\nNenhuma tarefa encontrada.")
        input("\nPressione 'Enter' para continuar...")        
    else:
        limpar_tela()
        imprimir_menu_listar_tarefas()
        op = input("Escolha uma opção: ")
        # listar todas as tarefas
        if op == "1":
            limpar_tela()
            for tarefa in tarefas:                    
                exibir_tarefa(tarefa)                
            input("\nPressione 'Enter' para continuar...")        
        
        # listar apenas as concluídas                
        elif op == "2":
            limpar_tela()
            concluidas = 0
            print("=== Tarefas Concluídas ===\n")
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
            nao_concluida = 0
            print("=== Tarefas Pendentes ===\n")
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
        

def exibir_tarefa(tarefa):
    print(f"\n=== Tarefa {tarefa["numero"]} ===")
    print(f"Título: {tarefa["Título"]}")
    print("Itens:")
    for item in tarefa["Item"]:
        print(f'- {item}')
    if tarefa["concluida"] == True:    
        print("Status: Concluída")        
    else:
        print("Status: Pendente")        

def marcar_concluida(numero_tarefa):    
    for tarefa in tarefas:                 
        if tarefa["numero"] == numero_tarefa:            
            tarefa["concluida"] = True
            print("\nConcluída com sucesso!")
    opcao = input("Excluir a tarefa concluída? ('1' para sim, 'Enter' para não):")
    if opcao == "1":
        deletar_tarefa(int(numero_tarefa))
        input("\nPressione 'Enter' para continuar...")        
    else:
        return    

def deletar_tarefa(numero_tarefa):
    deletou = False
    for tarefa in tarefas:         
        if tarefa["numero"] == numero_tarefa:
            deletou = True
            tarefas.remove(tarefa)
            print("\nDeletada com sucesso.")
    if not deletou:
        exibir_opcao_invalida()
                            
        


  
    
