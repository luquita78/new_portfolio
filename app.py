from flask import Flask, render_template,redirect, request, flash
from flask_mail import Mail, Message
from config import email, senha

app = Flask(__name__)
app.secret_key = 'percut'

mail_settings = {
    "MAIL_SERVER":'smtp.gmail.com',
    "MAIL_port": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL":True,
    "MAIL_USERNAME":email,
    "MAIL_PASSWORD":senha

}

app.config.update(mail_settings)

mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome,
        self.email = email,
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods = ['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(request.form['nome'],['email'],['mensagem'])

        msg = Message(
            subject=f'{formContato.nome} enviou-lhe uma mensagem.',
            sender=app.config.get("MAIL_USERNAME"),
            recipients= ['lucasbarbosa.oliveira78@gmail.com', app.config.get("MAIL_USERNAME")],
            body = f'''
            
            {formContato.nome} com o e-mail {formContato.email} enviou-lhe a seguinte mensagem:

            {formContato.mensagem}

            '''
            
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')

if __name__ == '__main__':
        app.run(debug=True)