from deprecated.view.windows.welcome_window import WelcomeWindow

from deprecated.controller.wizard_controller import WizardController


class WelcomeController:

    def __init__(self):
        self.welcome_window = WelcomeWindow()
        self.wizard_controller = WizardController()

    def show_window(self):
        self.welcome_window.show()

    def close_window(self):
        self.welcome_window.close()
