
#Author : JUAN MANUEL SUAREZ AGUIRRE
#Date : 4/04/2021
from PyQt5 import QtWidgets,QtCore,QtGui
import sys
from PyQt5.QtWidgets import *
from CONTROLLER import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.info = Crud()
        self.setWindowTitle("Hospital administration")
        self.resize(1000, 300)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.generalTabUI(), "add_Doc")
        tabs.addTab(self.networkTabUI(), "search_Doc")
        layout.addWidget(tabs)
    def generalTabUI(self):
        """Create the General page UI."""
        generalTab = QWidget()
        layout = QGridLayout()
        formLayout = QFormLayout()
        #id input
        label = QLabel("Id document")
        self.id = QLineEdit()
        layout.addWidget(label,0,0)
        layout.addWidget(self.id,0,1)

        label = QLabel("Name")
        self.name = QLineEdit()
        layout.addWidget(label,1,0)
        layout.addWidget(self.name,1,1)

        label = QLabel("speciality")
        self.phone = QLineEdit()
        layout.addWidget(label,2,0)
        layout.addWidget(self.phone,2,1)

        label = QLabel("Last name")
        self.Lname = QLineEdit()
        layout.addWidget(label,1,2)
        layout.addWidget(self.Lname,1,3)

        label = QLabel("Hospital")
        self.email = QLineEdit()
        layout.addWidget(label,2,2)
        layout.addWidget(self.email,2,3)
  
        # Add a button box
        btnBox = QPushButton("Add Doctor")
        btnBox.clicked.connect(self.inputscheckproducer)
        layout.addWidget(btnBox,4,4)
        
        self.setLayout(layout)
        generalTab.setLayout(layout)
        return generalTab
    def networkTabUI(self):
        networkTab = QWidget()
        layout = QGridLayout()
        formLayout = QFormLayout()

        label = QLabel("DNI")
        self.crop = QLineEdit()
        layout.addWidget(label,0,0)
        layout.addWidget(self.crop,0,1)
        
        # label = QLabel("Crop")
        # self.crop = QComboBox()
        # self.crop.addItems(['','Lemon','Orange'])
        # layout.addWidget(label,0,0)
        # layout.addWidget(self.crop,0,1)


        self.labelname = QLabel("")
        layout.addWidget(self.labelname,1,0)

        self.labelspec = QLabel()
        layout.addWidget(self.labelspec,2,0)
        
        self.labelhos = QLabel()
        layout.addWidget(self.labelhos,3,0)


        btnBox = QPushButton("Search")
        btnBox.clicked.connect(self.inputscheckfarm)
        layout.addWidget(btnBox,0,2)
        
        self.setLayout(layout)
        networkTab.setLayout(layout)
        return networkTab
    def inputscheckproducer(self):
        msg = QMessageBox()
        checker = [self.id.text().strip(),self.name.text().strip(),self.phone.text().strip(),self.Lname.text().strip(),self.email.text().strip()]
        if "" in checker:
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Critical)
            msg.setText('insert error')
            msg.exec_()
        else:
            self.info.createdoctor(checker[4],checker[0],checker[1]+" "+checker[3],checker[2])
            self.id.clear()
            self.name.clear()
            self.phone.clear()
            self.Lname.clear()
            self.email.clear()
            msg.setWindowTitle('Success')
            msg.setIcon(QMessageBox.Information)
            msg.setText('correct added')
            msg.exec_()
    def inputscheckfarm(self):
        msg = QMessageBox()
        doc_info = self.info.search_by_dni(self.crop.text().strip())
        if  '' == self.crop.text().strip():
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Critical)
            msg.setText('complete the box')
            msg.exec_()
        elif '' in doc_info:
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Critical)
            msg.setText('dni not found')
            msg.exec_()
        else:
            self.crop.clear()
            self.labelname.setText("NAME: " + doc_info[1][1])
            self.labelspec.setText("SPECIALITY: " + doc_info[1][2])
            self.labelhos.setText("HOSPITAL: " + doc_info[0])
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())