from source.view.windows.progress_window import ProgressWindow
from source.view.windows.project_window import ProjectWindow
from source.view.windows.welcome_window import WelcomeWindow
from source.view.windows.wizard_window import WizardWindow


class Controller:
    def __init__(self):
        self.welcome_window = WelcomeWindow()
        self.wizard_window = WizardWindow()
        self.project_window = ProjectWindow()
        self.progress_window = ProgressWindow()
        self.first_time = True
        self.list_graphs = []
        self.connect_events()

    def start(self):
        self.welcome_window.show()

    def connect_events(self):
        self.welcome_window.new_project.clicked.connect(self.show_wizard_window)
        self.wizard_window.cancel_button.clicked.connect(self.close_wizard_window)
        self.wizard_window.close_signal.connect(self.close_wizard_window)
        self.wizard_window.start_button.clicked.connect(self.start_filter)
        self.progress_window.canceled.connect(self.wizard_window.show)
        self.progress_window.finish.connect(self.finish_filter)

    def close_wizard_window(self):
        self.wizard_window.close()
        self.wizard_window = WizardWindow()
        self.welcome_window.show()

    def show_wizard_window(self):
        self.welcome_window.close()
        self.wizard_window.show()

    def start_filter(self):
        self.progress_window.show()
        method = self.wizard_window.field("method")
        method.set_attributes(self.wizard_window.field("equation"),
                              self.wizard_window.field("conditions"),
                              self.wizard_window.field("location"),
                              self.wizard_window.field("name"))
        method.process(self.wizard_window.field("files"), self.progress_window)

    def finish_filter(self):
        self.project_window.show()

    def show_project_window(self):
        self.project_window.showMaximized()
