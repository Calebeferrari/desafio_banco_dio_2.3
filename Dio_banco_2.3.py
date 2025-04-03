# Bibliotecas
import os
from time import sleep
from datetime import datetime


# Funções de apresentação
def lines():
    '''
    Linha de pontos para servir como divisórias de opções e apresentações
    '''
    # Quantidade de pontos da divisória
    amount_lines = 60
    # Caso precise retornar a divisória dentro de um  f-string ou em outra variável
    lines = '.' * amount_lines
    # Uso mais comum, simplesmente exibe as linhas
    print('.' * amount_lines)

    return lines

def titles(txt):
    '''
    Título de apresentação do programa e do uso da página
    '''
    id_banco = 'Banco DIO - '
    lines()
    print(f'${id_banco+txt:^58}$')
    lines()

def enter_pass():
    '''
    Simples comando de continuação.
    Serve para pausar a execução e em seguida o usuário continuar a aplicação
    '''
    input('Enter p/ continuar: ')

def clear_screen():
    """
    Função responsável por limpar tela a cada nova execução de tela.
    Função multiplataforma. Porém em caso de erro, apenas substituir os comandos internos por um print()
    """
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def sleep_general():
    '''
    Para controlar todas as pausas limitadas do programa.
    '''
    sleep(1.5)

# Funções auxiliares

# Menu local para diversas opções diversas 
def opc_continuation(txt_title:str,txt_notif:str, txt_opc:str, n1:int, n2:int):
    '''
    txt_title: Identifica o que deve estar dentro do título
    da página em execução.
    Exemplo:
        ..............................
        $   Banco DIO - txt_title    $
        ..............................
    
    txt_notif: Mensagem que será exibida entre o título e
    as opções do menu local.
    Se a entrada dela for vazia, deverá declarada como '',
    e dessa forma não aparecerá mensagem alguma.
    
    txt_opc: Modelo de menu conveniente
    para a ocasião.
    Exemplo:
    1 - Opcão 1
    2 - Opção 2
    0 - Sair

    n1 e n2: servem para indicar a quantidade
    de opções a serem utilizadas no mini menu.
    n1 para o menor valor indicado da opcão.
    n2 para o maior valor indicado da opção.
    Exemplo:
    P/ o modelo acima
    n1 = 0 : Menor valor indicado
    n2 = 2 : Maior valor indicado
    '''
    
    while True:
        try:
            # Complemento de título do menu
            titles(txt_title)

            # Condição para entrada de texto entre título e opções do menu
            if txt_notif != '':
                print(txt_notif)
                lines()
            
            # Condições para a exibição das opções do menu

            # Opção relativa a entrada float, p/ transações bancárias
            if txt_title == 'Depósito' or txt_title == 'Saque':
                
                # Entrada recebe um valor str p/ se adequar ao padrão de pontuação PT/BR - Virgulas se torna em ponto e ponto em x p/ gerar erro e receber apenas no padrão estabelecido.
                opc_cont = input(f'{txt_opc}\nR$').replace('.', 'x').replace(',', '.')

                # Tratamento de erro - P/ entrada com ponto.
                if 'x' in opc_cont:
                    raise Exception
                # Tratamento de erro - P/ entrada com mais de 2 valores decimais.
                if '.' in opc_cont:
                    if len(opc_cont.split('.')[-1]) > 2:
                        raise Exception
                
                # O valor que será retornado deverá ser float.
                opc_cont = float(opc_cont)

            # Opção relativa a entradas comuns de opções numéricas do tipo int
            else:
                
                opc_cont = int(input(f'{txt_opc}\nOpção: '))

            # Validação de opções válidas
            if opc_cont < n1 or opc_cont > n2:
                raise ValueError

        except ValueError:
            lines()
            print('Entrada inválida...Tente novamente.')
            sleep_general()
            clear_screen()

        except Exception as a:
            if 'x' in opc_cont:
                lines()
                print('Use virgula p/ valores decimais.')
                sleep_general()
                clear_screen()
                
            elif len(opc_cont.split('.')[-1]) > 2:
                lines()
                print('Use apenas 2 casas decimais.')
                sleep_general()
                clear_screen()
        
        else:
            return opc_cont

# Ordena lista geral em ordem alfabética
def list_order(lista_x):
    '''
    Responsável por em ordem alfabética os dicionários cadastrados na lista principal
    '''
    lista_ord = sorted(lista_x, key=lambda x:x['nome'])
    return lista_ord

# Gera cpf automaticamente - Usada para testes
def generator_cpf():
    '''
    Usada para gerar cpfs aleatórios.
    APAGAR função, quando programa estiver pronto.
    Função localizada dentro da função create_user(), na parte do
    cadastro de CPFs
    '''

    from random import randint
    cpf = randint(10000000000, 99999999999)
    return cpf

# Exibe a lista de cadastros formatada para leitura
def view_registration(lista_reg):
    '''
    Mostra a lista de cliente cadastrados
    '''

    # Título da lista - Sequência, nome e CPF
    print(f'{'Seq':>3}{'Nome':^8}{'CPF':>42}')

    # Linhas divisórias
    lines()

    # Apresentação da lista - Nome e CPF
    for pos, cont in enumerate(lista_reg):
        print(f'{pos+1:0>3} ',end='')

        for pos_dict, value in enumerate(lista_reg[pos].values()):
            if pos_dict == 0:
                print(f'{value[:40]:<42}',end='')

            elif pos_dict == 1:
                print(f'{value:^14}',end='')
                break
        print()

# Exibe as informações formatadas do cadastro selecionado
def visualizer_result(o_s_local, lista_geral_vis_result):
    '''
    Responvável por visualizar o cadastro selecionado.
    Informará dados e se tem contas vinculadas.
    Retornará o resultado com uma variável string(para facilitar na execução do programa na função que a conterá)
    
    o_s_local: Recebe o valor da posição em que está o cadastro pesquisado em relacão a lista de exibição. Não é sobre a lista geral.
    lista_geral_vis_result: Recebe a lista geral
    '''
    # Variáveis que manipularão os resultados e serão retornadas
    print_list_a = ''
    print_list_b = ''
    print_list_c = ''
    print_list_c_local_1 = ''
    print_list_c_local_2 = ''
    for key, value in lista_geral_vis_result[o_s_local-1].items():
        # Condições p/ visualizar a chave 'contas'. P/ saber se há contas cadastradas.
        if value == lista_geral_vis_result[o_s_local-1]['contas']:
            # Mensagem de que não tem contas vinculadas a cadastro
            if lista_geral_vis_result[o_s_local-1]['contas'] == []:
                print_list_c = 'Não possue contas cadastradas.'
                print_list_b = print_list_b + print_list_c
            # Mensagem de que notifica se há contas vinculadas e quais
            else:
                for cont in lista_geral_vis_result[o_s_local-1]['contas']:
                    for key_p, value_p in cont.items():
                        print_list_c_local_1 = str(f'{key_p.title()}: {value_p} ')
                        print_list_c_local_2 = print_list_c_local_2 + print_list_c_local_1
                    print_list_c_local_2 += '\n'
                print_list_c = f'Contas listadas:\n{print_list_c_local_2}'
                print_list_b = print_list_b + print_list_c
        # Juntará os resultados os convertendo em um string
        else:
            print_list_a = str(f'{key.title()}: {value}\n')
            print_list_b = print_list_b + print_list_a
    return print_list_b

# Funções de execução

# Exibe o menu principal
def main_menu():
    '''
    Função exclusiva para o menu principal
    A quantidade de opções tem que ser igual aos da condição de entrada.
    '''
    # Informação no título
    title_local = 'Admin'

    while True:
        try:
            # Apresentação da aba - Admin: Uso da gerência
            titles(title_local)

            # Opções do menu principal
            print('1 - Criar usuário')
            print('2 - Criar conta')
            print('3 - Lista de clientes')
            print('4 - Movimentação de contas')
            print('5 - Área do programador')
            print('0 - Encerrar')

            # Entrada da opção
            lines()
            opc_menu = int(input('Opção: ').strip())

            # Condições de entrada
            if opc_menu < 0 or opc_menu > 5:
                raise ValueError
            
        except:
            print('Opcão inválida.')
            enter_pass()
            clear_screen()

        else:
            if opc_menu == 1:
                clear_screen()
                return opc_menu                
            
            elif opc_menu == 2:
                clear_screen()
                return opc_menu
            
            elif opc_menu == 3:
                clear_screen()
                return opc_menu

            elif opc_menu == 4:
                clear_screen()
                return opc_menu
            
            elif opc_menu == 5:
                clear_screen()
                return opc_menu

            elif opc_menu == 0:
                clear_screen()
                return opc_menu

