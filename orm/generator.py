from faker import Faker
import random
from models import *

fake = Faker()

def createDatas(qntInserts, cur):
    try:
        for _ in range(qntInserts):
            createFuncionario(cur)
            print("func passou")
            createDepto(cur)
            print("depto")
            createProjeto(cur)
            print("proj")
            createAtividade(cur)
            print("ativ")
            # createMembro()
            createAtividadeMembro(cur)
            print("ativMem")
            createEquipe(cur)
            print("equipes")
            
        cur.execute('COMMIT')
        print('Dados inseridos com sucesso.')

    except Exception as error:
        print('Erro ao inserir dados:', error)

def createFuncionario(cur):
    nome = fake.name()
    sexo = random.choice(['M', 'F'])
    datanasc = fake.date_of_birth(minimum_age=18, maximum_age=65)
    salario = random.uniform(1000, 5000)
    supervisor = random.choice(Funcionario.select())
    depto = random.choice(Departamento.select())
    Funcionario.create(nome=nome, sexo=sexo, datanasc=datanasc, salario=salario, supervisor=supervisor, depto=depto)

def createDepto(cur):
    sigla = fake.random_element(['FIN', 'HR', 'IT', 'SALES'])
    descricao = fake.sentence()
    gerente = random.choice(Funcionario)
    Departamento.create(sigla=sigla, descricao=descricao, gerente=gerente)

def createEquipe(cur):
    codigo = random.randint(1000, 9999)
    nomeequipe = fake.random_element(['Equipe A', 'Equipe B', 'Equipe C'])
    Equipe.create(codigo=codigo, nomeequipe=nomeequipe)

# def createMembro(cur):
#     codigo = random.randint(1000, 9999)
#     codEquipe = random.choice(Equipe.select())
#     codFuncionario = random.choice(Funcionario.select())
#     Membro.create(codigo=codigo, codEquipe=codEquipe, codFuncionario=codFuncionario)

def createProjeto(cur):
    codigo = random.randint(1000, 9999)
    descricao = fake.sentence()
    depto = random.choice(Departamento.select())
    responsavel = random.choice(Funcionario.select())
    dataInicio = fake.date_between(start_date='-1y', end_date='today')
    dataFim = fake.date_between(start_date=dataInicio, end_date='+1y')
    situacao = random.choice(['Em Andamento', 'Concluído'])
    dataConclusao = None
    if situacao == 'Concluído':
        dataConclusao = fake.date_between(start_date=dataFim, end_date='today')
    equipe = random.choice(Equipe.select())
    Projeto.create(codigo=codigo, descricao=descricao, depto=depto, responsavel=responsavel, dataInicio=dataInicio, dataFim=dataFim, situacao=situacao, dataConclusao=dataConclusao, equipe=equipe)

def createAtividade(cur):
    codigo = random.randint(1000, 9999)
    descricao = fake.sentence()
    dataInicio = fake.date_between(start_date='-1y', end_date='today')
    dataFim = fake.date_between(start_date=dataInicio, end_date='+1y')
    situacao = random.choice(['Em Andamento', 'Concluída'])
    dataConclusao = None
    if situacao == 'Concluída':
        dataConclusao = fake.date_between(start_date=dataFim, end_date='today')
    Atividade.create(codigo=codigo, descricao=descricao, dataInicio=dataInicio, dataFim=dataFim, situacao=situacao, dataConclusao=dataConclusao)

def createAtividadeMembro(cur):
    codAtividade = random.choice(Atividade)
    codProjeto = random.choice(Projeto)
    AtividadeMembro.create(codAtividade=codAtividade, codProjeto=codProjeto)

def createAtividadeProjeto(cur):
    codAtividade = random.choice(Atividade)
    codProjeto = random.choice(Projeto)
    AtividadeProjeto.create(codAtividade=codAtividade, codProjeto=codProjeto)
