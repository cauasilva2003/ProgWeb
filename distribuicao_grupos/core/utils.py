import random
from datetime import datetime, timedelta

def alocar_alunos_e_sortear_grupos(tema, alunos):
    import random
    from datetime import datetime, timedelta

    random.shuffle(alunos)
    num_grupos = tema.quantidade_grupos
    grupos = [[] for _ in range(num_grupos)]

    for idx, aluno in enumerate(alunos):
        grupos[idx % num_grupos].append(aluno)

    ordem_apresentacao = list(range(num_grupos))
    random.shuffle(ordem_apresentacao)

    inicio = datetime.combine(datetime.today(), tema.horario_inicio)
    fim = datetime.combine(datetime.today(), tema.horario_fim)
    tempo_total = (fim - inicio).seconds // 60

    # Garante no mínimo 15 minutos por grupo
    tempo_por_grupo = max(15, tempo_total // num_grupos)

    horarios = [inicio + timedelta(minutes=i * tempo_por_grupo) for i in range(num_grupos)]

    return [
        {
            'nome': f'Grupo {i+1}',
            'alunos': grupos[i],
            'horario': horarios[ordem_apresentacao.index(i)].time(),
            'ordem': ordem_apresentacao.index(i) + 1
        } for i in range(num_grupos)
    ]