# Criação de cadastro de clientes
def create_user(creat_record, lista_conf, list_position):
    '''
    Função com dupla atribuição.
    Responsável pela criação de cadastro do cliente.
    Responsável por corrigir, a posteriori, os dados cadastrais do cliente.

    Cada campo do cadastro tem sua própria função. O que permite acrescimos mais fáceis para novos campos cadastrais.

    Variáveis:
    creat_record: Recebe um boolean. Caso True ele relaizará um cadastro. Caso False ele corrigirá um determinado cadastro.
    lista_conf: Recebe a lista geral, que armazena os cadastros.
    list_position: Receberá uma posição da lista geral em caso de correção

    '''

    # Declaração de dicionário local - Também zera para o próximo cadastro
    dicio_cliente = {}

    # Variável para execução ou interrupção do cadastro
    cicle_continue = True

    # Informação no título
    if creat_record == True:
        title_local = 'Cadastro de cliente'
    elif creat_record == False:
        title_local = 'Correção de cadastro'

    # Funções de campos cadastrais

    # Cadastro nome
    def cadastro_nome(cad_nome, cicle=True, creat_reg_local=creat_record):
        '''
        cad_name: Posição do campo nome no dicionário de cadastro da lista geral.
        cicle: Define a continuidade do ciclo de cadastramento ou correção do campo 'nome'.
        creat_reg_local: Define se a função vai cadastrar um novo nome ou fará uma correção.
        '''
        # Variável boolean usada para evitar repetição de mini menus nas execuções
        full_correction = True

        # Processo de cadastramento
        while cicle == True:
            try:

                # Condicional p/cadastro
                if creat_record == True:
                    titles(title_local)
                    print('Informe nome ou entre vazio p/sair.')
                    lines()
                    cad_nome['nome'] = str(input('Nome: ').strip().title())

                    if cad_nome['nome'] == '':
                        raise Exception

                # Condicional p/correção
                elif creat_record == False:

                    # Condição para evitar repetição de mini menus nas execuções
                    if full_correction == True:

                        # Mini menu de apresentação de campo a ser corrigido. Tem 3 opções: Corrigir, avancar p/ próximo campo ou encerrar.
                        opc_correction = opc_continuation(title_local, f'Nome: {lista_conf[list_position]['nome']}','1 - Corrigir\n2 - Avançar\n0 - Encerrar',n1=0,n2=2)
                        
                    # Condicionais de mini menu:

                    # Entrada de nome a ser corrigido
                    if opc_correction == 1:
                        
                        # Armazena dados originais do campo p/ evitar perde-lo no processo de correção
                        nome_atual = lista_conf[list_position]['nome']
                        
                        # Exibição da tela de correção
                        clear_screen()
                        titles(title_local)
                        print('Informe novo nome ou entre vazio p/sair.')
                        lines()
                        print(f'Nome atual: {lista_conf[list_position]['nome']}')
                        lines()
                        lista_conf[list_position]['nome'] = str(input('Nome: ').strip().title())
                        
                        # Variável usada para evitar repetição de mini menus nas execuções
                        full_correction = True

                        # Condição para entrada vazia
                        if lista_conf[list_position]['nome'] == '':
                            raise Exception

                    # Avançando campo
                    elif opc_correction == 2:

                        lines()
                        print('Avançando cadastro...')
                        sleep_general()
                        clear_screen()
                        break
                    
                    # Encerrando campo
                    elif opc_correction == 0:

                        lines()
                        print('Encerrando cadastro...')
                        sleep_general()
                        clear_screen()
                        cicle = False
                        return cicle

            # Tratamento de erros
            except Exception:
                lines()
                print('Entrada vazia...')
                sleep_general()
                clear_screen()

                # Opção para registrar novo nome ou voltar p/ menu principal
                opc_1 = opc_continuation('Cad. cliente', '', '1 - Continuar\n0 - Encerrar', 0, 1)


                if opc_1 == 1:
                    # Retomando valor de campo cadastrado
                    if creat_record == False:
                        lista_conf[list_position]['nome'] = nome_atual
                    # Mini tela de exibição
                    lines()
                    print('Cadastrar nome...')
                    sleep_general()
                    clear_screen()
                    continue

                elif opc_1 == 0:
                    # Limpando cadastro em caso de cadastro
                    cad_nome.clear()

                    # Retomando valor de campo cadastrado em caso de Correção
                    if creat_record == False:
                        lista_conf[list_position]['nome'] = nome_atual
                    
                    # Exibindo informação de encerramento
                    lines()
                    print('Encerrando cadastro...')
                    sleep_general()
                    clear_screen()
                    cicle = False
                    return cicle

            except ValueError as a:
                lines()
                print('Erro...Tente novamente')
                sleep_general()
                clear_screen()

            # Finalização de cadastro
            else:
                # Confirmação visual do cadastro efetuado.
                clear_screen()

                # Apresentação final

                # Mini menu com resultado p/ CADASTRO
                if creat_record == True:
                    opc_2 = opc_continuation(title_local, f'Nome cadastrado: {cad_nome['nome']}' , '1 - Continuar\n2 - Corrigir\n0 - Sair',n1=0,n2=2)
                
                # Mini menu com resultado p/ CORREÇÃO
                elif creat_record == False:
                    opc_2 = opc_continuation(title_local, f'Nome cadastrado: {lista_conf[list_position]['nome']}' , '1 - Continuar\n2 - Corrigir\n0 - Sair',n1=0,n2=2)

                # Condições de continuação de mini menu - Abrange ambos de cadastro e correção

                # Opção de avança para próximo campo de cadastramento
                if opc_2 == 1:
                    clear_screen()
                    return cad_nome

                # Opção de voltar para corrigir
                elif opc_2 == 2:
                    #Flag p/ voltar direto para página de correção
                    full_correction = False

                    # Mensagem de carregamento de correção
                    lines()
                    print('Carregando opção de correção.')
                    sleep_general()
                    clear_screen()
                    continue
                
                # Opção de encerramento. Voltar para menu princiapl - Cadastro e Correção
                elif opc_2 == 0:
                    # Exibição de encerramento em caso de CADASTRO
                    if creat_record == True:
                        cad_nome.clear()
                        lines()
                        print('Encerrando cadastro...')
                        sleep_general()
                        clear_screen()
                        cicle = False
                        return cicle

                    # Exibição de encerramento em caso de CORREÇÃO
                    elif creat_record == False:
                        lines()
                        print('Encerrando correções...')
                        sleep_general()
                        clear_screen()
                        cicle = False
                        return cicle
        
    # Cadastro cpf    
    def cadastro_cpf(cad_cpf, cicle=True, creat_record_local=creat_record):
        '''
        cad_cpf: Posição do campo cpf no dicionário de cadastro da lista geral.
        cicle: Define a continuidade do ciclo de cadastramento ou correção do campo 'cpf'.
        creat_record_local: Define se a função vai cadastrar um novo cpf ou fará uma correção.
        '''

        # Variável boolean usada para evitar repetição de mini menus nas execuções
        full_correction = True

        # Cadastro de CPF
        while cicle == True:
            
            try:
                # Apresentação de entrada de CPF - CADASTRO
                if creat_record == True:
                    titles(title_local)
                    print('Informe CPF ou entre vazio p/sair.')
                    lines()
                    cad_cpf['cpf'] = input('CPF [Apenas n°s]: ').strip()

                    # Gerador de CPF p/ testes 
                    #cad_cpf['cpf'] = generator_cpf()

                # Apresentação de entrada de CPF - CORREÇÃO
                elif creat_record == False:

                    # Transferindo valor de posição de cpf da lista geral para uma única variável local.
                    cad_cpf['cpf'] = lista_conf[list_position]['cpf']

                    # Armazenamento de valor de CPF atual
                    cpf_atual = lista_conf[list_position]['cpf']

                    # Variável boolean usada para evitar repetição de mini menus nas execuções
                    if full_correction == True:
                        # Mini menu de apresentação de campo a ser corrigido. Tem 3 opções: Corrigir, avançar p/ próximo campo ou encerrar.
                        opc_correction = opc_continuation(title_local, f'CPF: {cad_cpf['cpf']}','1 - Corrigir\n2 - Avançar\n0 - Encerrar',n1=0,n2=2)

                    # Condicionais de mini menu:

                    # Opção de correção de nome
                    if opc_correction == 1:
                        
                        # Exibição da tela de correção
                        clear_screen()
                        titles(title_local)
                        print('Informe novo CPF ou entre vazio p/sair.')
                        lines()
                        print(f'CPF atual: {cad_cpf['cpf']}')
                        lines()
                        cad_cpf['cpf'] = str(input('CPF: ').strip().title())

                    # Opção de avançar p/ cadastro seguinte
                    elif opc_correction == 2:

                        # Aviso de avanço no cadastramento
                        lines()
                        print('Avançando cadastro...')
                        sleep_general()
                        clear_screen()
                        break
                    
                    # Opção para encerrrar
                    elif opc_correction == 0:

                        # Transferência de valores da variável local para a variável da posição da lista geral - Caso de Correção
                        if creat_record == False:
                            lista_conf[list_position]['cpf'] = cad_cpf['cpf']

                        # Limpando varíável de cadastro local - Caso de Cadastro
                        cad_cpf.clear()

                        # Aviso de encerramento
                        lines()
                        print('Encerrando cadastro...')
                        sleep_general()
                        clear_screen()
                        cicle = False
                        return cicle

                # Condições válidas para CADASTRO e CORREÇÃO de cpf válido

                # Condição de saída - Entrada vazia
                if cad_cpf['cpf'] == '':
                    flag_error = 'vazio'
                    raise Exception

                # Tamanho de digitos
                if len(cad_cpf['cpf']) != 11:
                    # Usado para expecificar a saída da mensagem do erro
                    flag_error = '!=11'
                    raise Exception

                # Evitar CPF duplicado
                for cont in lista_conf:
                    if int(cad_cpf['cpf']) == int(cont['cpf'].replace('.', '').replace('-', '')):
                        flag_error = '=cpf'
                        raise Exception

                # Erro p/ entrada de número negativo
                if int(cad_cpf['cpf']) < 0:
                    raise ValueError
            
            # Tratamento de erros
            except ValueError as a:
                lines()
                print('Erro... Tente novamente.')
                sleep_general()
                clear_screen()

            except Exception as e:
                # Informa que cpf não é válido
                if flag_error == '!=11':
                    lines()
                    print('CPF inválido.')
                    sleep_general()
                    clear_screen()

                # Informa que CPF já existe
                elif flag_error == '=cpf':
                    lines()
                    print('Cpf já cadastrado.')
                    sleep_general()
                    clear_screen()
                
                # Opção de entrada vazia p/ tentar outro CPF ou voltar p/ menu principal
                elif flag_error == 'vazio':

                    # Mensagem de entrada vazia
                    lines()
                    print('Entrada vazia.')
                    sleep_general()
                    clear_screen()
                    
                    # Mini menu de opções de escolha
                    clear_screen()
                    opc = opc_continuation('Cad. cliente', '', '1 - Continuar\n0 - Encerrar', 0, 1)

                    # Opção p/ cadastrar novo CPF
                    if opc == 1:

                        # Retomando o valor incial do CPF
                        if creat_record == False:
                            cad_cpf['cpf'] = cpf_atual

                        # Mensagem p/ cadastrar novo CPF
                        lines()
                        print('Cadastro CPF.')
                        sleep_general()
                        clear_screen()
                        continue
                    
                    # Opção p/ encerrar cadastro
                    elif opc == 0:
                        
                        # Em caso de correção retoma o valor incial do CPF
                        if creat_record == False:
                            lista_conf[list_position]['cpf'] = cpf_atual

                        # Em caso de cadastro, limpa cadastro
                        cad_cpf.clear()

                        # Encerrando ciclo
                        cicle = False

                        # Exibição de mensagem de encerramento
                        lines()
                        print('Finalizando cadastro...')
                        sleep_general()
                        clear_screen()

                        return cicle                       
            
            # Conclusão de cadastro de CPF
            else:
                # Convertendo int em str
                #cad_cpf['cpf'] = str(cad_cpf['cpf'])

                # Formatação de CPF padrão (com . e -). Aplicando pontuação padrão.
                cad_cpf['cpf'] = cad_cpf['cpf'][:3] + '.' + cad_cpf['cpf'][3:6] + '.' + cad_cpf['cpf'][6:9] + '-' + cad_cpf['cpf'][9:]

                # Confirmação visual do cadastro efetuado + opção para tentar outro CPF ou voltar p/ menu principal
                clear_screen()
                opc = opc_continuation('Cad. cliente', f'CPF cadastrado: {cad_cpf['cpf']}', '1 - Continuar\n2 - Corrigir\n0 - Sair', 0, 2)
                
                # Condicionais de mini-menu de finalização de cadastro de CPF

                # Opção de continuar cadastro
                if opc == 1:

                    # Em caso de CORREÇÃO de cpf - Transferência de valores da variável local para a variável da posição da lista geral
                    if creat_record == False:
                        lista_conf[list_position]['cpf'] = cad_cpf['cpf']

                    # Comandos finais
                    clear_screen()
                    return cad_cpf

                # Opção de correção
                elif opc == 2:
                    # Condições p/ caso de correção
                    if creat_record == False:
                        # Boolean que garante a ida direto p/ cadastro
                        full_correction = False

                        # Transferindo novo valor de posição de cpf da lista geral para uma única variável local.
                        lista_conf[list_position]['cpf'] = cad_cpf['cpf']
                    
                        # Armazenamento de novo valor de CPF atual
                        cpf_atual = lista_conf[list_position]['cpf']

                    # Exibição de mensagem de correção
                    lines()
                    print('Corrigir CPF...')
                    sleep_general()
                    clear_screen()
                    continue

                # Opção de encerramento
                elif opc == 0:

                    # Em caso de CORREÇÃO de cpf - Transferência de valores da variável local para a variável da posição da lista geral
                    if creat_record == False:
                        lista_conf[list_position]['cpf'] = cad_cpf['cpf']
                    
                    # Em caso de CADASTRO de cpf - Limpa cadastro
                    cad_cpf.clear()

                    # Comando de encerramento de ciclo
                    cicle = False

                    # Mensagem final de encerramento de cadastro
                    lines()
                    print('Encerrando cadastro...')
                    sleep_general()
                    clear_screen()
                    return cicle  

    # Cadastrto data de nascimento
    def cadastro_data(cad_data, cicle=True, creat_reg_local=creat_record):
        '''
        Função responsável pela criação das datas de nascimeto.
        Também armazena a idade do cliente p/ futuras consultas.

        cad_data: Posição do campo de data de nascimento no dicionário de cadastro da lista geral.
        cicle: Define a continuidade do ciclo de cadastramento ou correção do campo 'nascimento'.
        creat_reg_local: Define se a função vai cadastrar uma nova data de nascimento ou fará uma correção.
        '''

        # Variável boolean usada para evitar repetição de mini menus nas execuções
        full_correction = True

        while cicle == True:

            try:
                # Condição p/ CADASTRO
                if creat_record == True:
                    titles(title_local)
                    print('Informe data de nascimento ou \nentre vazio p/sair.')
                    lines()
                    cad_data['nascimento'] = input('Data de nascimento:\n[Com barra. Ex: dd/mm/aaaa]\n').strip()
                
                # Condição p/ CORREÇÃO
                elif creat_record == False:
                    # Transferindo valor de posição de data da lista geral para uma única variável local.
                    cad_data['nascimento'] = lista_conf[list_position]['nascimento']

                    # Armazenamento de valor de data atual
                    data_atual = lista_conf[list_position]['nascimento']

                    # Variável boolean usada para evitar repetição de mini menus nas execuções
                    if full_correction == True:
                        # Mini menu de apresentação de campo a ser corrigido. Tem 3 opções: Corrigir, avancar p/ próximo campo ou encerrar.
                        opc_correction = opc_continuation(title_local, f'Data: {cad_data['nascimento']}','1 - Corrigir\n2 - Avançar\n0 - Encerrar',n1=0,n2=2)

                    # Condicionais de mini menu:

                    # Opção de correção de nome
                    if opc_correction == 1:
                        
                        # Exibição da tela de correção
                        clear_screen()
                        titles(title_local)
                        print('Informe novo data ou entre vazio p/sair.')
                        lines()
                        print(f'Data atual: {cad_data['nascimento']}')
                        lines()
                        cad_data['nascimento'] = str(input('Data: ').strip().title())

                    # Opção de avançar p/ cadastro seguinte
                    elif opc_correction == 2:

                        # Aviso de avanço no cadastramento
                        lines()
                        print('Avançando cadastro...')
                        sleep_general()
                        clear_screen()
                        break
                    
                    # Opção para encerrrar
                    elif opc_correction == 0:

                        # Transferência de valores da variável local para a variável da posição da lista geral
                        lista_conf[list_position]['nascimento'] = data_atual
                        
                        # Limpando varíável de cadastro local
                        cad_data.clear()

                        # Aviso de encerramento
                        lines()
                        print('Encerrando cadastro...')
                        sleep_general()
                        clear_screen()
                        cicle = False
                        return cicle

                # Condições de exceção
                if cad_data['nascimento'] == '':
                    flag_error = 'vazio'
                    raise Exception

                # Conversão da entrada em data - Determina que o programa tentará registrar apenas datas
                data_conversion = datetime.strptime(cad_data['nascimento'], '%d/%m/%Y')

            # Tratamento de erros
            except ValueError as error:

                lines()
                print('Erro... Tente novamente.')
                sleep_general()
                clear_screen()

            except Exception:

                # Opção para tentar outra data ou voltar p/ menu principal
                clear_screen()
                opc = opc_continuation('Cad. cliente', '', '1 - Cadastrar data\n0 - Voltar p/ menu', 0, 1)

                # Opção de cadastrar data
                if opc == 1:

                    # Retomando valor incial da data
                    data_atual = cad_data['nascimento']

                    # Mensagem de cadastro de data
                    lines()
                    print('Cadastro data...')
                    sleep_general()
                    clear_screen()
                    continue
                
                # Opção de encerramento de cadastro de data
                elif opc == 0:

                    # Retomando valor da posição da lista geral - Em caso de encerramento de correção
                    if creat_record == False:
                        lista_conf[list_position]['nascimento'] = data_atual
                    
                    # Limpando campo de data - Em caso de encerramento de cadastro
                    cad_data.clear()

                    # Encerrando ciclo
                    cicle = False

                    # Mensagem de encerramento
                    lines()
                    print('Finalizando cadastro...')
                    sleep_general()
                    clear_screen()
                    return cicle

            else:
                # Conversão para data padrão BR
                data_br = data_conversion.strftime('%d/%m/%Y')
                cad_data['nascimento'] = data_conversion.strftime('%d/%m/%Y')

                # Idade do cliente
                cad_data['idade'] = datetime.today().year - data_conversion.year
                if (datetime.today().month, datetime.today().day) < (data_conversion.month,data_conversion.day):
                    cad_data['idade'] -= 1

                # Confirmação visual do cadastro efetuado + opção para corrigr data de nascimento ou voltar p/ menu principal
                clear_screen()
                opc = opc_continuation('Cad. cliente', f'Data de nascimento: {cad_data['nascimento']}\nIdade atual: {cad_data['idade']}', '1 - Continuar\n2 - Corrigir\n0 - Sair', 0, 2)
                
                # Opção de finalização de cadastro de CPF
                if opc == 1:
                    # Caso de CORREÇÃO de data de nascimento
                    if creat_record == False:
                        # Transferindo valores da variável local para posição do cadastro corrigido
                        lista_conf[list_position]['nascimento'] = cad_data['nascimento']
                        lista_conf[list_position]['idade'] = cad_data['idade']
                        
                    clear_screen()
                    return data_conversion

                elif opc == 2:

                    # Condições p/ caso de correção
                    if creat_record == False:

                        # Atualizando o valor da posição da lista geral para a variável local - Exibirá o valor atualizado da data de nascimento
                        lista_conf[list_position]['nascimento'] = cad_data['nascimento']
                        lista_conf[list_position]['idade'] = cad_data['idade']

                        # Responsável por ir direto p/ correção
                        full_correction = False
                    
                    # Exibe mensagem de correção
                    lines()
                    print('Corrigir data de nascimento...')
                    sleep_general()
                    clear_screen()
                    continue

                elif opc == 0:
                    # Caso de CORREÇÃO de data de nascimento
                    if creat_record == False:
                        lista_conf[list_position]['nascimento'] = cad_data['nascimento']
                        lista_conf[list_position]['idade'] = cad_data['idade']
                    
                    # Caso de CADASTRO - Limpa campo de cadastro
                    cad_data.clear()

                    # Encerrando ciclo
                    cicle = False

                    # Mensagem de encerramento
                    lines()
                    print('Encerrando cadastro...')
                    sleep_general()
                    clear_screen()
                    return cicle

    # Cadastro endereço - Funcional, mas em contrução
    def cadastro_endereco(cad_endereco, cicle=True, creat_reg_local=creat_record):
        '''
        Campo em construção.
        Preenchimento opcional.
        '''

        # Variável boolean usada para evitar repetição de mini menus nas execuções
        full_correction = True

        while cicle == True:
            try:
                # Cadastro de endereço
                if creat_record == True:
                    titles(title_local)
                    print('Informe endereço:\n[Opcional. Vazio p/avançar]')
                    lines()
                    cad_endereco['endereço'] = input('Endereço [Estado e Cidade]: ').strip()
                
                # Correção de endereço
                elif creat_record == False:

                    # Transferindo valor de posição da lista geral para uma única variável local.
                    cad_endereco['endereço'] = lista_conf[list_position]['endereço']

                    # Armazena dados originais do campo p/ evitar perde-lo no processo de correção
                    endereco_atual = lista_conf[list_position]['endereço']

                    # Condição para evitar repetição de mini menus nas execuções
                    if full_correction == True:
                        # Mini menu de apresentação de campo a ser corrigido. Tem 3 opções: Corrigir, avancar p/ próximo campo ou encerrar.
                        opc_correction = opc_continuation(title_local, f'Endereço: {cad_endereco['endereço']}','1 - Corrigir\n2 - Avançar\n0 - Encerrar',n1=0,n2=2)
                        
                    # Condicionais de mini menu:

                    # Entrada de nome a ser corrigido
                    if opc_correction == 1:

                        # Exibição da tela de correção
                        clear_screen()
                        titles(title_local)
                        print('Preencha apenas com estado e cidade.\n[Campo opcional. Vazio p/avançar]')
                        lines()
                        print(f'Atual: {cad_endereco['endereço']}')
                        lines()
                        cad_endereco['endereço'] = str(input('Endereço: ').strip().title())
                        
                        # Variável usada para evitar repetição de mini menus nas execuções
                        full_correction = True

                        # Condição para entrada vazia
                        if cad_endereco['endereço'] == '':
                            cad_endereco['endereço'] = endereco_atual

                    # Avançando campo
                    elif opc_correction == 2:

                        # Retomando valor de lista geral da variável local
                        lista_conf[list_position]['endereço'] = cad_endereco['endereço']
                        
                        # Limpando variável local - Evitar erros
                        cad_endereco.clear()

                        lines()
                        print('Avançando cadastro...')
                        sleep_general()
                        clear_screen()
                        break
                    
                    # Encerrando campo
                    elif opc_correction == 0:

                        # Retomando valor de lista geral da variável local
                        lista_conf[list_position]['endereço'] = cad_endereco['endereço']

                        # Limpando variável local - Evitar erros
                        cad_endereco.clear()

                        lines()
                        print('Encerrando cadastro...')
                        sleep_general()
                        clear_screen()
                        cicle = False
                        return cicle

            # Tratamento de erros
            except ValueError as error:
                print('Erro...')
                sleep_general()
                clear_screen()
            
            # Finalização de entrada
            else:

                # Apresentação final de endereço
                clear_screen()
                
                opc = opc_continuation('Cad. cliente', 'Endereço cadastrado: Vazio' if cad_endereco['endereço'] == '' else f'Endereço cadastrado: {cad_endereco['endereço']}', '1 - Continuar\n2 - Corrigir\n0 - Sair', 0, 2)

                # Condicionais de mini-menu de finalização de cadastro de endereço

                # Opção de continuar cadastro
                if opc == 1:

                    # Em caso de CORREÇÃO de endereço
                    if creat_record == False:
                        # Transferência de valores da variável local para a variável da posição da lista geral
                        lista_conf[list_position]['endereço'] = cad_endereco['endereço']
                        # Limpando variável local
                        cad_endereco.clear()

                    # Comandos finais
                    clear_screen()
                    return cad_endereco

                # Opção de correção
                elif opc == 2:

                    
                    # Condições p/ caso de correção
                    if creat_record == False:

                        # Condições p/ caso de correção
                        full_correction = False
                        # Transferindo novo valor de posição de cpf da lista geral para uma única variável local.
                        lista_conf[list_position]['endereço'] = cad_endereco['endereço']
                        # Armazenamento de novo valor de CPF atual
                        endereco_atual = lista_conf[list_position]['endereço']

                    # Exibição de mensagem de correção
                    lines()
                    print('Corrigir endereço...')
                    sleep_general()
                    clear_screen()
                    continue

                # Opção de encerramento
                elif opc == 0:

                    # Em caso de CORREÇÃO de endereço - Transferência de valores da variável local para a variável da posição da lista geral
                    if creat_record == False:
                        lista_conf[list_position]['endereço'] = cad_endereco['endereço']
                    
                    # Em caso de CADASTRO de endereço - Limpa cadastro
                    cad_endereco.clear()

                    # Comando de encerramento de ciclo
                    cicle = False

                    # Mensagem final de encerramento de cadastro
                    lines()
                    print('Encerrando cadastro...')
                    sleep_general()
                    clear_screen()
                    return cicle  

    # Criação de dicionário que armazenará a lista de possíveis contas associadas do cliente cadastrado
    def add_contas(cad_list_cont, creat_reg_local=creat_record):
        '''
        Adiciona ao cadastro um dicionário que contém um lista
        Essa lista armazenará as contas cadastradas
        '''
        cad_list_cont['contas'] = []

        return cad_list_cont

    # Ciclo de execução do cadastro
    while True:
        # Campos de cadastros a serem preenchidos
        cicle_continue = cadastro_nome(dicio_cliente)
        if cicle_continue == False:
            break
            
        cicle_continue = cadastro_cpf(dicio_cliente)
        if cicle_continue == False:
            break

        cicle_continue = cadastro_data(dicio_cliente)
        if cicle_continue == False:
            break

        cicle_continue = cadastro_endereco(dicio_cliente)
        if cicle_continue == False:
            break
        
        # Adciona campo de contas a serem cadastradas - Em caso de cadastro
        if creat_record == True:
            add_contas(dicio_cliente)

        # Confirmação visual do cadastro efetuado.
        clear_screen()
        titles(title_local)
        
        # Visualização de cadastro realizado

        # P/ conta cadastrada
        if creat_record == True:
            for key, value in dicio_cliente.items():
                # Inibe a exibição do campo de contas
                if key == 'contas':
                    break
                print(f'{key.title()}: {value}')

        elif creat_record == False:
            for key, value in lista_conf[list_position].items():
                # Inibe a exibição do campo de contas
                if key == 'contas':
                    break
                print(f'{key.title()}: {value}')

        # Break de interrrupção do ciclo + mensagem de finalização
        lines()
        enter_pass()
        lines()
        print('Finalizando...')
        sleep_general()
        break

    # Finalização ciclo de Cadastro  
    clear_screen()
    return dicio_cliente

