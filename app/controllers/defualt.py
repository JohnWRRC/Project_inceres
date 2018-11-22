from flask import render_template
from app import app


from app.models.forms import LoginForm

@app.route("/index1")
@app.route("/") # decorator da rota 
def index(): # paasar o user como patametro
	# so encontrou pq por deaful procua na pasta templates
    return render_template('index.html') # enviando as variaveis

@app.route('/login', methods=["POST","GET"])
def login():
	form=LoginForm()
	if form.validate_on_submit:
		print(form.username.data)
		print(form.password.data)
	else:
		print (form.errors)
	return render_template('login.html',
						   form=form)
	

















#@app.route('/test/',defaults={'name':None})
#@app.route('/test/<name>')
##@app.route('/test/<int:id>') # caso eu queira receber algum numero inteiro converto no flask
##@app.route('/test/',methods=['GET'])
#def test(name):
    #if name:        
        #return 'ola %s'%name
    #else:
        #return 'Ola pessoal'