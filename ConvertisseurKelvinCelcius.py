from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtCore import QCoreApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        self.resize(350, 150)
        widget.setLayout(grid)


        self.__label_A = QLabel("Temperature: ")
        self.__temperature_input = QLineEdit("")
        self.__temperature_input.setMaxLength(50)
        self.__messagebox = QMessageBox(text='Permet de convertir un nombre soit de Kelvin vers Celcius, soit de Celcius vers Kelvin')
        self.__help = QPushButton("?")
        self.__help.clicked.connect(self.__helpfunc)
        self.__temperature_input2 = QLineEdit("")
        self.__temperature_input2.setMaxLength(50)
        self.__temperature_input2.setDisabled(True)
        self.__label_B = QLabel("°C")
        self.__convertir = QPushButton("Convertir")
        self.__errormsg = QLabel('')
        self.__errormsg.setWordWrap(True)
        self.__conversiontype = QComboBox()
        self.__conversiontype.addItems(['°C > K', 'K > °C'])
        self.__conversiontype.activated[str].connect(self.__onChanged)
        self.__label_C = QLabel("Conversion")
        self.__label_D = QLabel("K")
        self.__convertir.clicked.connect(self.__convertCK)
        self.setWindowTitle("Conversion de temperature")


        grid.addWidget(self.__label_A, 0, 0)
        grid.addWidget(self.__temperature_input, 0, 1)
        grid.addWidget(self.__label_B, 0, 2)

        grid.addWidget(self.__errormsg, 1, 0, 1, 2)

        grid.addWidget(self.__convertir, 2, 1)
        grid.addWidget(self.__conversiontype, 2, 2)

        grid.addWidget(self.__label_C, 3, 0)
        grid.addWidget(self.__temperature_input2, 3, 1)
        grid.addWidget(self.__label_D, 3, 2)

        grid.addWidget(self.__help, 4, 2)


    def __convertKC(self):
        try:
            if float(self.__temperature_input2.text()) < 0:
                self.__temperature_input2.setText('0')
                return self.__errormsg.setText('La temperature en Kelvin ne peut pas etre inferieur a zero!')
            else:
                n = round(float(self.__temperature_input2.text()) - 273.15, 2)
                self.__temperature_input.setText(str(n))
                self.__errormsg.setText('')
        except:
            self.__temperature_input2.setText('')
            self.__errormsg.setText('inserez un nombre!')


    def __helpfunc(self):
        self.__messagebox.exec()
        self.__messagebox.setIcon(QMessageBox.Information)
        self.__messagebox.setWindowTitle('Aide')
        self.__messagebox.resize(500, 500)

    def __convertCK(self):
        try:
            if float(self.__temperature_input.text()) < -273.15:
                self.__temperature_input.setText('-273.15')
                return self.__errormsg.setText('La temperature en Celcius ne peut pas etre inferieur a -273.15°C!')
            else:
                n = round(float(self.__temperature_input.text()) + 273.15, 2)
                self.__temperature_input2.setText(str(n))
                self.__errormsg.setText('')
        except:
            self.__temperature_input.setText('')
            self.__errormsg.setText('inserez un nombre!')


    def __onChanged(self, text):
        if text == 'K > °C':
            try:
                self.__convertir.clicked.disconnect(self.__convertCK)
                self.__convertir.clicked.connect(self.__convertKC)
                self.__temperature_input.setDisabled(True)
                self.__temperature_input2.setDisabled(False)
                self.__label_C.setText('Temperature:')
                self.__label_A.setText('Conversion:')
            except:
                pass
        elif text == '°C > K':
            try:
                self.__convertir.clicked.disconnect(self.__convertKC)
                self.__convertir.clicked.connect(self.__convertCK)
                self.__temperature_input.setDisabled(False)
                self.__temperature_input2.setDisabled(True)
                self.__label_A.setText('Temperature:')
                self.__label_C.setText('Conversion:')
            except:
                pass


    def __actionQuitter(self):
        return QCoreApplication.exit(0)