# Corrige os dados cadastrados do cliente
def registration_correction(cad_position, lista_geral_reg_correction):
    '''
    Função responsável por corrigir os dados cadastrados do cliente.

    cad_position: Armazena a posição do cadastro na lista de exibição.
    Se for declarado na função visualizer_result(), ela já mostrará o resultado na posição de exibição, sem a necessidade de alteração.
    Se for declarado diretamente em algum ciclo, necessitará decrescer 1 p/ equalizar a lista de exibição.

    lista_geral_reg_correction: Recebe a lista geral
    '''

    # Ciclo principal
    while True:
        # Função de exibição de dados de cadastro selecionado + menu principal da função
        opc_cont_rc = opc_continuation('Correção de cadastro',visualizer_result(cad_position, lista_geral_reg_correction),'1 - Corrigir dados\n2 - Excluir cadastro\n0 - Sair',n1=0,n2=2)

        # Condicionais de entrada de menu principal da função
        
        # Opção de correção
        if opc_cont_rc == 1:
            # Limpeza de tela
            clear_screen()
            # Função responsável para fazer a correção - cad_position decresce 1 p/ igualar a posição que está na lista
            create_user(False, lista_geral_reg_correction, cad_position-1)
        
        # Opção de exclusão
        elif opc_cont_rc == 2:
            # Limpeza de tela
            clear_screen()

            # Variável responável pelo texto interno do mini menu
            txt_local_rc = f'ATENÇÃO, deseja excluir:\nNome: {lista_geral_reg_correction[cad_position-1]['nome']}\nCPF: {lista_geral_reg_correction[cad_position-1]['cpf']}'
            
            # Mini menu de alerta - aviso se quer realmente excluir cadastro
            opc_rc = opc_continuation('Exclusão de cadastro',txt_local_rc, '1 - SIM, exclusão permanente de dados\n2 - NÃO',n1=1,n2=2)
            
            # Condições de mini menu

            # Opção p/ exclusão de cadastro
            if opc_rc == 1:
                lines()
                del lista_geral_reg_correction[cad_position-1]
                print('Excluindo cadastro...')
                sleep_general()
                clear_screen()
                break
            
            # Opção p/ retornar
            elif opc_rc == 2:
                lines()
                print('Voltando...')
                sleep_general()
                clear_screen()
        
        # Opção de encerramento
        elif opc_cont_rc == 0:
            lines()
            print('Retornando p/ lista de cadastros.')
            sleep_general()
            clear_screen()
            break

