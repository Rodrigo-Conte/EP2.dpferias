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
