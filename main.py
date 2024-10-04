import flask#type:ignore
import mysql.connector#type:ignore

def conexao_banco():
    conexao_banco = mysql.connector.connect(
        host = 'database-1.c9gog0qy601g.us-east-2.rds.amazonaws.com',
        password = 'rafa170700',
        database ='landmaker',
        user = 'admin'
    )
    return conexao_banco

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'adminland'

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/enviarform', methods=['POST'])
def enviarform():
    nome = flask.request.form.get('nome')
    email = flask.request.form.get('email')
    contato = flask.request.form.get('contato')
    desc = flask.request.form.get('descricao')


    conexao = conexao_banco()
    cursor = conexao.cursor()

    comando = 'INSERT INTO orcamento (nome, email, contato, descricao) value(%s, %s, %s, %s)'
    valores = (nome, email, contato, desc)
    cursor.execute(comando, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
    return flask.redirect('/')
if __name__ in '__main__':app.run(debug=True)