# Apresenta a lista de exibição de clientes cadastrados p/ consultas e alterações.
def check_user(def_lista_geral):
    '''
    Função responsável pela apresentação dos cadastros.
    Mostra a lista de clientes cadastrados.
    Fornece a opção de visualização detalhada do cadastro.
    A opção de visualização do cadastro pode ser feito pelo número sequêncial ou cpf.
    Retornará a posição do cadastro pesquisado na lista geral.

    '''
    # Texto inserido no título
    txt = 'Lista de clientes'
    
    # Condição p/ lista vazia - sem cadastros
    if def_lista_geral == []:
        # Apresentação das informações
        titles(txt)

        # Informação de lista vazia
        print('Sem cadastros adicionados.')

         # Finalização da lista
        cicle_view = False
        lines()
        enter_pass()
        lines()
        print('Voltando p/ menu principal.')
        sleep_general()
        clear_screen()
        return cicle_view
    
    # Condição para exibição de lista preenchida
    else:
        # Opções de visualização de perfil ou voltar a menu principal
        while True:
            try:
                # Apresentação de titulo
                titles(txt)

                # Visualização de lista de clientes cadastrados
                view_registration(def_lista_geral)

                # Linha divisória
                lines()

                opc_continue = int(input('N° - Sequência ou CPF p/ pesquisa\n0  - Voltar menu\nOpção: '))

                # Condicionais de erro expecíficas
                # Opc menor do que 0
                if opc_continue < 0:
                    raise ValueError
                # Qtd. de caracteres maior do que 11
                if len(str(opc_continue)) > 11:
                    raise ValueError
                # Encerrar página
                if opc_continue == 0:
                    break
            
            except ValueError:
                lines()
                print('Inválido...Tente novamente.')
                sleep_general()
                clear_screen()
            
            else:
                # Limpar tela anterior
                clear_screen()

                # Título de apresentação
                titles(txt)

                # Pesquisa pela n° sequencial
                if len(str(opc_continue)) < 11:

                    # Opção não contida na lista
                    if opc_continue > len(def_lista_geral):
                        print('Cadastro não encontrado.')
                        lines()
                        enter_pass()
                        clear_screen()
                        continue

                    else:
                        # Passar o valor da posição da pesquisa para a variável position_view
                        position_view = opc_continue
                        clear_screen()
                        # Retornando a posição pesquisada pela sequência
                        return position_view

                # Pequisa pelo CPF
                elif len(str(opc_continue)) == 11:
                    
                    # Flag p/ confirmar a presença do conteúdo pesquisado
                    cadastro_pesq = False

                    # Acessando lista
                    for pos_result, cont_result in enumerate(def_lista_geral):

                        # Acessando dicionários
                        for key_result, value_result in def_lista_geral[pos_result].items():

                            # Condição para mostrar resultado de dicionário
                            if opc_continue == int(def_lista_geral[pos_result]['cpf'].replace('.','').replace('-','')):
                                
                                # Flag confirmando a presença do conteúdo pesquisado
                                cadastro_pesq = True
                                # Passar o valor da posição da pesquisa para a variável position_view
                                # Nesse caso + 1, pois pos_result retorna a posição do cadastro na lista geral.
                                position_view = pos_result+1
                                clear_screen()

                                # Retornando a posição pesquisada pelo CPF
                                return position_view

                    # Condicional de cadastro não encontrado
                    if cadastro_pesq == False:
                        print('Cadastro não encontrado.')
                        # Precione enter p/ continuar
                        lines()
                        enter_pass()
                        clear_screen()
                        continue

    # Finalização da lista
    lines()
    print('Voltando p/ menu principal.')
    sleep_general()
    clear_screen()

    # Condição de finalização do ciclo de interação do visualizador da lista com a função de correção p/ encerramento na função de execução principal
    if opc_continue == 0:
        cicle_view = False
        return cicle_view

