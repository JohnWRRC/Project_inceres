from flask import render_template,flash,redirect,url_for
from flask_login import login_user,logout_user
from app import app, db, lm # o db pra sessao

from app.models.forms import LoginForm
from app.models.tables import User

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()
    #return User.query.filter_by(alternative_id=id).first()
	
@app.route("/index1")
@app.route("/") # decorator da rota 
def index(): # passar o user como patametro
	# so encontrou pq por deaful procua na pasta templates
    return render_template('index.html') # enviando as variaveis

@app.route('/login', methods=["GET","POST"])
def login():
	form=LoginForm()
	if form.validate_on_submit:
		user=User.query.filter_by(username=form.username.data).first()
		print (user)
		if user and user.password == form.password.data:
			login_user(user)
			flash("Logged in")
			return redirect(url_for("index"))
		else:
			flash("Invalid Login")
		
	
			
	return render_template('login.html',
						   form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for('index'))
						   














#@app.route("/teste/<info>")
#@app.route("/teste", defaults={'info':None})
#def teste(info):
	# i=User("Joao","1234","Joao","jw.ribeiro.rc@gmail.com") # instacia da classe tabela ADD  dados na tabela
	#db.session.add(i)# periodo de uttilizacao, passando a instacia i
	#db.session.commit() # salvando no banco de dados
	#r=User.query.filter_by(username="John").first() # posso usar . all() e outros
#	print (r)
#	print (r.username, r.name)
#	return "OK"
	


#@app.route('/test/',defaults={'name':None})
#@app.route('/test/<name>')
##@app.route('/test/<int:id>') # caso eu queira receber algum numero inteiro converto no flask
##@app.route('/test/',methods=['GET'])
#def test(name):
    #if name:        
        #return 'ola %s'%name
    #else:
        #return 'Ola pessoal'