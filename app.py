import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon

from api_call import get_information

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PHHS Brawl Stars AI by Rikhil")
        self.setWindowIcon(QIcon("../aiclub.png"))
        self.setFixedSize(QSize(1200, 800))

        self.title_label = QLabel("Player Info Input", self)
        self.title_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)

        self.token_label = QLabel("Enter Token:")
        self.token_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.token_input = QLineEdit()
        self.token_input.setFont(QFont("Arial", 14))

        self.player_tag_label = QLabel("Enter Player Tag:")
        self.player_tag_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.player_tag_input = QLineEdit()
        self.player_tag_input.setFont(QFont("Arial", 14))

        self.submit_button = QPushButton("Submit")
        self.submit_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.submit_button.setStyleSheet("""
                                            QPushButton {
                                                background-color: #007BFF; 
                                                color: white; 
                                                padding: 10px; 
                                                border-radius: 5px; 
                                            }
                                            QPushButton:hover {
                                                background-color: #0056b3; /* Darker blue on hover */
                                            }
                                            QPushButton:pressed {
                                                background-color: #004494; /* Even darker blue when clicked */
                                            }
                                        """)
        self.submit_button.clicked.connect(self.submit_info)

        self.output_label = QLabel("Output will appear here", self) 
        self.output_label.setFont(QFont("Arial", 16))
        self.output_label.setAlignment(Qt.AlignCenter)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("../mico.png").scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label.setAlignment(Qt.AlignCenter)

        horizontal_spacer = QSpacerItem(0, 50)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.token_label)
        input_layout.addWidget(self.token_input)
        input_layout.addWidget(self.player_tag_label)
        input_layout.addWidget(self.player_tag_input)
        input_layout.addWidget(self.submit_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addLayout(input_layout)
        layout.addItem(horizontal_spacer)
        layout.addWidget(self.image_label)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

        self.setStyleSheet("""
                                QWidget {
                                    background-color: #E6F0FF;
                                }
                                QLabel {
                                    color: #003366;
                                }
                                QLineEdit {
                                    background-color: #FFFFFF;
                                    border: 2px solid #003366;
                                    padding: 10px;
                                    border-radius: 15px;
                                }
                            """)
    def submit_info(self):
        token = self.token_input.text()
        player_tag = self.player_tag_input.text()

        if token and player_tag:
            get_information(token, player_tag)

            with open("output.txt", "r", encoding="utf-8") as fin:
                self.output_label.setText(fin.read())
                self.image_label.setPixmap(QPixmap("../barley.png").scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        else:
            self.output_label.setText("Please enter both token and player tag.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
