import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QHBoxLayout
)

moves = [
    "rock",
    "paper",
    "scissors",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget() # creating another widget inside a window?
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setWindowTitle("Rock paper scissors")

        title = QLabel("Choose a move...")
        layout.addWidget(title)

        for move in moves:
            widget = QPushButton()
            widget.setIcon(QIcon(move + ".png"))
            widget.setIconSize(QSize(80, 80))
            widget.setFixedSize(100, 100)
            layout.addWidget(widget)

            

        # Set the central widget of the Window.
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()