# Pesquisa os cadastros e retorna sua posição na lista de exibição (não da lista geral) para ligar a outra função, que executará seu comando no cadastro selecionado.
def search_list(txt_tilte_local, txt_notif_local, list_search_list):
    '''
    Responsável por pesquisar a lista de cadastros.
    Fornece as opções de pesquisar pelo CPF ou n° sequencial da lista.
    Depois de pesquisado ele retornará a posição do cadastro pesquisado.

    txt_tilte_local: Armazena o complemento do título.
    txt_notif_local: Armazena a mensagem entre o título e o menu local
    list_search_list: Recebe a lista geral para manipulação da posição dos dados pretendidos.
    '''
    
    # Informação das opções de menu local
    txt_menu_local = '1 - Pesquisar por CPF\n2 - Pesquisar por lista\n0 - Voltar p/ menu principal'
    # Variável flag responsável por interromper programa - False p/voltar no menu e True p/ encerrar 
    go_back = True
    # Declaração da variável que receberá a posição do cadastro selecionado.
    opc_search_register = 0
    
    # Ciclo principal
    while True:

        # Apresentação de menu local + entrada de opções
        opc_account_user = opc_continuation(txt_tilte_local, txt_notif_local, txt_menu_local, n1=0, n2=2)
        
        # Opcões de comando local

        # 0 - p/ sair do menu
        if opc_account_user == 0:
            # Indicaca que o programa deve interromper o cadastro
            go_back = False

            # Mensagem de retorno ao menu principal
            lines()
            print('Voltando...')
            sleep_general()

            # Finalização local - limpar tela
            clear_screen()
            break
        
        # 1 - p/ pesquisar por cpf e retorna a posição do cadastro selecionado
        elif opc_account_user == 1:

            # Limpando tela anterior
            clear_screen()

            # Condicional de visualização de lista - lista_geral vazia
            if list_search_list == []:

                # Informações de título - mensagem na tela e demais funções p/ estética e de passagem. Volta p/ menu anterior.
                titles(txt_tilte_local)
                print('Não há clientes cadastrados.')
                lines()
                enter_pass()
                clear_screen()
                continue

            else:
                # Ciclo de pesquisa pelo CPF
                while True:
                    # Informações da tela de entrada do CPF
                    try:
                        titles(txt_tilte_local)
                        opc_search_register = int(input('Informe CPF ou 0 p/voltar:\n'))

                        # Condicionais
                        # Opção de retornar
                        if opc_search_register == 0:
                            # Evita de sair do ciclo principal por causa do break.
                            go_back = False

                            # Mensagem de volta
                            lines()
                            print('Voltando...')
                            sleep_general()
                            clear_screen()
                            break

                        # CPF inválido
                        if len(str(opc_search_register)) != 11:
                            raise Exception

                    except ValueError:
                        lines()
                        print('Erro...Tente novamante.')
                        sleep_general()
                        clear_screen()

                    except Exception:
                        lines()
                        print('CPF inválido.')
                        sleep_general()
                        clear_screen()
                    
                    else:

                        # Flag p/ confirmar a presença de conteúdo pesquisado
                        search_cpf = False

                        # Acessa a lista geral de cadastros
                        for pos_cpf, cont_cpf in enumerate(list_search_list):
                            # Procura o dicionário pesquisado
                            for key_cpf, value_cpf in cont_cpf.items():
                                # Condicional p/ exibir cadastro de cpf pesquisado
                                if opc_search_register == int(cont_cpf['cpf'].replace('.','').replace('-','')):
                                    # Confirmação de conteúdo - Flag p/ saber se a pesquisa tem resultado
                                    search_cpf = True
                                    # Confirma ou retoma o valor True p/ variável go_back. Em caso dela se tornar False em desistência de pesquisa anterior. Necessário p/ o devido avanço do ciclo.
                                    go_back = True
                                    # Repassando o valor da posição do cadastro na lista geral p/ varíavel de pesquisa. + 1 p/ equalizar com a lista de exibição
                                    opc_search_register = pos_cpf + 1
                                    # Interrompe ciclo p/ retornar o valor da posição do cadastro pesquisado
                                    break
                            
                        # Interrompe o ciclo de busca de cadastro na lista geral. Evita que as variáveis tomem outros valores em demais ciclos.
                        if search_cpf == True:
                            break

                        # Condicional p/ exibir tela de conteúdo não localizado na pesquisa
                        elif search_cpf == False:
                            lines()
                            print('Cadastro não encontrado...Tente novamente.')
                            sleep_general()
                            clear_screen()
                            continue

            # Finaliza o ciclo principal em relação ao último estagio - Cadastro já definido
            if go_back == True:
                break
        
        # 2 - Pesquisa pela lista e retorna a posição do cadastro selecionado
        elif opc_account_user == 2:

            # Limpando tela anterior
            clear_screen()

            # Condicional de visualização de lista - lista_geral vazia
            if list_search_list == []:

                # Informações de título - mensagem na tela e demais funções p/ estética e de passagem. Volta p/ menu anterior.
                titles(txt_tilte_local)
                print('Não há clientes cadastrados.')
                lines()
                enter_pass()
                clear_screen()
                continue

            else:
                # Ciclo de pesquisa pelo número sequencial da lista de cadastros
                while True:
                    try:
                    # Informações de página de entrada
                        titles(txt_tilte_local)
                        view_registration(list_search_list)
                        lines()
                        # Menu local
                        opc_search_register = int(input('N° sequencial para selecionar cadastro\n0 - Voltar\nOpção: '))

                        # Condicionais de mini menu local
                        if opc_search_register == 0:
                            go_back = False
                            lines()
                            print('Voltando...')
                            sleep_general()
                            clear_screen()
                            break

                        if opc_search_register > len(list_search_list):
                            raise Exception
                        
                        if opc_search_register < 0:
                            raise ValueError

                    except ValueError as error:
                        lines()
                        print('Entrada inválida...Tente novamente.')
                        sleep_general()
                        clear_screen()
                    
                    except Exception as error:
                        lines()
                        print('Cadastro não encontrado...Tente novamente.')
                        sleep_general()
                        clear_screen()


                    else:
                        # Variável de interrupção de ciclo principal
                        go_back = True

                        # Encerrar ciclo p/ que função retorne a posição do cadastro selecionado
                        break

                # Finaliza o ciclo principal em relação ao último estagio - Cadastro já definido
                if go_back == True:
                    break

    # Finalização
    clear_screen()

    return opc_search_register, go_back

