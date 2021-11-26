#importando dependencias
import pandas as pd
import numpy as np
import pymssql
import mysql.connector

#conectando nos servidores
connMS = pymssql.connect(server='1.1.1.1',
                        user="teste",
                        password="teste",
                        database='teste',
                        host='1.1.1.1',
                        port='1433',)

conn = mysql.connector.connect(host='1.1.1.0',
                                port='3306',
                                database='teste',
                                user='teste',
                                password= f'teste')

#lendo do sql workbench e criando csv com pandas
sql = "SELECT cd_entrada from ControleEntrada where data = CURDATE();"
data = pd.read_sql(sql, conn)

#adicionando um id com numpy
data.index = np.arange(1, len(data)+1)

data.to_csv('caminho/ate/pasta/compartilhada/dentro/do/servidor/do/banco/ControleEntrada.csv', header = False)

#drop na tabela, cria a tabela e executa a procedure
cursorMS = connMS.cursor()
cursorMS.execute("DROP TABLE ControleEntrada")
cursorMS.execute("CREATE TABLE ControleEntrada([id] [bigint] IDENTITY(1,1) PRIMARY KEY NOT NULL,[codigo_entrada] [bigint] NOT NULL")

# Crie uma procedure no banco dessa forma
#   CREATE PROCEDURE [dbo].[sp_inserir_ControleEntrada]
#   AS
#   BEGIN
#   	BULK INSERT ControleEntrada
#   	FROM 'caminho/ate/pasta/compartilhada/dentro/do/servidor/do/banco/ControleEntrada.csv'
#   	WITH (FORMAT='CSV')
#   END
#   GO

cursorMS.execute("execute [dbo].[sp_inserir_ControleEntrada]")
connMS.commit()

#encerra a conexão
print('done.')
cursorMS.close()
connMS.close()