import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QMessageBox, QInputDialog
from PyQt5.QtWidgets import QLabel, QListWidget, QListWidgetItem, QPushButton, QComboBox, QRadioButton
from PyQt5.QtCore import QModelIndex
import sqlite3



class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setGeometry(400,400, 400, 400)
        self.list_widget = QListWidget(self)
        self.list_widget.addItems(['1', '2', '3', '4', '5'])
        self.list_widget.clicked.connect(self.choise)
        self.list_widget.currentItem()
        self.button = QPushButton('пни меня', self)
        self.button.move(0, 280)
        self.button.clicked.connect(self.choise)
        self.rb = QRadioButton('asdfgh', self)
        self.rb.setChecked(True)
        self.rb.move(0, 320)


        conn = sqlite3.connect('QT_project')
        cur = conn.cursor()
        temp = ', '.join(str(i[0]) for i in cur.execute('''
                            SELECT task_id FROM user_decision WHERE user_id = 3 AND complited = 1
                            ''').fetchall())
        print(temp)
        result = cur.execute(f"""SELECT id, title, task_text
                                FROM task
                                WHERE id not in ({temp})""").fetchall()
        conn.close()
        print(*result, sep='\n')

    def choise(self, item):
        print(
            item.data()
        )





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())