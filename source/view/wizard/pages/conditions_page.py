from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from source.store import help_button_text


class ConditionsPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.complete = False

        self.incomplete_message = "Equation or conditions must be filled"
        self.alert_text = help_button_text.conditions

        self.structural_invariants_group: ComboBoxesGroup
        self.spectral_invariants_group: ComboBoxesGroup

    def set_up_layout(self) -> None:
        """Set the layout of the conditions page,
        adding the two widgets with the conditions setting the spacing and the window title
        The attributes will be set is the:
            Title,
            layout with is the QHBoxLayout,
            set the spacing,
            add the two widgets it is the structural invariants group and the spectral invariants group
            and set the content margin
        """
        self.setTitle("Conditions")

        layout = QHBoxLayout()
        layout.setSpacing(5)
        layout.addWidget(self.structural_invariants_group)
        layout.addWidget(self.spectral_invariants_group)
        layout.setContentsMargins(30, 25, 30, 25)

        self.setLayout(layout)

    def isComplete(self) -> bool:
        """this method will verify the status of the 'complete' variable and return it
        Returns
        --------
        bool
            The status of the 'complete' variable
        """
        return self.complete


class ComboBoxesGroup(QGroupBox):
    def __init__(self, title, dictionary, update_conditions):
        super().__init__()

        self.title = title
        self.dictionary = dictionary
        self.update_conditions = update_conditions

        self.conditions_layout = QGridLayout()
        self.scroll_area = QScrollArea()

        self.button_group = QGroupBox()

        self.set_content_attributes()
        self.set_up_layout()
        self.fill_combos()

    def set_content_attributes(self) -> None:
        """ Set the content attributes of the Combo Boxes Group it will appear in the conditions page.
            The attributes are:
                The title,
                set the size policy it is QSizePolicy,
                set the minimumWidth at 250 pixels,
                set the attributes of the scroll area it is QScrollArea, the attributes are widgetResizable it is true
                and setFrameShape who defines the shape frame of the scroll area it is No frame,
                set the horizontal spacing of the conditions page, it is 20 pixels
                and set the set flat the button group it is an QGroupBox, that button will contain the tue and false states for the conditions
        """
        self.setTitle(self.title)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumWidth(250)

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)

        self.conditions_layout.setHorizontalSpacing(20)

        self.button_group.setFlat(True)

    def set_up_layout(self) -> None:
        """Set the layout of the combo box, placing the widgets.
            The content of the layout will be:
                The grid layout it is an QGridLayout,
                set the Column minimum width, who needs two parameters the first will be for what column been 0 for the first one,
                and the second parameter for the stretch of the column,
                add two widgets for the layout who will be one label with the true and align to center and other to false also with center alignment,
                set the button group with that layout in grid,
                add to the conditions layout the button group as a widget
        """
        grid_layout_aux = QGridLayout()
        grid_layout_aux.setColumnMinimumWidth(0, 200)
        grid_layout_aux.addWidget(QLabel("true"), 0, 1, Qt.AlignCenter)
        grid_layout_aux.addWidget(QLabel("false"), 0, 2, Qt.AlignCenter)
        self.button_group.setLayout(grid_layout_aux)
        self.conditions_layout.addWidget(self.button_group, 0, 0)

    def fill_combos(self) -> None:
        """Fill the combos with the conditions in the combo box, and setting some layout for the combos
            First this method will get in the dictionary with a 'for' all the conditions.
            In it loop of the 'for' getting the condition with their key,
            set the button_group with the nome of the object who is received by the dictionary,
            create a grid auxiliary layout, set the minimum width and create add a label to the layout with the dictionary object,
            create the true and false buttons passing the method passing the update_conditions parameter,
            add to the layout the buttons aligning them to center set the layout and putt that in the conditions' layout.
            After the loop will create and set the widget layout with the condition's layout,
            set the scroll_area with the widget layout, and will put the widget layout as a widget in the vertical_layout_grid who will be showned
        """
        for i, key in enumerate(self.dictionary):
            button_group = QGroupBox()
            button_group.setFlat(True)
            button_group.setObjectName(f"{key}")

            grid_layout_aux = QGridLayout()
            grid_layout_aux.addWidget(QLabel(f"{key}"), i + 1, 0)
            grid_layout_aux.setColumnMinimumWidth(0, 200)

            true = QRadioButton()
            true.clicked.connect(self.update_conditions)
            true.setObjectName("true")

            false = QRadioButton()
            false.clicked.connect(self.update_conditions)
            false.setObjectName("false")

            grid_layout_aux.addWidget(true, i + 1, 1, Qt.AlignCenter)
            grid_layout_aux.addWidget(false, i + 1, 2, Qt.AlignCenter)
            button_group.setLayout(grid_layout_aux)
            self.conditions_layout.addWidget(button_group, i + 1, 0)

        vertical_layout_aux = QVBoxLayout()
        widget_aux = QWidget()
        widget_aux.setLayout(self.conditions_layout)
        self.scroll_area.setWidget(widget_aux)
        vertical_layout_aux.addWidget(self.scroll_area)
        self.setLayout(vertical_layout_aux)
