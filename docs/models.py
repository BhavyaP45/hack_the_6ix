from docs import app, db, UserMixin, bcrypt, loginmanager

@loginmanager.user_loader #Required property for the users to be authenticated
def load_user(user_id):
    return User.query.get(user_id)

#Create class user with Database Model, create various columns
class User(db.Model, UserMixin): #Use UserMixin class to add prexisting methods
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 45), nullable = False, unique = True)
    email_address = db.Column(db.String(), unique = True, nullable = False)
    password_hash = db.Column(db.String(), nullable = False)
    is_manager = db.Column(db.Boolean())
    company = db.Column(db.String(length = 45), nullable = False)
    tasks = db.relationship('Task', backref = "assigned_tasks", lazy = True)
    
    #Create a password property
    @property
    def password(self):
      return self.password
    
    @password.setter #Used to set the property of password into a hashed one using bcrypt class
    def password(self, plain_text_password):
      self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    #Create a method that returns a boolean by checking an attempted password with the stored hash
    def check_password_correction(self, attempted_password):
      return bcrypt.check_password_hash(self.password_hash, attempted_password) #checks the hash password with the attempted one
    
class Task(db.Model):
   id = db.Column(db.Integer(), primary_key = True)
   title =  db.Column(db.String(length = 45), nullable = False)
   assigned_to = db.Column(db.Integer(), db.ForeignKey("user.id")) 
   task_type = db.Column(db.String(length = 45), nullable = False)
   subtask1 = db.Column(db.String(length = 100))
   subtask2 = db.Column(db.String(length = 100))
  
