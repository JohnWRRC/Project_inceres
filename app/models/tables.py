from app import db
"""
AS tabelas sao declaradas em formato de classes

"""
class User(db.Model):
    __tablename__="users" # parametro especial. Nome da tabela no banco de dados
    id= db.Coluum(db.Integer, prymary_key=True)
    username=db.Colunm(db.String,unique=True) 
    password=db.Colunm(db.String)
    name=db.Colunm(db.String)
    email=db.Colunm(db.String)
    
    #metodo contrutor
    def __init__(self, user,password,name,email):
        self.username=username
        self.password=password
        self.name=name
        self.email=email
        
    # fucao especial para representacao
    def __repr__(self):
        """
        Essa fucao retorna os registros
        """
        return "<User %>"% self.username


class Post(db.Model):
    __tablename__="posts"
    id= db.Coluum(db.Integer, prymary_key=True)
    contents=db.Coluum(db.Text)
    
    user_id=db.Colunm(db.Integer,db.Foreingkey('users.id')) # campo especial, carrega a chave estrangeira
    
    # relationship, tras todas as informacoes do usuario feito na pesquisa
    user=db.relationship('User',foreing_keys=user_id) # relacionando com a classe User
    
    def __init__(self,contents,user_id):
        self.contents=-contents
        self.user_id=user_id
    
    #representacao
    def __repr__(self):
        return "< Post %>"%self.id
    
        
class Follow(db.Model):
    __tablename__="follow"
    id= db.Coluum(db.Integer, prymary_key=True)
    user_id=db.Colunm(db.Integer,db.Foreingkey('users.id'))
    follower_id=db.Colunm(db.Integer,db.Foreingkey('users.id'))
    
    user=relationship('User', foreing_keys=user_id)
    follower=relationship('User',foreing_keys=follower_id)
    
    
    
    