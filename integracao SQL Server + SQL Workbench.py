#importing dependencies
import pandas as pd
import numpy as np
import pymssql
import mysql.connector

#connecting into servers
connMS = pymssql.connect(server='1.1.1.1',
                        user="test",
                        password="test",
                        database='test',
                        host='1.1.1.1',
                        port='1433',)

conn = mysql.connector.connect(host='1.1.1.0',
                                port='3306',
                                database='test',
                                user='teste',
                                password= f'test')

#reading from sql workbench and creating csv with pandas
sql = "SELECT target from TableTarget where data = CURDATE();"
data = pd.read_sql(sql, conn)

#adding id with numpy
data.index = np.arange(1, len(data)+1)

data.to_csv('path/ControleEntrada.csv', header = False)

#drop table and create table to make sure that is a new one
cursorMS = connMS.cursor()
cursorMS.execute("DROP TABLE TableTarget")
cursorMS.execute("CREATE TABLE TableTarget([id] [bigint] IDENTITY(1,1) PRIMARY KEY NOT NULL,[target] [bigint] NOT NULL")

# Create a Procedure like this in the database
#   CREATE PROCEDURE [dbo].[sp_insert_TableTarget]
#   AS
#   BEGIN
#   	BULK INSERT TableTarget
#   	FROM 'path/ControleEntrada.csv'
#   	WITH (FORMAT='CSV')
#   END
#   GO

cursorMS.execute("execute [dbo].[sp_insert_TableTarget]")
connMS.commit()

#end connections
print('done.')
cursorMS.close()
connMS.close()
