from flask import Flask
app = Flask(__name__) # instancia que contem tudo do flask

@app.route("/") # decorator da rota 
def index():
    return("helo word")

if __name__=="__main__":
    app.run()