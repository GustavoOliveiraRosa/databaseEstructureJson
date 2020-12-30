#https://extendsclass.com/json-diff.html
import pymysql
from jsondiff import diff
import json

conexao = pymysql.connect(user='', passwd='', host='')

cursor = conexao.cursor()


## Verificando tabelas 
TablesArrayDevelopment = []
cursor.execute("USE **DATABASE**")
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
    ColumnsArrayDevelopment = []
    cursor.execute((str("DESCRIBE ")+str(table[0])))
    columns = cursor.fetchall()
    for column in columns:
        ColumnsArrayDevelopment.append({"coluna":column[0]})
    TablesArrayDevelopment.append({"tabela":table[0],"colunas":ColumnsArrayDevelopment})

with open('hml.json', 'w') as outfile:
    json.dump(TablesArrayDevelopment, outfile)


## Verificando tabelas 
TablesArrayProduction = []
cursor.execute("USE **DATABASE**")
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
    ColumnsArrayProduction = []
    cursor.execute((str("DESCRIBE ")+str(table[0])))
    columns = cursor.fetchall()
    for column in columns:
        ColumnsArrayProduction.append({"coluna":column[0]})
    TablesArrayProduction.append({"tabela":table[0],"colunas":ColumnsArrayProduction})

with open('production.json', 'w') as outfile:
    json.dump(TablesArrayDevelopment, outfile)



conexao.commit()

conexao.close()