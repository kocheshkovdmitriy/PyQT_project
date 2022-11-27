import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QMessageBox, QInputDialog
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem

import sqlite3
import shlex
import subprocess




class About(QDialog):
    def __init__(self):
        super(About, self).__init__()
        self.setLayout(QHBoxLayout(self))
        self.lable = QLabel(
            'Тpенажер по Python',
            self
        )
        self.layout().addWidget(self.lable)


class Auth(QDialog):
    def __init__(self):
        super(Auth, self).__init__()
        uic.loadUi('auth_form.ui', self)
        self.buttonBox.accepted.connect(self.auth_user_ok)
        self.buttonBox.rejected.connect(self.auth_user_not)

    def auth_user_ok(self):
        login = self.login.text()
        password = self.password.text()
        conn = sqlite3.connect('QT_project')
        cur = conn.cursor()
        result = cur.execute(f"SELECT login, password, name, id FROM user WHERE login = '{login}'").fetchall()
        conn.close()
        if result:
            if str(result[0][1]) == password:
                MainWindow.user = (result[0][0], result[0][2], result[0][3])
                print(MainWindow.user)
            else:
                msgBox = QMessageBox()
                msgBox.setText("Неверный пароль!!!")
                msgBox.exec()
        elif login:
            name, ok_pressed = QInputDialog.getText(
                self,
                "Неверный логин",
                "Пользователя с таким логином не существует!\n"
                "Хотите создать пользователя?\n"
                "введите имя:")
            if ok_pressed:
                print(login, password, name)
                conn = sqlite3.connect('QT_project')
                cur = conn.cursor()
                cur.execute(f"INSERT INTO user(login, password, name) VALUES ('{login}', '{password}', '{name}')")
                conn.commit()
                conn.close()
                MainWindow.user = (login, name)
                print(MainWindow.user)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Поле 'логин' не может быть пустым!\n Введите ваши данные еще раз")
            msg.setWindowTitle("Ошибка имени пользователя")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        self.login.clear()
        self.password.clear()

    def auth_user_not(self):
        self.login.clear()
        self.password.clear()



class Task(QWidget):
    def __init__(self, text, mainWin):
        super(Task, self).__init__()
        self.mainWin = mainWin
        uic.loadUi('FormTask.ui', self)

        self.setWindowTitle(text[0])
        self.btn1.clicked.connect(self.run_code)
        self.btn2.clicked.connect(self.run_test)
        self.task.setText(text[1])

    def run_code(self):
        code = self.decision.toPlainText()
        command = f'python -c "{code}"'
        command = shlex.split(command)
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        outs, errs = process.communicate(timeout=1)

        print(outs.decode(), errs.decode())
        self.answer.setText(f'{outs.decode()}{errs.decode()}')

    def run_test(self):
        self.answer.setText("Тестируем вот этот код:\n{}".format(self.decision.toPlainText()))

    def closeEvent(self, event):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Вы действительно хотите уйти?\n Не отправленное решение не будет сохранено!")
        msg.setWindowTitle("Завершение работы")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msg.exec() == 1024:
            self.mainWin.show()
            event.accept()
        else:
            event.ignore()


class MainWindow(QMainWindow):
    user = (None, None, None)

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWin.ui', self)
        self.setWindowTitle('Тренажер по python')
        self.about_dialog = About()
        self.auth_dialog = Auth()

        self.radioButton_1.setChecked(True)
        self.radioButton_1.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()

        conn = sqlite3.connect('QT_project')
        cur = conn.cursor()
        result = [str(el[0]) + ' ' + (el[1]
                  if len(el[1]) < 30 else el[1][:27] + '...')
                  for el in cur.execute(f"SELECT id, section FROM section_task ORDER BY id").fetchall()]
        conn.close()
        self.comboBox_section.addItems(['Все темы'] + result)

        self.show_list_task.clicked.connect(self.choise_task)
        self.about.triggered.connect(self.show_about)
        self.auth_button.clicked.connect(self.show_auth)
        self.filter_button.clicked.connect(self.run_filter)
        self.list_task.clicked.connect(self.show_task)

    def choise_task(self):
        sql_request = self.__get_sql_request()
        conn = sqlite3.connect('QT_project')
        cur = conn.cursor()
        result = [' '.join(str(i) for i in el)
                  for el in cur.execute(sql_request).fetchall()]
        conn.close()
        self.list_task.clear()
        self.list_task.addItems(result)


    def show_task(self, item):
        conn = sqlite3.connect('QT_project')
        cur = conn.cursor()
        result = cur.execute(f"SELECT title, task_text"
                             f" FROM task "
                             f"WHERE id = {item.data().split()[0]}").fetchall()
        conn.close()
        self.second_form = Task(result[0], self)
        self.second_form.show()
        self.hide()

    def show_about(self):
        self.about_dialog.show()

    def show_auth(self):
        self.auth_dialog.show()
        self.hide()

        if self.auth_dialog.exec_() == QDialog.Accepted:
            self.show()
            if not MainWindow.user[0] is None:
                self.welcome_user.setText(f'Здравствуйте, {MainWindow.user[1]}')
                self.radioButton_1.show()
                self.radioButton_2.show()
                self.radioButton_3.show()

    def run_filter(self):
        print(
            self.comboBox_section.currentText(),
            self.radioButton_1.isChecked(),
            self.radioButton_2.isChecked(),
            self.radioButton_3.isChecked()
        )

    def __get_sql_request(self):
        choise_filters = list()
        if self.comboBox_section.currentText() != 'Все темы':
            choise_filters.append(f'section_id = {self.comboBox_section.currentText().split()[0]}')
        if not (MainWindow.user[2] is None or self.radioButton_1.isChecked()):
            conn = sqlite3.connect('QT_project')
            cur = conn.cursor()
            temp = ', '.join(str(i[0])
                             for i in cur.execute(
                                      f"""
                                      SELECT task_id 
                                      FROM user_decision 
                                      WHERE user_id = {MainWindow.user[2]} AND complited = 1
                                      """).fetchall())
            if self.radioButton_2.isChecked():
                choise_filters.append(f"""id not in ({temp})""")
            else:
                choise_filters.append(f"""id in ({temp})""")
            conn.close()

        sql_request = f"""SELECT id, title 
                          FROM task 
                          {('WHERE ' + ' AND '.join(choise_filters)) if choise_filters else ''}
                          ORDER BY id"""
        print(sql_request)
        return sql_request


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())