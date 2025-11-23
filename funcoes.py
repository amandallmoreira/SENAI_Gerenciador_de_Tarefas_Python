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
    print("-" * 50)
    exibir_concluidas()
    print("Gerenciador de Tarefas")
    print("1. Cadastrar tarefa")
    print("2. Listar Tarefa")
    print("3. Marcar Tarefa como Concluida")
    print("4. Deletar tarefa")
    print("0. Sair")

def cadastrar_tarefa(titulo, itens):
    global numero_tarefa

    # controle de tarefa concluída ou não concluída
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
    # Append() adiciona um item ao final da lista
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")

def listar_tarefas(): # [
    #     {chave: valor, chave: valor, chave: ["", "", ""], chave:valor}, 
    #     {chave: valor, chave: valor, chave: ["", "", ""], chave:valor}, 
    #     {chave: valor, chave: valor, chave: ["", "", ""], chave:valor}
    # ]  
    # controle do número de tarefas
    if tarefas == []:
        print("Não há tarefas cadastradas!")
    else:
        for tarefa in tarefas:        
            # TODO: informação acerca da tarefa estar concluída ou não - opcional, caso tarefa concluida, um resultado, caso não, outro resultado
            print(f"\n*** TAREFA {tarefa["numero"]} ***")
            print(tarefa["Título"])
            for elemento in tarefa["Item"]:
                print(f'- {elemento}')        
        
def marcar_concluida(numero_tarefa):
    for tarefa in tarefas:         
        if tarefa["numero"] == numero_tarefa:
            tarefa["concluida"] == True
            print("Marcada como concluída com sucesso!")     

def deletar_tarefa(numero_tarefa):
    for tarefa in tarefas:         
        if tarefa["numero"] == numero_tarefa:
            tarefas.remove(tarefa)
            print("\nTarefa deletada com sucesso!")
                            
        
def filtar_tarefas(filtro):
    if filtro == "concluidas":
        pass
        #TODO: codificar exibir somente as tarefas concluídas
    elif filtro == "nao_concluidas":
        pass
        #TODO: codificar exibir somente as tarefas não concluídas
    else:
        # sem filtro, exibe todas as tarefas        
        listar_tarefas()

  
    