# Realiza o a criacão e vinculação de conta com o cadastro selecionado
def account_registration(list_general_reg, list_account_reg, opc_search, numbering_ac, *,txt_tilte_local_ac):
    '''
    Área responsável pelo cadastro da conta.
    Recebe a lista geral, lista de contas e a posição da lista geral a ser alterada.
    Exibe uma tela com os dados do cliente e da conta cadastrada.

    Variáveis

    list_general_reg: Recebe a lista geral de cadastros.
    list_account_reg: Recebe a lista de cadastro que possuem contas.
    opc_search: Recebe a posição na lista geral do cadastro que receberá uma nova conta.
    numbering_ac: Recebe o número da última conta cadastrada, que será o parametro para o cadastramento da próxima conta.
    txt_tilte_local_ac: Recebe a informação que segue junto ao título da tela em exibição.

    '''

    # Exibição de cadastro selecionado

    # Variáveis da função de exibição - Opc_search NÃO decresce 1 pois a função visualizer_result já o faz.
    txt_opc_local = '1 - Cadastrar conta\n0 - Voltar'
    print_definitive = visualizer_result(opc_search, list_general_reg)

    # Exibição do cadastro em mini-menu de continuação.
    opc_continuation_ar = opc_continuation(txt_title = 'Cadastro de Contas', txt_notif = print_definitive, txt_opc = txt_opc_local, n1=0,n2=1)

    # Condições de mini meni local

    # 1 - Cadastramento de conta
    if opc_continuation_ar == 1:

        # Mensagem informando a criação da conta - Opc_search decresce 1 p/ equalizar com lista geral.
        lines()
        print('Criando conta p/:')
        print(f'Cliente: {list_general_reg[opc_search-1]['nome']}')
        print(f'CPF: {list_general_reg[opc_search-1]['cpf']}')
        lines()
        sleep_general()
        clear_screen()
                        
        # Preenchimento do número da conta
        numbering_ac += 1
        numero_conta = f'{numbering_ac:05d}'
        numero_agencia = f'{1:03d}'

        # Dicionário de conta padrão
        conta_unica = {
            'cliente':{'nome cliente':list_general_reg[opc_search-1]['nome'],
                       'cpf cliente': list_general_reg[opc_search-1]['cpf']},
            'conta':{'n° conta': numero_conta, 'agencia': numero_agencia},
            'movimentação':[],
            'propriedades':{'saldo': 0, 'limite': 0}
            }

        # Adicionando os dados da conta no dicionário do cliente 
        list_general_reg[opc_search-1]['contas'].append(conta_unica['conta'])

        # Adicionando dicionário de conta única a lista de contas
        list_account_reg.append(conta_unica)

        # Exibição de lista - Exibe apenas nome, cpf e números da conta e agência.
        titles(txt_tilte_local_ac)
        print('Conta criada com sucesso:')
        lines()

        # Flag usada para pausar execução quando chegar na posição da movimentação
        position = 0
        # Apresentação de dados cadastrais - nome, cpf, conta e ag.
        for key_1, value_1 in conta_unica.items():
            if position == 2:
                break
            for key_2, value_2 in value_1.items():
                print(f'{key_2.title()}: {value_2}')
            position +=1

        lines()
        enter_pass()
        lines()
        print('Carregando menu cadastro de conta.')
        sleep_general()
        clear_screen()
        return list_general_reg, list_account_reg, numbering_ac
    
    # 0 - Opção de voltar
    elif opc_continuation_ar == 0:
        lines()
        print('Voltando...')
        sleep_general()
        clear_screen()
        return list_general_reg, list_account_reg, numbering_ac

