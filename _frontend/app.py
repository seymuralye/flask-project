from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask (__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345_Ulkar@localhost:3306/my_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    from controllers import *

return app

from controllers import *
from models import *
db.create_all()

# from extensions import *






if __name__ == '__main__':
    app.run(debug=True)