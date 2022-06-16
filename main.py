from flask import Flask, render_template, request
import this
import operacoes
this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""

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

if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)