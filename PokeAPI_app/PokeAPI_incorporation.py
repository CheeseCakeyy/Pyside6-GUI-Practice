import sys
import requests
from theme_toggle import Theme
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QPushButton,QLineEdit,QVBoxLayout
from PySide6.QtGui import QPixmap
from io import BytesIO

class Mycode(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon")

        main_window = QWidget()
        self.setCentralWidget(main_window)
        layout = QVBoxLayout()
        main_window.setLayout(layout)
        self.theme_manager = Theme(self,layout)
        
        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Enter a Pokemon Name")
        layout.addWidget(self.textbox)

        self.button = QPushButton("Submit")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.fetch_pokedata)

        self.info_label = QLabel("Pokemon info incoming")
        layout.addWidget(self.info_label)

        self.image_label = QLabel()
        self.image_label.setFixedSize(150,150)
        layout.addWidget(self.image_label)

    def fetch_pokedata(self):
        name = self.textbox.text().strip().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"

        try:
            response = requests.get(url)
            data = response.json()

            poke_name = data["name"].capitalize()
            poke_type = data["types"][0]["type"]["name"].capitalize()
            sprite_url = data["sprites"]["front_default"]

            self.info_label.setText(f"Name: {poke_name} \n Type: {poke_type}")

            image_data = requests.get(sprite_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(BytesIO(image_data).read())
            self.image_label.setPixmap(pixmap.scaled(150,150))

        except Exception as e: 
            self.info_label.setText("Failed to fetch data. Try a valid Pokémon name.")
            self.image_label.clear()
 
manager = QApplication(sys.argv)
window = Mycode()
window.show()
manager.exec()