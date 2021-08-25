from logging import error
from flask import render_template, request, url_for, redirect
from models import Project, app, db

def get_projects():
    return Project.query.all()

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/project/new', methods=['GET', 'POST'])
def create():
    if request.form:
        new_project = Project(
            title = request.form['title'],
            date_completed = request.form['date'],
            description = request.form['desc'],
            skills = request.form['skills'],
            github_url = request.form['github']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects = get_projects())

@app.route('/project/<id>')
def detail(id):
    project = Project.query.get(id)
    return render_template('detail.html', project=project, projects=get_projects())

@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get(id)
    if request.form:
        project.title = request.form['title']
        project.date_completed = request.form['date']
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.github_url = request.form['github']
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editform.html', project=project, projects=get_projects())

@app.route('/project/<id>/delete')
def delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html', projects=get_projects())

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', msg=error, projects=get_projects()), 404 


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')