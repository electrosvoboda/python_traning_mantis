from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_css_selector("span.bracket").click()
        wd.find_element_by_xpath("/ html / body / table[3] / tbody / tr[1] / td / form / input[2]")

    def fill_project_form(self, project):
        self.changes_field("name", project.name)
        self.changes_field("description", project.description)

    def changes_field(self, project_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(project_name).click()
            wd.find_element_by_name(project_name).clear()
            wd.find_element_by_name(project_name).send_keys(text)

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        self.fill_project_form(project)
        wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[7]/td/input")