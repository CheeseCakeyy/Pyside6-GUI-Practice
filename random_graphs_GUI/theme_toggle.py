from PySide6.QtWidgets import QPushButton
import sys

class Theme:
    def __init__(self,window,layout):
        self.window = window
        self.light_mode = True

        self.toggle_button = QPushButton("Enable Dark Mode")
        self.toggle_button.clicked.connect(self.toggle_theme)
        layout.addWidget(self.toggle_button)

        self.apply_light_theme()

    def toggle_theme(self):
        if self.light_mode:
            self.apply_dark_theme()
            self.toggle_button.setText("Enable Light Mode")
        else:
            self.apply_light_theme()
            self.toggle_button.setText("Enable Dark Mode")
        self.light_mode = not self.light_mode

    def apply_light_theme(self):
        self.window.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                color: #000;
            }
            QPushButton {
                background-color: #e0e0e0;
                padding: 6px;
                border-radius: 4px;
            }
        """)

    def apply_dark_theme(self):
        self.window.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #fff;
            }
            QPushButton {
                background-color: #444;
                color: #fff;
                padding: 6px;
                border-radius: 4px;
            }
        """)