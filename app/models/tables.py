from app import db
"""
AS tabelas sao declaradas em formato de classes

"""
class User(db.Model):
    __tablename__="users" # parametro especial. Nome da tabela no banco de dados
    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String,unique=True) 
    password=db.Column(db.String)
    name=db.Column(db.String)
    email=db.Column(db.String)
    
    #metodo contrutor
    @property
    def is_authenticated(self):
	
        return True
    @property
    def is_active(self):
        return True    
    @property
    def is_anonymous(self):
        return True    
    
    def get_id(self):
        return str(self.id)   

   
    def __init__(self, username,password,name,email):
        self.username=username
        self.password=password
        self.name=name
        self.email=email
        
    # fucao especial para representacao
    def __repr__(self):
        """
        Essa fucao retorna os registros
        """
        return "<User %s>"% self.username
    
    
		
    

class Post(db.Model):
    __tablename__="posts"
    id= db.Column(db.Integer, primary_key=True)
    contents=db.Column(db.Text)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id')) # campo especial, carrega a chave estrangeira
    # relationship, tras todas as informacoes do usuario feito na pesquisa
    user=db.relationship('User',foreign_keys=user_id) # relacionando com a classe User
    
    def __init__(self,contents,user_id):
        self.contents=-contents
        self.user_id=user_id
    
    #representacao
    def __repr__(self):
        return "< Post %s>"%self.id
    
        
class Follow(db.Model):
    __tablename__="follow"
    id= db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    follower_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    
    user=db.relationship('User', foreign_keys=user_id)
    follower=db.relationship('User',foreign_keys=follower_id)
    
    
    
    