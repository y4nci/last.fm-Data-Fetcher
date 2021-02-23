import sys
from datafetcher import fetch
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPalette, QBrush


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("last.fm Stats Viewer")
        self.setGeometry(100, 100, 800, 450)
        background = QImage("loveless.jpg")  # A classic album. Would definitely recommend
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)
        self.text1 = QtWidgets.QLabel("")
        self.text2 = QtWidgets.QLabel("")
        self.username = QtWidgets.QLineEdit()
        self.username_text = QtWidgets.QLabel("username ")
        self.datatype = QtWidgets.QComboBox()
        self.datatype.addItems(["", "albums", "artists", "tracks"])
        self.datatype_text = QtWidgets.QLabel("data type ")
        self.timerange = QtWidgets.QComboBox()
        self.timerange.addItems(["", "last week", "last month", "last 3 months", "last 6 months", "last year", "all time"])
        self.timerange_text = QtWidgets.QLabel("time interval ")
        self.check = QtWidgets.QCheckBox()
        self.check_text = QtWidgets.QLabel("include scrobbles ")
        self.button = QtWidgets.QPushButton("get your data")
        vertical_left = QtWidgets.QVBoxLayout()
        vertical_left.addWidget(self.username_text)
        vertical_left.addWidget(self.datatype_text)
        vertical_left.addWidget(self.timerange_text)
        vertical_left.addWidget(self.check_text)

        vertical_right = QtWidgets.QVBoxLayout()
        vertical_right.addWidget(self.username)
        vertical_right.addWidget(self.datatype)
        vertical_right.addWidget(self.timerange)
        vertical_right.addWidget(self.check)

        horizontal_top = QtWidgets.QHBoxLayout()
        horizontal_top.addStretch()
        horizontal_top.addLayout(vertical_left)
        horizontal_top.addLayout(vertical_right)
        horizontal_top.addStretch()

        input_layout = QtWidgets.QVBoxLayout()
        input_layout.addStretch()
        input_layout.addLayout(horizontal_top)
        input_layout.addWidget(self.button)
        input_layout.addStretch()

        final_layout = QtWidgets.QHBoxLayout()
        final_layout.addStretch()
        final_layout.addWidget(self.text1)
        final_layout.addLayout(input_layout)
        final_layout.addWidget(self.text2)
        final_layout.addStretch()

        self.setLayout(final_layout)

        self.button.clicked.connect(self.click)

        self.show()

    def click(self):

        # This isn't the normal way to do this, but this was my first attempt to create a GUI program using PyQt5 and I
        # avoided using QMainWindow intentionally.

        self.username.deleteLater()
        self.username_text.deleteLater()
        self.datatype.deleteLater()
        self.datatype_text.deleteLater()
        self.timerange.deleteLater()
        self.timerange_text.deleteLater()
        self.button.deleteLater()
        self.check.deleteLater()
        self.check_text.deleteLater()
        left = fetch(1, self.datatype.currentText(), self.username.text(), self.timerange.currentText(), self.check.isChecked())
        right = fetch(2, self.datatype.currentText(), self.username.text(), self.timerange.currentText(), self.check.isChecked())

        if left == "!!!": self.text1.deleteLater()  # An error message fetch() generates.
        else: self.text1.setText(left)

        self.text2.setText(right)


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
