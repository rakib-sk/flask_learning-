from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import db, User   # models কে import করা যাবে কারণ db এখন ওখানেই defined

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        db.create_all()   # প্রথমবার DB তৈরি

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)