# Realiza as transações bancárias
def bank_transaction(list_general_bt, list_account_bt, opc_search_bt):
    '''
    Função responsável por realizar as transações bancárias dos clientes.
    Função manipulará a lista de contas.
    A lista geral será usada para exibir as informações do cliente e p/ localizar a posição do cadastro da lista de contas.

    Args_
    list_general_bt: Recebe a lista geral de cadastros
    list_account_bt: Recebe a lista de contas cadastradas
    opc_search_bt: Recebe a posição do cadastro em relação a lista de exibição. Importante decrescer 1 p/ equalizar a lista geral.
    '''
    
    # Declaração de variáveis

    # Descrição de título padrão p/ todos menus locais
    txt_bt = 'Movimentação'

    # Lista que contém a posição dos cadastros que têm contas na lista de contas.
    list_pos_account_in_list = list()

    # Armazena as informações do cliente em uma string. Servirá p/ exibição na mensagem informativa no menu de escolha de conta a ser movimentada.
    lines_ac = lines() # Exibe um linha divisória na mensagem que será exibida
    clear_screen() # Limpa as linhas do lines() acima.
    info_client = f'Cliente: {list_general_bt[opc_search_bt-1]['nome']}\nCPF: {list_general_bt[opc_search_bt-1]['cpf']}\n{lines_ac}\nEscolha uma conta a ser movimentada'

    # Armazena a posição da conta no menu de exibição
    pos_account_in_menu = 1

    # Armazena informação das contas listadas para exibição em menu de escolha de conta a ser movimentada
    account_string = 'Contas listadas:'

    # Ciclo responsável por identificar contas pertencentes a cadastro selecionado
    for pos, cont in enumerate(list_account_bt):

        for key, value in cont.items():

            # Pesquisa as contas do cliente a partir do CPF da lista geral em relação ao CPF da lista de contas
            if list_general_bt[opc_search_bt-1]['cpf'] == cont['cliente']['cpf cliente']:
                
                # Lista que armazena a localização das contas na lista de contas
                list_pos_account_in_list.append(pos)

                # String que armazena as informações das contas cadastradas
                account_string += f'\n{pos_account_in_menu} - Conta:{list_account_bt[pos]['conta']['n° conta']} Agência: {list_account_bt[pos]['conta']['agencia']}'

                # Adicionando mais 1 p/ exibição de possível outra conta
                pos_account_in_menu += 1
                
                break
    
    # Finalização de mensagem p/ exibição em menu de escolha de conta a ser movimentada
    account_string += '\n0 - Voltar'
    
    # Mensagem p/ caso não haja conta vinculada ao cliente
    if list_pos_account_in_list == []:
        account_string = 'Nenhuma conta vincula ao cliente\n0 - Voltar'
    
    # Declaração de funções

    # Deposito
    def bank_deposit(info_client_bank_deposit, position_bank_deposit, list_ac_bank_deposit):
        '''
        Função responsável por conter e manipular informações referentes a deposito.
        
        Args:
        info_client_bank_deposit: Recebe os dados principais do cliente(Nome, CPF, Conta e Agência). 
        position_bank_deposit: Recebe a posição da conta selecionada na lista de contas.
        list_ac_bank_deposit: Recebe a lista de contas. Que será manipulada e retornada no final.

        '''

        # Limpa tela anterior
        clear_screen()
        
        # Menu local para transação de depositos - Limite de 500000 por deposito.
        opc_bank_deposit = opc_continuation('Depósito', info_client_bank_deposit, 'Valor de deposito [0 p/ encerrar]:', n1=0, n2=500000)

        if opc_bank_deposit == 0:
            lines()
            print('Sem deposito. Encerrando...')
            sleep_general()
            clear_screen()
            return list_ac_bank_deposit
        
        else:
            # Manipulação de dados relativos ao deposito

            # Marcação da data da transação
            data_now = datetime.now()
            # Conversão da data de transação para padrão BR
            date_now_convertion = data_now.strftime('%d/%m/%Y %H:%M:%S')
            # Inserção de dados do depósito em um dicionário local de organização
            transaction = {'depósito': opc_bank_deposit, 'horário': date_now_convertion}
            # Inserção de dados do depósito na lista de contas.
            list_ac_bank_deposit[position_bank_deposit]['movimentação'].append(transaction)
            # Atualização do campo de saldo do dicionário de propriedades da lista de contas
            list_ac_bank_deposit[position_bank_deposit]['propriedades']['saldo'] += opc_bank_deposit

            # Mensagem de confirmação da transação
            '''
            Valor de entrada (opc_bank_deposit) é convertido em str p/ exibição de valor depositado.
            Um 0 é acrescentado no final da exibição caso tenha menos de 2 casas decimais informadas na entrada.
            '''
            str_deposit = str(list_ac_bank_deposit[position_bank_deposit]['movimentação'][-1]['depósito']).replace('.', ',')
            lines()
            print('Deposito realizado com sucesso.')
            print(f'Valor depositado: R${str_deposit}',end='')
            print('0' if len(str_deposit.split(',')[-1]) == 1 else '')

            # Finalização de deposito bem sucedido
            lines()
            enter_pass()
            clear_screen()

            return list_ac_bank_deposit

    # Saque
    def bank_withdrawal(info_client_bank_withdrawal, position_bank_withdrawal, list_ac_bank_withdrawal):
        '''
        Função responsável por conter e manipular informações referentes a saque.
        
        Args:
        info_client_bank_withdrawal: Recebe os dados principais do cliente(Nome, CPF, Conta e Agência). 
        position_bank_withdrawal: Recebe a posição da conta selecionada na lista de contas.
        list_ac_bank_withdrawal: Recebe a lista de contas. Que será manipulada e retornada no final.

        '''

        # Limpa tela anterior
        clear_screen()
        
        # Menu local para transação de saques - Limite de 500000 por saque.
        opc_bank_withdrawal = opc_continuation('Saque', info_client_bank_withdrawal, 'Valor de saque [0 p/ encerrar]:', n1=0, n2=500000)

        if opc_bank_withdrawal == 0:
            lines()
            print('Nenhum saque. Encerrando...')
            sleep_general()
            clear_screen()
            return list_ac_bank_withdrawal
        
        elif opc_bank_withdrawal > list_ac_bank_withdrawal[position_bank_withdrawal]['propriedades']['saldo']:
            lines()
            print('Saldo insuficiente. Encerrando...')
            sleep_general()
            clear_screen()
            return list_ac_bank_withdrawal
        
        else:
            # Manipulação de dados relativos a saque

            # Marcação da data da transação
            data_now = datetime.now()
            # Conversão da data de transação para padrão BR
            date_now_convertion = data_now.strftime('%d/%m/%Y %H:%M:%S')
            # Inserção de dados do saque em um dicionário local de organização
            transaction = {'saque': opc_bank_withdrawal, 'horario': date_now_convertion}
            # Inserção de dados de saque na lista de contas.
            list_ac_bank_withdrawal[position_bank_withdrawal]['movimentação'].append(transaction)
            # Atualização do campo de saldo do dicionário de propriedades da lista de contas
            list_ac_bank_withdrawal[position_bank_withdrawal]['propriedades']['saldo'] -= opc_bank_withdrawal

            # Mensagem de confirmação da transação
            '''
            Valor de entrada (opc_bank_withdrawal) é convertido em str p/ exibição de valor sacado.
            Um 0 é acrescentado no final da exibição caso tenha menos de 2 casas decimais informadas na entrada.
            '''
            str_withdrawal = str(list_ac_bank_withdrawal[position_bank_withdrawal]['movimentação'][-1]['saque']).replace('.', ',')
            lines()
            print('Saque realizado com sucesso.')
            print(f'Valor sacado: R${str_withdrawal}',end='')
            print('0' if len(str_withdrawal.split(',')[-1]) == 1 else '')

            # Finalização de saque bem sucedido
            lines()
            enter_pass()
            clear_screen()

            return list_ac_bank_withdrawal

    # Extrato
    def bank_statement(info_client_bank_statement, position_bank_statement, list_ac_bank_statement):
        '''
        Função responsável exibir informações referentes as movimentações do cliente selecionado.
        
        Args:
        info_client_bank_statement: Recebe os dados principais do cliente(Nome, CPF, Conta e Agência). 
        position_bank_statement: Recebe a posição da conta selecionada na lista de contas.
        list_ac_bank_statement: Recebe a lista de contas. Que será manipulada e retornada no final.

        '''
        # Limpeza de tela anterior
        clear_screen()

        # Título da página
        titles('Extrato')

        # Apresentação das informações do cliente
        print(info_client_bank_statement)
        
        # Linha divisória
        lines()

        # Apresentação de monvimentações
        print('Movimentação de conta:\n')

        # Ciclo que apresenta movimentação feitas

        for pos_bs, cont_bs in enumerate(list_ac_bank_statement[position_bank_statement]['movimentação']):
            # Acessando dicionário de movimentação e horário
            for key_bs, value_bs in cont_bs.items():

                # Tratamento de saída de valores movimentados. Padrão finaceiro (R$, uso de vírgula e dois 0s no final)
                str_value_bs = str(value_bs).replace('.', ',')

                if len(str_value_bs.split(',')[-1]) == 1:
                    str_value_bs += '0'
                
                if key_bs == 'depósito' or key_bs == 'saque':
                    str_value_bs = 'R$'+str_value_bs
                
                # Saída de informações
                print(f'{key_bs.title()}: {str_value_bs}')

            print()
        
        # Apresentação de saldo em conta
        lines()
        str_bank_balance = str(list_ac_bank_statement[position_bank_statement]['propriedades']['saldo']).replace('.', ',')
        print(f'Saldo: R${str_bank_balance}',end='')
        print('0' if len(str_bank_balance.split(',')[-1]) == 1 else '')

        # Finalização de extrato
        lines()
        enter_pass()
        lines()
        print('Encerrando consulta...')
        sleep_general()
        clear_screen()

    # Ciclo p/ escolha de conta ser movimentada
    while True:

        # Menu p/ exibir conta selecionada
        opc_bt = opc_continuation(txt_bt, info_client, account_string, n1=0, n2= len(list_pos_account_in_list))
    
        # Opção p/ voltar
        if opc_bt == 0:

            # Mensagem de saída
            lines()
            print('Voltar...')
            sleep_general()
            clear_screen()
            break
        
        # Opção de seleção de alguma conta cadastrada
        else:
            '''
            Linha de acesso:
            lista de contas(list_account_bt) recebe a posição da lista de posição de contas(list_pos_account_in_list),
            que recebe a posição do menu de exibição de contas (opc_bt) menos 1 p/ igualar com a posição da lista de posições de contas.
            
            list_account_bt[list_pos_account_in_list[opc_bt-1]]['conta']
            '''

            # Limpa tela anterior
            clear_screen()

            # Posição do cadastro em lista de contas selecionado
            position_in_list_account = list_pos_account_in_list[opc_bt-1]

            # Informações de cliente p/ menu local
            info_client_account = f'Cliente: {list_general_bt[opc_search_bt-1]['nome']}' 
            info_client_account += f'\nCPF: {list_general_bt[opc_search_bt-1]['cpf']}'
            info_client_account += f'\nConta: {list_account_bt[position_in_list_account]['conta']['n° conta']}'
            info_client_account += f'\nAgência: {list_account_bt[position_in_list_account]['conta']['agencia']}'
            
            # Informações de opções p/ menu local
            menu_opc_transactions = 'Opcões de transações:\n1 - Deposito\n2 - Saque\n3 - Extrato\n0 - Voltar'
            
            # Ciclo p/ movimentar conta
            while True:

                # Menu p/ movimentação de conta selecionada
                opc_transactions = opc_continuation(txt_bt, info_client_account, menu_opc_transactions, n1=0, n2=3)

                # Opções de transações

                # Encerramento 
                if opc_transactions == 0:

                    # Mensagem de volta. Retornará p/ menu de escolha de conta.
                    lines()
                    print('Voltando...')
                    sleep_general()
                    clear_screen()
                    break

                # Deposito
                elif opc_transactions == 1:

                    # Função de deposito. Retorna o valor da lista de contas
                    list_account_bt = bank_deposit(info_client_account, position_in_list_account, list_account_bt)

                    continue

                # Saque
                elif opc_transactions == 2:

                    # Função de saque. Retorna o valor da lista de contas
                    list_account_bt = bank_withdrawal(info_client_account, position_in_list_account, list_account_bt)

                    continue

                # Extrato
                elif opc_transactions == 3:

                    # Função de verificação de extrato bancário.
                    bank_statement(info_client_account, position_in_list_account, list_account_bt)

                    continue

    #print('Encerrando...\nÚltimo ponto p/ sair da função.')
    #enter_pass()
    #clear_screen()

    return list_account_bt

