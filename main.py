from flask import Flask, render_template, request
import this
import operacoes
this.codigo = 0
this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.mensagem = ""
this.nDado = ""
this.campo = ""
this.dado = ""

pessoa = Flask(__name__) #Representando uma variável do tipo flask

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.data     = request.form['tNovaData']
        this.dados    = operacoes.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo='Página Principal', resultado=this.dados)

@pessoa.route('/consultar.html', methods=['GET', 'POST'])
def consultarTudo():
    if request.method == 'POST':
        this.mensagem = operacoes.consultarTudo()
    return render_template('consultar.html', titulo='Consultar', dados=this.mensagem)

@pessoa.route('/consultarCodigo.html', methods=['GET','POST'])
def consultarIndividual():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.mensagem = operacoes.consultar(this.codigo)
    else:
        this.mensagem = ""
    return render_template('consultarCodigo.html', titulo='Consultar por código', dados=this.mensagem)

@pessoa.route('/atualizar.html', methods=['GET','POST'])
def atualizarDados():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.nDado  = request.form['tNovoDado']
        this.dado = operacoes.atualizar(this.codigo, this.campo, this.nDado)
    return render_template('atualizar.html', titulo='Atualizar', resultado=this.dado)

@pessoa.route('/excluir.html', methods=['GET', 'POST'])
def excluirDados():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.dado   = operacoes.deletar(this.codigo)
    return render_template('excluir.html', titulo='Excluir', resultado=this.dado)

if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)