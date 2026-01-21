import sys
import requests
from theme_toggle import Theme
from PySide6.QtWidgets import QApplication,QHBoxLayout,QSpinBox,QMainWindow,QWidget,QLabel,QVBoxLayout,QComboBox,QPushButton

class money_exchange(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Money_Exchange_Rates")
        currencies = ["USD", "EUR", "INR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY"]

        main_window = QWidget()
        self.setCentralWidget(main_window)
        layout = QVBoxLayout()
        main_window.setLayout(layout)
        self.theme_toggle = Theme(self,layout)

        self.input_field = QSpinBox()
        self.input_field.setMaximum(1000000000)
        layout.addWidget(self.input_field)

        HLayout_for_label = QHBoxLayout()
        layout.addLayout(HLayout_for_label)
        HLayout_for_combobox = QHBoxLayout()
        layout.addLayout(HLayout_for_combobox)


        self.label1 = QLabel()
        self.label1.setText("From: ")
        HLayout_for_label.addWidget(self.label1)
        self.label2 = QLabel()
        self.label2.setText("To: ")
        HLayout_for_label.addWidget(self.label2)

        self.currency1 = QComboBox()
        self.currency2 = QComboBox()
        self.currency1.addItems(currencies)
        self.currency2.addItems(currencies)
        HLayout_for_combobox.addWidget(self.currency1)
        HLayout_for_combobox.addWidget(self.currency2)

        self.button = QPushButton("Convert")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.conversion)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

    def conversion(self):
         amount = self.input_field.value()
         from_currency = self.currency1.currentText()
         to_currency = self.currency2.currentText()
        
         try: 
             response = requests.get(f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}")
             data = response.json()
             result = data["rates"][f"{to_currency}"]
             final_conversion = result * amount
             self.result_label.setText(f"{amount} {from_currency} =  {final_conversion} {to_currency} ")
         except Exception as e:
             self.result_label.setText("Conversion Failed")
    

manager = QApplication(sys.argv) 
window = money_exchange()
window.show()
manager.exec()           
