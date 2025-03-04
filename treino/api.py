from ninja import Router
from .schemas import AlunoSchema, ProgressoAlunoSchema, AulaRealizadaSchema
from .models import Alunos, AulasConcluidas
from ninja.errors import HttpError
from typing import List
from .graduacao import *
from datetime import date

treino_router = Router()

@treino_router.post('', response={200: AlunoSchema})
def criar_aluno(request, aluno_schema: AlunoSchema):
    nome = aluno_schema.dict()['nome']
    email = aluno_schema.dict()['email']
    data_nascimento = aluno_schema.dict()['data_nascimento']
    faixa = aluno_schema.dict()['faixa']

    if Alunos.objects.filter(email=email).exists():
        raise HttpError(400, 'Email já cadastrado')
    
    aluno = Alunos(**aluno_schema.dict()) #descompresao de dados = aluno = Alunos(nome=nome, email=email, data_nascimento=data_nascimento, faixa=faixa)
    aluno.save()

    return aluno

@treino_router.get('/alunos/', response=List[AlunoSchema])
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos

@treino_router.get('/progresso_aluno/', response={200: ProgressoAlunoSchema})
def progresso_aluno(request, email_aluno: str):
    aluno = Alunos.objects.get(email=email_aluno)
    faixa_atual = aluno.get_faixa_display()
    n = order_belt.get(faixa_atual, 0)
    total_aulas_proxima_faixa = calcula_lesson_to_upgrade(n)
    total_aulas_concluidas_faixa = AulasConcluidas.objects.filter(aluno=aluno, faixa_atual=aluno.faixa).count()
    aulas_faltates = total_aulas_proxima_faixa - total_aulas_concluidas_faixa
    
    return {"email": aluno.email, "nome": aluno.nome, "faixa": faixa_atual, "total_aulas": total_aulas_concluidas_faixa, "aulas_para_proxima_faixa": aulas_faltates}

@treino_router.post('/aula_realizada/', response={200: str})   
def aula_realizada(request, aula_realizada: AulaRealizadaSchema):
    qtd = aula_realizada.dict()['qtd']
    email_aluno = aula_realizada.dict()['email_aluno']

    if qtd <= 0:
        raise HttpError(400, 'Quantidade de aulas inválida')
    aluno = Alunos.objects.get(email=email_aluno)

    for _ in range(0, qtd):
        ac = AulasConcluidas(
            aluno=aluno,
            faixa_atual=aluno.faixa
        )
        ac.save()

     # Verificar se o aluno atingiu o número necessário de aulas para a próxima faixa
    faixa_atual = aluno.get_faixa_display()
    n = order_belt.get(faixa_atual, 0)
    total_aulas_proxima_faixa = calcula_lesson_to_upgrade(n)
    total_aulas_concluidas_faixa = AulasConcluidas.objects.filter(aluno=aluno, faixa_atual=aluno.faixa).count()

    if total_aulas_concluidas_faixa >= total_aulas_proxima_faixa:
        # Atualizar a faixa do aluno
        nova_faixa = next((faixa for faixa, ordem in order_belt.items() if ordem == n + 1), None)
        if nova_faixa:
            aluno.faixa = nova_faixa[0]  # Atualizar a faixa do aluno (primeira letra da faixa)
            aluno.save()

    return 200, f"Aula marcada como realizada para o aluno {aluno.nome}"

@treino_router.put('/aluno/{aluno_id}', response=AlunoSchema)
def update_aluno(request, aluno_id: int, aluno_data: AlunoSchema):
    aluno = Alunos.objects.get(id=aluno_id)
    idade = date.today() - aluno.data_nascimento
    
    if int(idade.days/365) < 18 and aluno_data.dict()['faixa'] in ('A', 'R', 'M', 'P'):
        raise HttpError(400, 'Aluno menor de idade não pode receber essa faixa')
    
    for attr, value in aluno_data.dict().items():
        if value:
            setattr(aluno, attr, value)
    aluno.save()
    return aluno

@treino_router.delete('/aluno/{aluno_id}', response={200: str})
def delete_aluno(request, aluno_id: int):
    aluno = Alunos.objects.get(id=aluno_id)
    aluno.delete()
    return 200, f"Aluno {aluno.nome} deletado com sucesso"