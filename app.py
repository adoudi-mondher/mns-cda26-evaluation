from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

from routes import * 

with app.app_context():
    from models import Event
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)