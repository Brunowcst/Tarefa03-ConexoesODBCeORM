from faker import Faker
import random

fake = Faker()

def createDatas(conn, qntInserts):
    try:
        for _ in range(qntInserts):
            createFuncionario()
            createDepto()
            createProjeto()
            createAtividade()
            createMembro()
            createAtividadeMembro()
            createEquipe()
            
        conn.commit()
        print('Dados inseridos com sucesso.')

    except Exception as error:
        print('Erro ao inserir dados na tabela funcionario:', error)

def createFuncionario():
    codigo = random.randint(1000, 9999)
    nome = fake.name()
    sexo = random.choice(['M', 'F'])
    dataNasc = fake.date_of_birth(minimum_age=18, maximum_age=65)
    salario = random.uniform(1000, 5000)
    supervisor = random.choice(Funcionario.select())
    depto = random.choice(Departamento.select())
    Funcionario.create(codigo=codigo, nome=nome, sexo=sexo, dataNasc=dataNasc, salario=salario, supervisor=supervisor, depto=depto)

def createDepto():
    codigo = random.randint(1000, 9999)
    sigla = fake.random_element(['FIN', 'HR', 'IT', 'SALES'])
    descricao = fake.sentence()
    gerente = random.choice(Funcionario.select())
    Departamento.create(codigo=codigo, sigla=sigla, descricao=descricao, gerente=gerente)

def createEquipe():
    codigo = random.randint(1000, 9999)
    nomeEquipe = fake.random_element(['Equipe A', 'Equipe B', 'Equipe C'])
    Equipe.create(codigo=codigo, nomeEquipe=nomeEquipe)

def createMembro():
    codigo = random.randint(1000, 9999)
    codEquipe = random.choice(Equipe.select())
    codFuncionario = random.choice(Funcionario.select())
    Membro.create(codigo=codigo, codEquipe=codEquipe, codFuncionario=codFuncionario)

def createProjeto():
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

def createAtividade():
    codigo = random.randint(1000, 9999)
    descricao = fake.sentence()
    dataInicio = fake.date_between(start_date='-1y', end_date='today')
    dataFim = fake.date_between(start_date=dataInicio, end_date='+1y')
    situacao = random.choice(['Em Andamento', 'Concluída'])
    dataConclusao = None
    if situacao == 'Concluída':
        dataConclusao = fake.date_between(start_date=dataFim, end_date='today')
    Atividade.create(codigo=codigo, descricao=descricao, dataInicio=dataInicio, dataFim=dataFim, situacao=situacao, dataConclusao=dataConclusao)

def createAtividadeMembro():
    codAtividade = random.choice(atividades)
    codProjeto = random.choice(projetos)
    AtividadeMembro.create(codAtividade=codAtividade, codProjeto=codProjeto)

def createAtividadeProjeto():
    codAtividade = random.choice(atividades)
    codProjeto = random.choice(projetos)
    AtividadeProjeto.create(codAtividade=codAtividade, codProjeto=codProjeto)
