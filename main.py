import sys

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QMessageBox, QInputDialog
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem

import sqlite3

from run_and_test_code import run, testing


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
        user = self.__get_user(login)
        if user:
            if str(user[0][1]) == password:
                MainWindow.user = (user[0][0], user[0][2], user[0][3])
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
                conn = sqlite3.connect('QT_project')
                cur = conn.cursor()
                cur.execute(f"INSERT INTO user(login, password, name) VALUES ('{login}', '{password}', '{name}')")
                conn.commit()
                conn.close()
                user = self.__get_user(login)
                MainWindow.user = (login, name, user[0][3])
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

    def __get_user(self, login):
        conn = sqlite3.connect('QT_project')
        cur = conn.cursor()
        result = cur.execute(f"SELECT login, password, name, id FROM user WHERE login = '{login}'").fetchall()
        conn.close()
        return result



class Task(QWidget):
    """
    Виджет окна решения задачи.
    :arg
        mainWin объект главного окна, в нем список выбранных задач и пользователь
            .user(login, name, id)
            .tasks[id,...]
        task[id, title, text, tests, decision, flag_done] текущая задача
    """

    def __init__(self, pk, mainWin):
        super(Task, self).__init__()
        uic.loadUi('FormTask.ui', self)
        self.setWindowIcon(QIcon('python.jpg'))
        self.label_verdict.hide()
        self.label_verdict.setStyleSheet("background-color: #94db70;")
        self.mainWin = mainWin
        self.task = self.__get_task(pk)

        self.__view_task()
        self.button_run_code.clicked.connect(self.run_code)
        self.button_run_test.clicked.connect(self.run_test)
        self.previous_task.clicked.connect(self.show_previous_task)
        self.next_task.clicked.connect(self.show_next_task)
        self.back_button.clicked.connect(self.back)

    def run_code(self):
        code = self.input_decision.toPlainText()
        outs, errs = run(code, self.input_data.toPlainText())
        self.output_answer.setText(f'{outs.decode()}{errs.decode()}')

    def run_test(self):
        code = self.input_decision.toPlainText()
        result, flag_done = testing(code, self.task[3])
        self.output_answer.setText(result)
        if not MainWindow.user[0] is None:
            conn = sqlite3.connect('QT_project')
            cur = conn.cursor()
            if self.task[4]:
                print('Перезаписываем решение')
                request = f"""UPDATE user_decision SET complited = '{flag_done}', task_decision = "{code}" 
                              WHERE task_id = '{self.task[0]}' AND user_id = '{MainWindow.user[2]}'"""
            else:
                print('Сохраняем решение')
                request = f"""INSERT INTO user_decision(task_id, complited, task_decision, user_id)
                              VALUES ('{self.task[0]}', '{flag_done}', "{code}", '{MainWindow.user[2]}')"""
            self.task[4], self.task[5] = code, flag_done
            if self.task[5]:
                self.label_verdict.show()
            else:
                self.label_verdict.hide()
            cur.execute(request)
            conn.commit()
            conn.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Сохранять решения могут только авторизированные пользователи!!!\n"
                        "Если хотите сохранить решения вернитесь к списку задач и авторизируйтесь.")
            msg.setWindowTitle("Сохранение не удалось")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def show_previous_task(self):
        self.__clear_input()
        index_task = (self.mainWin.tasks.index(self.task[0]) - 1) % len(self.mainWin.tasks)
        self.task = self.__get_task(self.mainWin.tasks[index_task])
        self.__view_task()

    def show_next_task(self):
        self.__clear_input()
        index_task = (self.mainWin.tasks.index(self.task[0]) + 1) % len(self.mainWin.tasks)
        self.task = self.__get_task(self.mainWin.tasks[index_task])
        self.__view_task()

    def back(self):
        self.close()

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

    def __get_task(self, pk):
        conn = sqlite3.connect('QT_project')
        cur = conn.cursor()
        task = cur.execute(f"SELECT id, title, task_text, tests"
                             f" FROM task "
                             f"WHERE id = {pk}").fetchall()
        decision = []
        if not MainWindow.user[0] is None:
            decision = cur.execute(f"SELECT task_decision, complited"
                                 f" FROM user_decision "
                                 f"WHERE user_id = {MainWindow.user[2]} AND task_id = {pk}").fetchall()
        conn.close()
        if not decision:
            decision = [['', 0]]
        task = list(task[0])
        task.extend(decision[0])
        return task

    def __view_task(self):
        self.setWindowTitle(self.task[1])
        self.label_task.setText(self.task[2])
        self.input_decision.setText(self.task[4])
        if self.task[5]:
            self.label_verdict.show()
        else:
            self.label_verdict.hide()

    def __clear_input(self):
        self.input_decision.clear()
        self.input_data.clear()
        self.output_answer.clear()


class MainWindow(QMainWindow):
    '''
    Виджет главного окна.
    :arg
        user(login, name, id) авторизированный пользователь, по умолчанию (None, None, None)
    '''

    user = (None, None, None)

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWin.ui', self)
        self.setWindowTitle('Тренажер по python')
        self.setWindowIcon(QIcon('python.jpg'))
        self.about_dialog = About()
        self.auth_dialog = Auth()
        self.tasks = list()

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
        self.list_task.clicked.connect(self.show_task)

    def choise_task(self):
        sql_request = self.__get_sql_request()
        conn = sqlite3.connect('QT_project')
        cur = conn.cursor()
        result = cur.execute(sql_request).fetchall()
        self.tasks = [el[0] for el in result]
        result = [' '.join(str(i) for i in el) for el in result]
        conn.close()
        self.list_task.clear()
        self.list_task.addItems(result)

    def show_task(self, item):
        self.second_form = Task(item.data().split()[0], self)
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
        return sql_request


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())