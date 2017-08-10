import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI.Sidebar import PeopleItem

class PeopleSidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.pItems=[PeopleItem.PeopleItem()]*4
        self.initUI()
    def initUI(self):
        self.setWindowTitle('People')
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.setMaximumWidth(250)
        #self.setStyleSheet('border: 1px solid black;')

        self.setGeometry(100,100,250,200)
        self.vlayout=QVBoxLayout()
        self.vlayout.setContentsMargins(QMargins(0,0,0,0))
        self.vlayout.setSpacing(0)
        for item in self.pItems:
            item=PeopleItem.PeopleItem()
            item.setGeometry(0,0,250,25)
            self.vlayout.addWidget(item)
            line=QFrame()
            line.setContentsMargins(QMargins(0,0,0,0))

            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            self.vlayout.addWidget(line)
        self.vlayout.addStretch(1)
        self.setLayout(self.vlayout)

    def paintEvent(self, e):
        qp=QPainter()
        qp.begin(self)
        pen=QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(1,1,self.size().width()-2,self.size().height()-2)
        qp.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=PeopleSidebar()
    ex.show()
    sys.exit(app.exec_())