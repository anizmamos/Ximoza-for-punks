# imports
import sys
from random import choice, randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon


class Opening(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window setup
        self.setGeometry(412, 412, 412, 500)
        self.setWindowTitle('Хiмоz@ for punks')
        self.pixmap = QPixmap('ximoza.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(412, 412)
        self.image.setPixmap(self.pixmap)
        self.setWindowIcon(QIcon("icon.jpg"))

        # Button setup
        self.btn = QPushButton('Начать', self)
        self.btn.resize(412, 100)
        self.btn.move(0, 400)
        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        # Form changer
        self.second_form = Menu(self, "")
        self.second_form.show()
        self.close()


class Menu(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, *args):
        # Window setup
        self.setGeometry(412, 412, 412, 500)
        self.setWindowTitle('Хiмоz@ for punks')
        self.pixmap = QPixmap('ximoza2.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(412, 412)
        self.image.setPixmap(self.pixmap)
        self.setWindowIcon(QIcon("icon.jpg"))

        # Difficult button1 setup
        self.button_1 = QPushButton('Учебник', self)
        self.button_1.resize(412, 100)
        self.button_1.move(0, 200)
        self.button_1.clicked.connect(self.open_handbook)

        self.button_2 = QPushButton('Элементы для новичков', self)
        self.button_2.resize(206, 100)
        self.button_2.move(0, 300)
        self.button_2.clicked.connect(self.open_easy_elem)

        self.button_3 = QPushButton('O и OH для чайников', self)
        self.button_3.resize(206, 100)
        self.button_3.move(206, 300)
        self.button_3.clicked.connect(self.open_easy_o_oh)

        self.button_4 = QPushButton('Элементы для знатоков', self)
        self.button_4.resize(206, 100)
        self.button_4.move(0, 400)
        self.button_4.clicked.connect(self.open_hard_elem)

        self.button_5 = QPushButton('O и OH для профи', self)
        self.button_5.resize(206, 100)
        self.button_5.move(206, 400)
        self.button_5.clicked.connect(self.open_easy_o_oh)

        self.show()

    def open_handbook(self):
        # Form changer
        self.easy_Handbook_form = Handbook()
        self.easy_Handbook_form.show()

    def open_easy_elem(self):
        # Form changer
        self.easy_Elem_form = EasyElem()
        self.easy_Elem_form.show()

    def open_easy_o_oh(self):
        # Form changer
        self.easy_O_OH_form = Menu(self, "")
        self.easy_O_OH_form.show()

    def open_hard_elem(self):
        # Form changer
        self.hard_Elem_form = Menu(self, "")
        self.hard_Elem_form.show()

    def open_hard_o_oh(self):
        # Form changer
        self.hard_O_OH_form = Menu(self, "")
        self.hard_O_OH_form.show()


class Handbook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window setup
        self.setGeometry(412, 412, 412, 500)
        self.setWindowTitle('Хiмоz@ for punks')
        self.pixmap = QPixmap('mendtable.jpeg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(412, 412)
        self.image.setPixmap(self.pixmap)
        self.setWindowIcon(QIcon("icon.jpg"))

        self.button_1 = QPushButton('Оксиды', self)
        self.button_1.resize(206, 100)
        self.button_1.move(0, 400)
        self.button_1.clicked.connect(self.open_handbook_o)

        self.button_2 = QPushButton('Гидрооксиды', self)
        self.button_2.resize(206, 100)
        self.button_2.move(206, 400)
        self.button_2.clicked.connect(self.open_handbook_oh)

    def open_handbook_o(self):
        # Form changer
        self.easy_Handbook_form = HandbookO()
        self.easy_Handbook_form.show()
        self.close()

    def open_handbook_oh(self):
        # Form changer
        self.easy_Elem_form = EasyElem()
        self.easy_Elem_form.show()
        self.close()


class HandbookO(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window setup
        self.setGeometry(412, 412, 412, 500)
        self.setWindowTitle('Хiмоz@ for punks')
        self.pixmap = QPixmap('o.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(412, 412)
        self.image.setPixmap(self.pixmap)
        self.setWindowIcon(QIcon("icon.jpg"))

        self.button_1 = QPushButton('Оксиды', self)
        self.button_1.resize(206, 100)
        self.button_1.move(0, 400)
        self.button_1.clicked.connect(self.open_handbook_o)

        self.button_2 = QPushButton('Гидрооксиды', self)
        self.button_2.resize(206, 100)
        self.button_2.move(206, 400)
        self.button_2.clicked.connect(self.open_handbook_oh)

    def open_handbook_o(self):
        # Form changer
        self.easy_Handbook_form = Handbook()
        self.easy_Handbook_form.show()

    def open_handbook_oh(self):
        # Form changer
        self.easy_Elem_form = EasyElem()
        self.easy_Elem_form.show()


class EasyElem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window setup
        self.setGeometry(412, 412, 412, 500)
        self.setWindowTitle('Хiмоz@ for punks')
        self.setWindowIcon(QIcon("icon.jpg"))

        self.easyelem = {'H': 'Водород', 'Li': 'Литий', 'Cu': 'Медь', 'Fe': 'Железо', 'O': 'Кислород',
                         'Na': 'Натрий', 'K': 'Калий', 'N': 'Азот', 'Mg': 'Магний', 'Ca': 'Кальций',
                         'Zn': 'Цинк', 'Ag': 'Серебро', 'Au': 'Золото', 'Al': 'Алюминий', 'Si': 'Кремний'}

        self.easychoice = choice(list(self.easyelem.keys()))
        self.f_in = list(open('score.txt'))
        self.f_out = open('score.txt', mode='w')

        if randint(0, 1) == 1:
            self.name_label = QLabel(self)
            self.name_label.setText(self.easychoice)
            self.name_label.move(40, 90)

            self.button_1 = QPushButton(self.easyelem[self.easychoice], self)
            self.button_1.resize(206, 100)
            self.button_1.move(0, 400)
            self.button_1.clicked.connect(self.correct)

            self.button_2 = QPushButton(self.easyelem[choice(list(self.easyelem.keys()))], self)
            self.button_2.resize(206, 100)
            self.button_2.move(206, 400)
            self.button_2.clicked.connect(self.incorrect)

            self.button_3 = QPushButton('Назад', self)
            self.button_3.resize(412, 50)
            self.button_3.move(0, 0)
            self.button_3.clicked.connect(self.esc)

        else:
            self.name_label = QLabel(self)
            self.name_label.setText(self.easychoice)
            self.name_label.move(40, 90)

            self.button_2 = QPushButton(self.easyelem[choice(list(self.easyelem.keys()))], self)
            self.button_2.resize(206, 100)
            self.button_2.move(0, 400)
            self.button_2.clicked.connect(self.incorrect)

            self.button_1 = QPushButton(self.easyelem[self.easychoice], self)
            self.button_1.resize(206, 100)
            self.button_1.move(206, 400)
            self.button_1.clicked.connect(self.correct)

            self.button_3 = QPushButton('Назад', self)
            self.button_3.resize(412, 50)
            self.button_3.move(0, 0)
            self.button_3.clicked.connect(self.esc)

    def esc(self):
        # Form changer
        self.close()

    def correct(self):
        # Form changer
        self.easy_Elem_form = EasyElem()
        self.easy_Elem_form.show()
        self.score += 1
        print(self.score)

    def incorrect(self):
        # Form changer
        self.score -= 1
        print(self.score)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Opening()
    ex.show()
    sys.exit(app.exec())