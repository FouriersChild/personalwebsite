from flask import Flask

template_folder = "templates"
app = Flask(__name__, template_folder=template_folder)
app.config['SECRET_KEY'] = 'password12345abcde'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'