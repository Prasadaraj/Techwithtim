from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #chatgpt3    

# Initialise the database

db=SQLAlchemy(app)

#Create db model
#class Friends(db.Model):
#    id = db.Column (db.Integer, primary_key=True)   
#name = db.Column(db.String(200), nullable=False)
#date_created = db.Column(db.DateTime, default=datetime.utcnow)
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)    

def __repr__(self):
    return '<Name %r>' % self.id

@app.route('/')
def index():
    title="Prasada Blog"
    return render_template("index.html", title=title)


@app.route('/friends', methods=['POST', 'GET'])
def friends():
    title = "My Friend List"
    #return render_template("friends.html", title=title) 
    if request.method =='POST':   #it takes the name from the form and place in the variable ‘friend_name’
        #return "You clicked the button"     
        friend_name = request.form ['name']
        new_friend = Friends(name=friend_name)     #add this name to the column in our database Friends
# Push to database using try and except function
        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect('/friends')
        except:
            return "There was an error adding your friend"
        else:
            friends = Friends.query.order_by(Friends.date_created)
        return render_template('friends.html', title= title, friends=friends)

if __name__=="__main__":
	app.run(debug=True)           
