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
