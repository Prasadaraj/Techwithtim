from flask import Flask, render_template, flash 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm 
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
#pip install Flask-WTF
#create file using touch hello.py

app = Flask(__name__)
#add database and path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#server to run flask properly
# set FLASK_APP=hello.py
# set FLASK_ENV=development
# set FLASK_DEBUG=1 to automatically load after any changes
#flask run
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#secret key!
app.config['SECRET_KEY'] = "my super secretFalse that no one"  
#app.app_context().push()
#Initialize the Database
db= SQLAlchemy(app)
#go to shell: from hello import db
#db.create_all()
#exit() to exit shell

#create a model
#class Users(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#name = db.Column(db.String(200), nullable=False)
#email = db.Column(db.String(120), nullable=False, unique=True)
#date_added = db.Column(db.DateTime, default=datetime.utcnow) 

#create a string
#def __repr__(self):
#    return f'<User {self.name}, Email: {self.email}>'

#with app.app_context():
#    db.create_all()
    
#Create form class
#class UserForm(FlaskForm):
#    name= StringField("Whats your name")
#    submit=SubmitField("Submit")
    
#class UserForm(FlaskForm):
#    Name= StringField("Name", validators=[DataRequired()])
#    Email= StringField("Email", validators=[DataRequired()])
#    submit=SubmitField("Submit")
        
#@app.route('/user/add', methods=['GET','POST'])
#def add_user():
#    name=None
#    return render_template("add_user.html", form=form)
# custom error pages

#invalid pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Invalid Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500 

 
#@app.route('/<name>')
def user(name):
    return render_template("user.html", user_name=name)

@app.route('/')
def indexx():
    first_name="Morris"
    stuff= "This is Bold"
    favorite_pizza=["Pepperoni","Cheese","Anchovies", 41]
    
    
    return render_template("indexx.html", first_name=first_name, stuff=stuff,favorite_pizza=favorite_pizza)
    
#    favorite_pizza

#def index():
#    #title="Prasada Blog"
#    return '<h1> Hello World ! </h1>'

#@app.route('/user/<name>')
#def user(name):
#    return '<h1> Hello {}! </h1>'.format(name)
 
if __name__ == "__main__":
   app.run(debug=False)