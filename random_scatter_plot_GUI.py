import sys
from theme_toggle import Theme
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog

class Myplots(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple Plots")

        main_window = QWidget()
        self.setCentralWidget(main_window)
        main_layout= QVBoxLayout()
        main_window.setLayout(main_layout)
        self.theme_manager = Theme(self, main_layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        self.save_button = QPushButton("Save the Current Graph")
        main_layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save)

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        self.button1 = QPushButton("Random scatter plot")
        self.button2 = QPushButton("Bar Graph")
        self.button3 = QPushButton("Pie chart")

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)

        self.button1.clicked.connect(self.plot1)
        self.button2.clicked.connect(self.plot2)
        self.button3.clicked.connect(self.plot3)

    def plot1(self):
        self.figure.clear()
        ax =  self.figure.add_subplot(111)
        x = np.random.randint(200,size=100)
        y = np.random.randint(200,size=100)
        colors = np.random.randint(200,size=100)
        size = 10*np.random.randint(100,size=100)
        ax.scatter(x,y,c=colors,s=size,alpha=0.5,cmap='seismic_r')
        ax.set_title("Random scatter plot")  
        ax.axis('off')
        self.canvas.draw()

    def plot2(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        x = np.array([3,4,5,7,9])
        y = np.array([1,2,3,4,4])
        ax.plot(x,y,marker='o')
        ax.set_title("Line Graph")
        self.canvas.draw()

    def plot3(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        x = np.array([25,50,25])
        mylabels = ["Apples", "Bananas", "Cherries"]
        ax.pie(x,labels=mylabels,startangle=90, shadow=True)
        ax.set_title("Pie Chart")
        self.canvas.draw()

    def save(self):
        filename,_ = QFileDialog.getSaveFileName(self,"Save the Current Graph")
        if filename:
            self.figure.savefig(filename)

Manager = QApplication(sys.argv)
window = Myplots()
window.show()

Manager.exec()
