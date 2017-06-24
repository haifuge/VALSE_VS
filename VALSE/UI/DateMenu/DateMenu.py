import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI.DateMenu import DateSelector
from UI.DateMenu import CustomFrequencyPanel

class DateMenu(QWidget):
    closeSignal=pyqtSignal()
    startDate=''
    endDate=''
    frequency=[]
    location=''
    """description of class"""
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,300)
        self.setMinimumSize(250, 300)
        # textEdit position
        txtY=15;
        txtX=90;
        # textEdit size
        txtWidth=120
        txtHeight=27
        # row height
        yInterval=30

        lblName=QLabel(self);
        lblName.setText('Name:')
        lblName.adjustSize()
        lblName.move(20,txtY)
        self.btnName=QPushButton(self)
        self.btnName.setText('New_Window_1')
        self.btnName.resize(txtWidth,txtHeight)
        self.btnName.move(txtX,txtY)

        txtY=txtY+yInterval;
        lblDateStart=QLabel(self)
        lblDateStart.setText('Date Start:')
        lblDateStart.adjustSize()
        lblDateStart.move(20,txtY)
        self.btnDateStart=QPushButton(self)
        self.btnDateStart.setText('MM/DD/YY')
        self.btnDateStart.resize(txtWidth,txtHeight)
        self.btnDateStart.move(txtX,txtY)

        txtY=txtY+yInterval;
        lblDateEnd=QLabel(self)
        lblDateEnd.setText('Date End:')
        lblDateEnd.adjustSize()
        lblDateEnd.move(20,txtY)
        self.btnDateEnd=QPushButton(self)
        self.btnDateEnd.setText('MM/DD/YY')
        self.btnDateEnd.move(txtX,txtY)
        self.btnDateEnd.resize(txtWidth,txtHeight)

        txtY=txtY+yInterval+5;
        lblFrequency=QLabel(self)
        lblFrequency.setText('Frequency:')
        lblFrequency.adjustSize()
        lblFrequency.move(20,txtY)
        self.btnWeekly=QPushButton(self)
        self.btnWeekly.setText('Weekly')
        self.btnWeekly.setCheckable(True)
        self.btnWeekly.move(txtX,txtY)
        self.btnWeekly.resize(txtWidth,txtHeight)

        txtY=txtY+yInterval-4;
        self.btnMonthly=QPushButton(self)
        self.btnMonthly.setText('Monthly')
        self.btnMonthly.setCheckable(True)
        self.btnMonthly.move(txtX,txtY)
        self.btnMonthly.resize(txtWidth,txtHeight)

        txtY=txtY+yInterval-4;
        self.btnYearly=QPushButton(self)
        self.btnYearly.setText('Yearly')
        self.btnYearly.setCheckable(True)
        self.btnYearly.move(txtX,txtY)
        self.btnYearly.resize(txtWidth,txtHeight)

        txtY=txtY+yInterval-4;
        self.btnCustom=QPushButton(self)
        self.btnCustom.setText('Custom...')
        self.btnCustom.setCheckable(True)
        self.btnCustom.move(txtX,txtY)
        self.btnCustom.resize(txtWidth,txtHeight)

        # location
        txtY=txtY+yInterval+5;
        lblLocation=QLabel(self)
        lblLocation.setText('Location:')
        lblLocation.adjustSize()
        lblLocation.move(20,txtY)
        self.btnLocation=QComboBox(self)
        self.btnLocation.addItems(['Location1','Location2','Location3'])
        self.location='Location1'
        self.btnLocation.move(txtX,txtY)
        self.btnLocation.resize(txtWidth,txtHeight)
        self.btnLocation.currentTextChanged.connect(self.setLocation)

        txtY=txtY+yInterval+5;
        self.btnCancel=QPushButton(self)
        self.btnCancel.setText('Cancel')
        self.btnCancel.resize(QSize(70,30))
        self.btnCancel.move(35,txtY)
        self.btnCancel.clicked.connect(self.btnDecClicked)
        self.btnConfirm=QPushButton(self)
        self.btnConfirm.setText('Confirm')
        self.btnConfirm.resize(QSize(70,30))
        self.btnConfirm.clicked.connect(self.btnDecClicked)
        self.btnConfirm.move(150,txtY)

        #  btn date click
        self.btnDateStart.clicked.connect(self.btnDateClicked)
        self.btnDateEnd.clicked.connect(self.btnDateClicked)
        self.ds=DateSelector.DateSelector(self)
        self.ds.signal[str].connect(self.setbtnText)
        self.ds.setWindowFlags(Qt.FramelessWindowHint)
        
        # btn frequency click
        self.btnWeekly.clicked.connect(self.frequencyClicked)
        self.btnMonthly.clicked.connect(self.frequencyClicked)
        self.btnYearly.clicked.connect(self.frequencyClicked)
        self.btnCustom.clicked.connect(self.frequencyClicked)

    def setLocation(self):
        self.location=self.btnLocation.currentText()
    def btnDecClicked(self):
        s=self.sender()
        if s==self.btnCancel:
            self.close()
            self.closeSignal.emit()
        if s==self.btnConfirm:
            self.close()
            print(self.startDate, self.endDate, self.frequency, self.location, sep=', ')
            self.closeSignal.emit()

    def initLocation():


    def frequencyClicked(self):
        self.freqSender=self.sender();
        if self.freqSender==self.btnWeekly:
            self.btnWeekly.setChecked(True)
            self.btnMonthly.setChecked(False)
            self.btnYearly.setChecked(False)
            self.btnCustom.setChecked(False)
            self.frequency=[1,1,1,1,1,1,1]
        if self.freqSender==self.btnMonthly:
            self.btnWeekly.setChecked(False)
            self.btnMonthly.setChecked(True)
            self.btnYearly.setChecked(False)
            self.btnCustom.setChecked(False)
            self.frequency=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        if self.freqSender==self.btnYearly:
            self.btnWeekly.setChecked(False)
            self.btnMonthly.setChecked(False)
            self.btnYearly.setChecked(True)
            self.btnCustom.setChecked(False)
            self.frequency=[1,1,1,1,1,1,1,1,1,1,1,1]
        if self.freqSender==self.btnCustom:
            self.btnWeekly.setChecked(False)
            self.btnMonthly.setChecked(False)
            self.btnYearly.setChecked(False)
            self.btnCustom.setChecked(True)
            self.cp=CustomFrequencyPanel.CustomFrequencyPanel(self)
            self.cp.setWindowFlags(Qt.FramelessWindowHint)
            point=self.btnCustom.rect().topRight()
            global_point=self.btnCustom.mapToGlobal(point)
            self.cp.setPosition(global_point.x(),global_point.y())
            self.cp.signal.connect(self.emitFrequency)
            self.cp.exec_()
        #frequency=self.freqSender.text()
    def emitFrequency(self, arr):
        self.frequency=arr
    def btnDateClicked(self):
        self.btnSender=self.sender()
        point=self.btnSender.rect().topRight()
        global_point=self.btnSender.mapToGlobal(point)
        self.ds.setPosition(global_point.x(), global_point.y())
        self.ds.exec_()
    def setbtnText(self, s):
        self.btnSender.setText(s)
        if self.btnSender==self.btnDateStart:
            self.startDate=s
        if self.btnSender==self.btnDateEnd:
            self.endDate=s


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=DateMenu()
    #ex=YearlySelectionPanel()
    ex.show();
    sys.exit(app.exec_())

