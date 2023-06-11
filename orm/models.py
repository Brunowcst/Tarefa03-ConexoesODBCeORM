from peewee import *
import psycopg2

db = PostgresqlDatabase('postgres', user='EquipesDB', password='postgres123', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Funcionario(BaseModel):
    codigo = AutoField()
    nome = CharField(max_length=15, null=False)
    sexo = CharField(max_length=1, null=True, default=None)
    dataNasc = DateField(null=True, default=None)
    salario = DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    supervisor = ForeignKeyField('self', backref='subordinados', null=False, on_delete='SET_NULL', on_update='CASCADE')
    depto = DeferredForeignKey('Departamento', backref='funcionario', null=True, on_delete='SET_NULL', on_update='CASCADE')
    
    class Meta:
        table_name = 'funcionario'

class Departamento(BaseModel):
    codigo = AutoField()
    sigla = CharField(max_length=15, null=False, unique=True)
    descricao = CharField(max_length=25, null=False)
    gerente = ForeignKeyField(Funcionario, backref='departamentos', null=True, on_delete='SET_NULL', on_update='CASCADE')

    class Meta:
        table_name = 'departamento'

class Equipe(BaseModel):
    codigo = AutoField()
    nomeEquipe = CharField(max_length=45, null=True, default=None)

    class Meta:
        table_name = 'equipe'

class Projeto(BaseModel):
    codigo = AutoField()
    descricao = CharField(max_length=45, null=True, default=None)
    depto = ForeignKeyField(Departamento, backref='projetos', null=True, on_delete='SET_NULL')
    responsavel = ForeignKeyField(Funcionario, backref='projetos_responsavel', null=True, on_delete='SET_NULL')
    dataInicio = DateField(null=True, default=None)
    dataFim = DateField(null=True, default=None)
    situacao = CharField(max_length=45, null=True, default=None)
    dataConclusao = DateField(null=True, default=None)
    equipe = ForeignKeyField(Equipe, backref='projetos', null=True, on_delete='SET_NULL')

    class Meta:
        table_name = 'projeto'

class Atividade(BaseModel):
    codigo = AutoField()
    descricao = CharField(max_length=45, null=True, default=None)
    dataInicio = DateField(null=True, default=None)
    dataFim = DateField(null=True, default=None)
    situacao = CharField(max_length=45, null=True, default=None)
    dataConclusao = DateField(null=True, default=None)

    class Meta:
        table_name = 'atividade'

class AtividadeProjeto(BaseModel):
    codAtividade = ForeignKeyField(Atividade, backref='projetos', column_name='codAtividade')
    codProjeto = ForeignKeyField(Projeto, backref='atividades', column_name='codProjeto')

    class Meta:
        primary_key = CompositeKey('codProjeto', 'codAtividade')
        table_name = 'atividade_projeto'

class AtividadeMembro(BaseModel):
    codAtividade = ForeignKeyField(Atividade, backref='membros', column_name='codAtividade')
    codMembro = ForeignKeyField(Funcionario, backref='atividades', column_name='codMembro')

    class Meta:
        primary_key = CompositeKey('codAtividade', 'codMembro')
        table_name = 'atividade_membro'