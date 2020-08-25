from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    project = Project(name="joe", description="bowie")
    app.project.create_project(project)