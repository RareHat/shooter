from PyQt5.QtWidgets import *

import main

app = QApplication([])
window = QWidget()



play_btn = QPushButton("Почати Гру")
settings_btn = QPushButton("Налаштування")
shop_btn = QPushButton("Магазин")
levels = QPushButton("Рівні")

play_btn.clicked.connect(main.game)



main_line = QVBoxLayout()
main_line.addWidget(play_btn)
main_line.addWidget(settings_btn)
main_line.addWidget(shop_btn)
main_line.addWidget(levels)
window.setLayout(main_line)















window.show()
app.exec()

