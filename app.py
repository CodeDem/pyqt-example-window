import sys
from PyQt4 import QtGui


import sys
from PyQt4 import QtGui


class GUI(QtGui.QWidget):

    def __init__(self):
        super(GUI, self).__init__()
        
        if sys.argv:
            self.data = sys.argv

        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        lbl1 = QtGui.QLabel('Argument passed', self)
        lbl1.move(100, 50)
        try:
            lbl2 = QtGui.QLabel(self.data[1], self)
        except:
            lbl2 = QtGui.QLabel('No Arguments passed', self)
        lbl2.move(100, 80)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('New Window')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
