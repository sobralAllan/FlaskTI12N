import conexaoBD
import mysql.connector

db_connection = conexaoBD.conexao()
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "Insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, dataDeNascimento)
        con.execute(sql)
        db_connection.commit()
        return con.rowcount,"Inserido!"
    except Exception as erro:
        return erro