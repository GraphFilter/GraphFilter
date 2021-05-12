from src.view.welcome.welcome_window import WelcomeWindow
from src.view.welcome.welcome_content import WelcomeContent
from src.controller.wizard_controller import WizardController


class WelcomeController:

    def __init__(self):
        self.welcome_window = WelcomeWindow()
        self.welcome_content = WelcomeContent()
        self.wizard_controller = WizardController()

        self.welcome_window.setCentralWidget(self.welcome_content)

    def show_window(self):
        self.welcome_window.show()

    def close_window(self):
        self.welcome_window.close()
