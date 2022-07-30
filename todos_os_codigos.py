def transforma_base(quests):
    dicionario = {}
    
    listaf = []
    listam = []
    listad = []
    
    for i in quests:
        for quest, nivel in i.items():
            if nivel == 'facil':
                listaf.append(i)

            elif nivel == 'medio':
                listam.append(i)
            
            elif nivel == 'dificil':
                listad.append(i)
         
    if len(listaf) != 0:
        dicionario['facil'] = listaf

    if len(listam) != 0: 
        dicionario['medio'] = listam
    
    if len(listad) != 0:
        dicionario['dificil'] = listad

    return dicionario

def valida_questao(quest):

    error = {}
    alternativa = ['A', 'B', 'C', 'D']

  

    if 'titulo' not in quest.keys():
        error['titulo'] = 'nao_encontrado'
    elif quest['titulo'] == '' or len(quest['titulo'].strip()) == 0 or "/t" in quest['titulo']:
        error['titulo'] = 'vazio'
    
    nivel = ['facil', 'medio', 'dificil']

    if 'nivel' not in quest.keys():  
        error['nivel'] = 'nao_encontrado'
    elif quest['nivel'] not in nivel:
        error['nivel'] = 'valor_errado'
    
    if len(quest.keys()) != 4:
        error['outro'] = 'numero_chaves_invalido'
        condicao = True

    

    condicao = True

    if 'opcoes' not in quest.keys():
        error['opcoes'] = 'nao_encontrado'
        condicao = False

    elif len(quest['opcoes'].keys()) != 4:
        error['opcoes'] = 'tamanho_invalido'
        condicao = False

    if condicao and  quest['opcoes'] == 'chave_invalida_ou_nao_encontrada':
       condicao = False

    if condicao == True:
        if 'A' not in quest['opcoes'].keys():
            error['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        
        elif 'B' not in quest['opcoes'].keys():
            error['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        elif 'C' not in quest['opcoes'].keys():
            error['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        elif 'D' not in quest['opcoes'].keys():
            error['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        else: 
            for opcao in alternativa:
                if opcao in quest['opcoes'].keys():
                    if quest['opcoes'][opcao] == '' or len(quest['opcoes'][opcao].strip()) == 0 or '/t' in quest['opcoes'][opcao]:
                        if 'opcoes' not in error:
                            error['opcoes'] = {}
                        error['opcoes'][opcao] = 'vazia'
    
    if 'correta' not in quest.keys():
        error['correta'] = 'nao_encontrado'

    elif quest['correta'] not in alternativa:
        error['correta'] = 'valor_errado'

    return error
def valida_questao(quest):

    error = {}
    alternativa = ['A', 'B', 'C', 'D']


    if 'titulo' not in quest.keys():
        error['titulo'] = 'nao_encontrado'
    elif quest['titulo'] == '' or len(quest['titulo'].strip()) == 0 or "/t" in quest['titulo']:
        error['titulo'] = 'vazio'
    
    nivel = ['facil', 'medio', 'dificil']

    if 'nivel' not in quest.keys():  
        error['nivel'] = 'nao_encontrado'
    elif quest['nivel'] not in nivel:
        error['nivel'] = 'valor_errado'
    
    if len(quest.keys()) != 4:
        error['outro'] = 'numero_chaves_invalido'
        condicao = True

    

    condicao = True

    if 'opcoes' not in quest.keys():
        error['opcoes'] = 'nao_encontrado'
        condicao = False

    elif len(quest['opcoes'].keys()) != 4:
        error['opcoes'] = 'tamanho_invalido'
        condicao = False

    if condicao and  quest['opcoes'] == 'chave_invalida_ou_nao_encontrada':
       condicao = False

    if condicao == True:
        if 'A' not in quest['opcoes'].keys():
            error['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        
        elif 'B' not in quest['opcoes'].keys():
            error['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        elif 'C' not in quest['opcoes'].keys():
            error['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        elif 'D' not in quest['opcoes'].keys():
            error['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        else: 
            for opcao in alternativa:
                if opcao in quest['opcoes'].keys():
                    if quest['opcoes'][opcao] == '' or len(quest['opcoes'][opcao].strip()) == 0 or '/t' in quest['opcoes'][opcao]:
                        if 'opcoes' not in error:
                            error['opcoes'] = {}
                        error['opcoes'][opcao] = 'vazia'
    
    if 'correta' not in quest.keys():
        error['correta'] = 'nao_encontrado'

    elif quest['correta'] not in alternativa:
        error['correta'] = 'valor_errado'

    return error

def valida_questoes(lista):
    erros=[]
    for i in lista:
        validacao=valida_questao(i)
        erros.append(validacao)
    return erros
import random
def sorteia_questao(dic, nivel):
    sort=random.choice(dic[nivel])
    return sort
import random
def sorteia_questao_inedida(dic, nivel, lista):
    sort=random.choice(dic[nivel])
    lista.append(sort)
    return sort
def questao_para_texto(dic,num):

    var_x = ''
    tracos = '------------------------------------- '
    inicio = 'QUESTAO' + ' ' + str(num) + '\n\n'
    d = dic['titulo'] + '\n\n'
    e = 'RESPOSTAS:\n'

    for letra, texto in dic['opcoes'].items():
        var_x += (f'{letra}: {texto}' '\n')
    
    final = tracos + inicio + d + e + var_x

    return final
def gera_ajuda(dicionario):
    lista=[]
    for quest, resp in dicionario['opcoes'].items():
        if quest!=dicionario['correta']:
            lista.append(resp)
    sort=random.randint(1,2)
    mod=random.sample(lista, sort)
    dica='DICA:\n'
    dica += 'Opções certamente erradas:' + ' | '.join(mod)
    return dica
