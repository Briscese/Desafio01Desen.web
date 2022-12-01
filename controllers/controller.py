from flask.views import MethodView
from flask import request, render_template,redirect
from db import mysql


class IndexController(MethodView):
    def get(self):            
        return render_template('index.html')

class LinkQuemSomosController(MethodView):
    def get(self):            
        return render_template('pagina2.html')

class LinkContatoController(MethodView):
    def get(self):    
        with mysql.cursor() as cur:        
            mensagem = ''
            cur.execute('SELECT * from contato')
            contato= cur.fetchall()
            return render_template('pagina3.html', mensagem=mensagem,contato=contato)

class EnvioController(MethodView):
    def post(self):
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        with mysql.cursor() as cur:
            cur.execute('INSERT INTO contato (EMAIL,ASSUNTO,MENSAGEM) VALUES (%s,%s,%s)',(email,assunto,mensagem))
            cur.connection.commit()
            cur.execute('SELECT * from contato')
            contato=cur.fetchall()
            mensagem = 'Mensagem enviada com sucesso !!!'


        return render_template('pagina3.html',mensagem=mensagem,contato=contato)