from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date_completed = db.Column('Completed', db.String(7),)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    github_url = db.Column('Github Link', db.String())

    def __repr__(self):
        return f"""<Project (ID: {self.id}
        Title: {self.title}
        Date completed: {self.date_completed}
        Description: {self.description}
        skills: {self.skills}
        Github Link: {self.github_url}"""
