from datetime import date, datetime, timedelta, time

# 1 implementar a data e a hora da tarefa
# 2 no cadastro o usuario digitará a data e a hora
# 2.1 acrescenta a variável data e hora
# 2.2 acrescenta a chave data e hora
# 3 data e hora facultativas para o usuário
# caso o usuário opte por não cadastrar data e hora o campo ficará vazio
# 4certificar que o usuário digitou a data e a hora no formato correto
# 5precisa verificar se a data é anterio à data atual
# 6 atualizar a exibição
# 6.1 tratamento para data e hora vazia
# 6.2 exibição da data 
# 7 atualizar o salvamento no arquivo
# 8 atualizar a recuperação do arquivo

def gerar_data_vazia():
    """Retorna um objeto datetime no formato com data 'vazia' para controle"""
    data_base = datetime.min  # 0001-01-01 00:00:00
    return date(data_base.year, data_base.month, data_base.day)  # 0001-01-01

def gerar_hora_vazia():
    """Retorna um objeto datetime no formato com hora 'vazia' para controle"""
    data_base = datetime.min  # 0001-01-01 00:00:00
    return time(data_base.hour, data_base.minute)

def cadastrar_data():
    """Retorna data inserida pelo usuário no formato datetime ou 0001/01/01 para controle"""
    # captura string data informada pelo usuário e faz a mudança para / caso entre - ou .    
    data_usuario = input("Digite a data (dd/mm/aaaa): ").replace("-", "/").replace(".", "/")    
    # tenta converter a string de data_usuario para um formato datetime
    try:
        data = datetime.strptime(data_usuario, '%d/%m/%Y').date()
        #verifica se a data inserida pelo usuário é maior que a data atual
        if verificar_data_futura(data):
            # retorna a data se maior que atual               
            return data
        else:
            # gera erro se menor que data atual
            raise ValueError("Data da tarefa precisa ser posterior à data atual.")            
    except ValueError as msg:
        print("\n")
        print("=== Opção Inválida! ===")
        print(msg)
        opcao = input("\nDigite 'd' para data ou 'Enter' para concluir: ").lower()            
        if opcao == "d":
            # funcao recursiva
            data_usuario = input("Digite a data (dd/mm/aaaa): ").replace("-", "/").replace(".", "/")
            try:
                data = datetime.strptime(data_usuario, '%d/%m/%Y').date()
                if verificar_data_futura(data):
                    return data
                else:
                    raise ValueError("Data da tarefa precisa ser posterior à data atual.")
            except ValueError:                
                return gerar_data_vazia() # 0001-01-01
        else:            
            return gerar_data_vazia() # 0001-01-01

def cadastrar_hora():
    """Retorna hora inserida pelo usuário no formato datetime ou 0001/01/01 para controle"""
    # opcao do usuario para data    
    hora_usuario = input("Digite a hora (hh:mm): ").replace("-", ":").replace(".", ":").replace("/", ":")    
    try:
        hora = datetime.strptime(hora_usuario, '%H:%M').time()               
        return hora # 15:30:00            
    except ValueError:
        print("\n")
        print("=== Opção Inválida! ===")
        opcao_hora_2 = input("\nDigite 'h' para data ou 'Enter' para concluir: ").lower()         
        if opcao_hora_2 == "h":            
            hora_usuario = input("Digite a hora (hh:mm): ").replace("-", ":").replace(".", ":").replace("/", ":")
            try:
                hora = datetime.strptime(hora_usuario, '%H:%M').time() # 15:30:00
                return hora # 15:30:00
            except:                
                return gerar_hora_vazia() # 00:00:00
                
        else:
            return gerar_hora_vazia() # 00:00:00

def verificar_data_futura(data):
    """Recebe uma data e retorna verdadeiro se maior que data atual ou falso se menor que data atual"""
    hoje = datetime.today().date()
    return data > hoje

def verificar_data_semana(data):
    """Recebe uma data e retorna verdadeiro se dentro de intervalo de até 7 dias ou falso se fora do intervalo"""
    hoje = datetime.today().date()
    diferenca = data - hoje
    return diferenca.days < 7

