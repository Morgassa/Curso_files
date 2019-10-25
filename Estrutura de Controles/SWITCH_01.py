def semana(dia):
    dias ={
        'segunda':'Dia de semana',
        'terça': 'Dia de semana',
        'quarta': 'Dia de semana',
        'quinta': 'Dia de semana',
        'sexta': 'Dia de semana',
        'sábado': 'Fim de semana',
        'domingo': 'Fim de semana',
    }
    return (dias.get(dia, '** inválido **'))


print(semana('cachorro'))