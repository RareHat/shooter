from PyQt5.QtWidgets import *




window.show()
app.exec()

play_btn = QPushButton("Почати Гру")
settings_btn = QPushButton("Налаштування")
shop_btn = QPushButton("Магазин")
levels = QPushButton("Рівні")

main_line = QVBoxLayout()
main_line.AddWidget(play_btn)
main_line.AddWidget(settings_btn)
main_line.AddWidget(shop_btn)
main_line.AddWidget(levels)
















app = QApplication([])
window = QWidget()
