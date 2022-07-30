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
