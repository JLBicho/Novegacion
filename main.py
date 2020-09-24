import sys

# settings contains global variables used across modules
import settings
# gui contains the MainWindow of the application
from gui import MainWindow
# QApplication is used to create the App
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainwindow = MainWindow()
	mainwindow.resize(1200, 900)
	mainwindow.show()
	sys.exit(app.exec_())

	