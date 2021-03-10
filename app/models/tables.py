from app import db

class User(db.Model):
    __tablename__ = "users"

    id  = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String,unique = True,nullable=False)
    senha = db.Column(db.String,nullable=False)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return '%r' %(self.nome)

class Meta(db.Model):
    __tablename__ = "metas"

    id = db.Column(db.Integer,primary_key = True)
    titulo = db.Column(db.String,nullable=False)
    descricao = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys = user_id)

    def __init__(self,titulo, descricao, user_id):
        self.titulo = titulo
        self.descricao = descricao
        self.user_id = user_id
    def __repr__(self):
        return '%r'%(self.titulo)