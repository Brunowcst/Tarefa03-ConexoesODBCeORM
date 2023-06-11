from peewee import *
import models

# Criação das tabelas
if __name__ == '__main__':
    """ initial """
    models.db.connect()
    models.db.create_tables([models.Funcionario,
                             models.Departamento,
                             models.Equipe,
                             models.Projeto,
                             models.Atividade,
                             models.AtividadeProjeto,
                             models.AtividadeMembro])
    
    models.db.close()

# https://docs.peewee-orm.com/en/latest/peewee/querying.html
# https://docs.google.com/document/d/1pEhJvmaZb_QBZvUhxBW_p1bHIv3mayhIpQIwG9OLsj4/edit