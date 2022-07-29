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
