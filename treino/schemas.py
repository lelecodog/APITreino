from ninja import ModelSchema, Schema
from .models import Alunos
from typing import Optional

class AlunoSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'email', 'data_nascimento', 'faixa']

class ProgressoAlunoSchema(Schema):
    email: str
    nome: str
    faixa: str
    total_aulas: int
    aulas_para_proxima_faixa: int

class AulaRealizadaSchema(Schema):
    qtd: Optional[int] = 1
    email_aluno: str

