from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('page.html', usuario='usuário')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cad.html')

@app.route('/inicio', methods=['POST',])
def inicio():
    nome = request.form['pnome']
    return render_template('page.html', usuario=nome, ident='Seja Bem-Vinde, '+ nome)

@app.route('/deslogado')
def deslogado():
    return redirect('/')
app.run(debug=True)