from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = 'Pantera'

app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Savioli2230@localhost/jogosbrunno'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

from views import *

if __name__=='__main__':
    app.run(debug=True)