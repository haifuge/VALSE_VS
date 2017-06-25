import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Common import CommonMethod
from Common import CommonTools

class VectorTrail(QWidget):
    max_x=300.0
    max_y=300.0
    width=400.0
    height=400.0
    proportion_scale_x=1.0
    proportion_scale_y=1.0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(self.width, self.height)
        self.map=QPixmap('Maps/testMap.png')
        self.lmap=Map(self)
        self.lmap.setImage('Maps/testMap.png');
        self.lmap.setScaledContents(True)
        self.lmap.resize(self.width,self.height)
        self.lmap.move(0,0)
        #self.initTimer()

    def SetMap(self,  maxx, maxy, map_path):
        self.max_x=maxx
        self.max_y=maxy
        self.proportion_scale_x=self.max_x/self.width
        self.proportion_scale_y=self.max_y/self.height
        self.map=QPixmap(map_path)
        
        self.lmap.setPixmap(map);
        self.lmap.setScaledContents(True)
        self.lmap.resize(self.width,self.height)
        self.lmap.move(0,0)
        
    def resizeEvent(self, e):
        self.lmap.resize(self.size())

    def initTimer(self):
        self.timer=QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.click)
        self.i=1
        self.n=10
        self.step=30
        self.setFixedSize(self.size())
        self.timer.start()

    def click(self):
        self.repaint()
        self.i=self.i+1
        if self.i==self.n:
            self.timer.stop()
            self.setFixedSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX)


class Map(QLabel):
  
    def __init__(self, parent=None):
        super().__init__(parent);

    def setImage(self, path):
        self.img=QPixmap(path)

    def setData(self, arr):
        self.positions=arr;

    def paintEvent(self, e):
        qp=QPainter()
        qp.begin(self)
        #CommonMethod.DrawMarker(self.i*self.step, self.i*self.step, qp, CommonTools.Shape.cross, CommonTools.Color.red, 15)
        #qp.setPen(QPen(QColor.black))
        qp.drawPixmap(0,0,self.img)
        qp.drawRect(10,10,10,10)
        qp.end()
    
    def resizeEvent(self, e):
        self.img=self.img.scaled(self.size(),Qt.IgnoreAspectRatio, Qt.FastTransformation)

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=VectorTrail()
    ex.show()
    sys.exit(app.exec_())