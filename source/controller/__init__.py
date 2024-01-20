from source.view.windows.welcome_window import WelcomeWindow
from source.view.windows.wizard_window import WizardWindow


class Controller:
    def __init__(self):
        self.welcome_window = WelcomeWindow()
        self.wizard_window = WizardWindow()

        self.connect_events()

    def start(self):
        self.welcome_window.show()

    def connect_events(self):
        self.welcome_window.new_project.clicked.connect(self.show_wizard_window)

        self.wizard_window.cancel_button.clicked.connect(self.close_wizard_window)
        self.wizard_window.close_signal.connect(self.close_wizard_window)

    def close_wizard_window(self):
        self.wizard_window.close()
        self.wizard_window = WizardWindow()
        self.connect_events()
        self.welcome_window.show()

    def show_wizard_window(self):
        self.welcome_window.close()
        self.wizard_window.show()
