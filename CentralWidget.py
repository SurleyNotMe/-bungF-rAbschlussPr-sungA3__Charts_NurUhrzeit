from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QCheckBox, QGridLayout, QPushButton, QLineEdit, QRadioButton, QButtonGroup, \
    QGroupBox, QVBoxLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__radioButton_dhl = QRadioButton("DHL", self)
        self.__radioButton_ups = QRadioButton("UPS", self)
        self.__radioButton_pickup = QRadioButton("Selbstabholung", self)

        self.__buttonGroup_delivery = QButtonGroup(self)
        self.__buttonGroup_delivery.addButton(self.__radioButton_dhl)
        self.__buttonGroup_delivery.addButton(self.__radioButton_ups)
        self.__buttonGroup_delivery.addButton(self.__radioButton_pickup)

        vBoxLayout_delivery = QVBoxLayout()
        vBoxLayout_delivery.addWidget(self.__radioButton_dhl)
        vBoxLayout_delivery.addWidget(self.__radioButton_ups)
        vBoxLayout_delivery.addWidget(self.__radioButton_pickup)

        groupBox_delivery = QGroupBox("Lieferoptionen", self)
        groupBox_delivery.setLayout(vBoxLayout_delivery)

        self.__radioButton_paypal = QRadioButton("Paypal", self)
        self.__radioButton_bank = QRadioButton("Banküberweisung", self)
        self.__radioButton_crypto = QRadioButton("Bitcoin", self)
        self.__radioButton_cash = QRadioButton("Barzahlung", self)

        self.__buttonGroup_payment = QButtonGroup(self)
        self.__buttonGroup_payment.addButton(self.__radioButton_paypal)
        self.__buttonGroup_payment.addButton(self.__radioButton_bank)
        self.__buttonGroup_payment.addButton(self.__radioButton_crypto)
        self.__buttonGroup_payment.addButton(self.__radioButton_cash)

        vBoxLayout_payment = QVBoxLayout()
        vBoxLayout_payment.addWidget(self.__radioButton_paypal)
        vBoxLayout_payment.addWidget(self.__radioButton_bank)
        vBoxLayout_payment.addWidget(self.__radioButton_crypto)
        vBoxLayout_payment.addWidget(self.__radioButton_cash)

        groupBox_payment = QGroupBox("Bezahloption", self)
        groupBox_payment.setLayout(vBoxLayout_payment)

        self.__checkbox_agb = QCheckBox(self)
        self.__checkbox_agb.setText("Sie stimmen den AGBs zu.")
        self.__checkbox_agb.setToolTip("Unsere AGBs finden Sie auf unserer Website.")
        self.__checkbox_agb.setChecked(True)
        self.__checkbox_agb.released.connect(self.activate_agb)

        self.__checkbox_newsletter = QCheckBox(self)
        self.__checkbox_newsletter.setText("Newsletter abonieren.")
        self.__checkbox_newsletter.released.connect(self.activate_newsletter)

        self.__lineEdit = QLineEdit(self)
        self.__lineEdit.setHidden(True)

        self.__pushbutton = QPushButton(self)
        self.__pushbutton.setText("Verbindlich bestellen")

        grid = QGridLayout()
        grid.addWidget(self.__checkbox_agb, 0, 0)
        grid.addWidget(self.__checkbox_newsletter, 1, 0)
        grid.addWidget(self.__lineEdit, 2, 0)
        grid.addWidget(self.__pushbutton, 3, 0)
        grid.addWidget(groupBox_payment, 4, 0)
        grid.addWidget(groupBox_delivery, 5, 0)
        self.setLayout(grid)

    @pyqtSlot()
    def activate_agb(self):
        if self.__checkbox_agb.isChecked():
            self.__pushbutton.setEnabled(True)
        else:
            self.__pushbutton.setDisabled(True)

    @pyqtSlot()
    def activate_newsletter(self):
        if self.__checkbox_newsletter.isChecked():
            self.__lineEdit.setHidden(False)
        else:
            self.__lineEdit.setHidden(True)
