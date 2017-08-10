import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Common import CommonMethod
from Common import CommonTools

class Marker(QWidget):
    def __init__(self, _color, _shape, _x, _y, _size=16, parent=None):
        super().__init__(parent)
        self.color=_color
        self.shape=_shape
        self.x=_x
        self.y=_y
        self.size=_size

        QToolTip.setFont(QFont('SansSerif',10))
        toolTip=str(self.x)+', '+str(self.y)
        self.setToolTip(toolTip)

        self.setMinimumSize(self.size,self.size)
        #self.move(300,300)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent")


    def paintEvent(self, e):
        qp=QPainter()
        qp.begin(self)
        CommonMethod.DrawMarker(self.x,self.y,qp,self.shape,self.color,self.size)
        qp.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Marker(CommonTools.Color.red, CommonTools.Shape.square, 10,10)
    ex.show()
    sys.exit(app.exec_())