def programer_area(general_list_pa, account_list_pa):

    while True:
        opc_ti = opc_continuation('Testes TI', 'Escolha lista específica','1 - Lista geral\n2 - Lista de contas\n0 - Sair',n1=0,n2=2)
        
        if opc_ti == 1:
            clear_screen()
            for dados in general_list_pa:
                print(dados)
                lines()
            enter_pass()
            clear_screen()
        
        elif opc_ti == 2:
            clear_screen()
            for dados in account_list_pa:
                print(dados)
                lines()
            enter_pass()
            clear_screen()
            
        elif opc_ti == 0:
            lines()
            print('Encerrando...')
            sleep_general()
            clear_screen()
            break

    return general_list_pa, account_list_pa

# Programa princiapal
def main_program():
    '''
    Executa o programa principal
    '''

    # Declaração de listas e dicionários gerais
    lista_geral = list()
    lista_contas = list()
    cliente = dict()
    
    # Variável responsável pela numeração das contas registradas. Sempre adicionando mais 1 ao valor da última cadastrada.
    account_numbering = 0

    # Ciclo principal - Menu geral
    while True:
        local_opc = main_menu()

        # Opção de criação de cliente
        if local_opc == 1:
            # Função de criação de cliente
            cliente = create_user(True, lista_geral, None)

            # Inserindo cliente recem criado a lista geral de clientes - Se a entrada for vazia não adicionará na lista_geral
            if cliente != {}:
                lista_geral.append(cliente)
                # Colocando em ordem alfabética
                lista_geral = list_order(lista_geral).copy()
        
        # Pesquisa de cadastro + criação e vinculo de conta com cliente
        elif local_opc == 2:
            # Ciclo de interação de função de pesquisa com função de criação e vinculo de conta/cliente.
            while True:
                '''
                Ciclo será responsável por passar os retornos da pesquisa para a função de criação da conta(account_registration).
                
                search_list_variable: Recebe a posição do cadastro na lista_geral.
                go_back_definition: Recebe a flag de continuação do processo de cadastramento.
                '''
                # Função de pesquisa de cadastro - CPF ou posição, distintamente.
                search_list_variable, go_back_definition = search_list(txt_tilte_local = 'Cadastro de Contas', txt_notif_local = 'Escolha um cliente p/ cadastrar conta.', list_search_list = lista_geral)
                # Condição de continuação de programa
                if go_back_definition == False:
                    break
                
                lista_geral, lista_contas, account_numbering = account_registration(lista_geral, lista_contas, search_list_variable,account_numbering, txt_tilte_local_ac = 'Cadastro de Contas')
        
        # Exibe uma lista com os clientes cadastrados e opção de correção de cadastro.
        elif local_opc == 3:

            # Ciclo de interação do visualizador da lista geral com a função de correção
            while True:
                '''
                Ciclo responsável por interagir a função de pesquisa com a de correção
                pos_view: é o valor retornado da posição pesquisada.
                '''
                # Função que visualiza lista geral
                pos_view = check_user(lista_geral)
                # Condição de continuação de programa
                if pos_view == False:
                    break

                # Função responsável por corrigir cadastro selecionado
                registration_correction(pos_view, lista_geral)

                # Organizando em ordem alfabética
                lista_geral = list_order(lista_geral).copy()
        
        # Área de movimentação de contas
        elif local_opc == 4:

            # Ciclo interage as funções de pesquisa com o de movimentação de contas
            while True:
                '''
                Ciclo responsável por interagir a função de pesquisa com o de movimentação de contas.
                pos_view_bt: É o valor retornado da posição pesquisada.
                '''
                # Função de pesquisa de cadastro
                search_list_bt, pos_view_bt = search_list(txt_tilte_local = 'Movimentação Bancária', txt_notif_local = 'Escolha um cliente p/ transações.', list_search_list = lista_geral)
                
                # Condição de continuação de programa
                if pos_view_bt == False:
                    break

                # Função de transações bancárias - Retorna as movimentações p/ a lista de contas
                lista_contas = bank_transaction(lista_geral, lista_contas, search_list_bt)
        
        # Área do programador - Conferência de listas
        elif local_opc == 5:

            lista_geral, lista_contas = programer_area(lista_geral, lista_contas)                

        # Encerrar o programa
        elif local_opc == 0:
            titles('Encerramento')
            print('Encerrando programda...')
            sleep_general()
            print('Programa encerrado')
            break
    
    return lista_geral

# Execução da função principal - Programa principal
main_program()

