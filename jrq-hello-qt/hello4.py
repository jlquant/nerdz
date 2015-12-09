import sys, os
from PyQt4 import QtGui, QtCore, uic

DIRPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		uic.loadUi(os.path.join(DIRPATH, 'hello4.ui'), self)
		self.btnExit.clicked.connect(self.handleButton)

	def handleButton(self):
		print('Hello World')
		self.close()

if __name__ == '__main__':

	app = QtGui.QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())

