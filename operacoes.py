import conexaoBD
import mysql.connector
import this
this.msg = ""
db_connection = conexaoBD.conexao()
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "Insert into pessoa(codigo, nome, telefone, dataDeNascimento, endereco) values('', '{}', '{}', '{}', '{}')".format(nome, telefone, dataDeNascimento, endereco)
        con.execute(sql)
        db_connection.commit()
        return con.rowcount,"Inserido!"
    except Exception as erro:
        return erro

def consultarTudo():
    try:
        sql = "select * from pessoa"
        con.execute(sql)

        this.msg = ""
        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            this.msg = this.msg + "Código: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
        return this.msg
    except Exception as erro:
        return erro

def consultar(cod):
    try:
        sql = "select * from pessoa where codigo = '{}'".format(cod)
        con.execute(sql)

        this.msg = ""
        this.msg = "Nenhum dado Encontrado!"
        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            if int(codigo) == int(cod):
                this.msg = "Código: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
                return this.msg
        return this.msg
    except Exception as erro:
        return erro

def atualizar(codigo, campo, novoDado):
    try:
        sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro

def deletar(codigo):
    try:
        sql = "delete from pessoa where codigo = '{}'".format(codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} deletado!".format(con.rowcount)
    except Exception as erro:
        return erro


