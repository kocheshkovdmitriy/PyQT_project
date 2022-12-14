from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 335)
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 0, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_user = QtWidgets.QLabel(self.centralwidget)
        self.welcome_user.setObjectName("welcome_user")
        self.verticalLayout.addWidget(self.welcome_user)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reg_button = QtWidgets.QPushButton(self.centralwidget)
        self.reg_button.setObjectName("reg_button")
        self.horizontalLayout.addWidget(self.reg_button)
        self.auth_button = QtWidgets.QPushButton(self.centralwidget)
        self.auth_button.setObjectName("auth_button")
        self.horizontalLayout.addWidget(self.auth_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.filters = QtWidgets.QLabel(self.centralwidget)
        self.filters.setObjectName("filters")
        self.verticalLayout.addWidget(self.filters)
        self.label_section = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_section.sizePolicy().hasHeightForWidth())
        self.label_section.setSizePolicy(sizePolicy)
        self.label_section.setObjectName("label_section")
        self.verticalLayout.addWidget(self.label_section)
        self.comboBox_section = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_section.setObjectName("comboBox_section")
        self.verticalLayout.addWidget(self.comboBox_section)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 10, 10, 10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.list_task = QtWidgets.QListWidget(self.centralwidget)
        self.list_task.setObjectName("list_task")
        self.verticalLayout_5.addWidget(self.list_task)
        self.show_list_task = QtWidgets.QPushButton(self.centralwidget)
        self.show_list_task.setObjectName("show_list_task")
        self.verticalLayout_5.addWidget(self.show_list_task)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.menu.addAction(self.about)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тренажер по python"))
        self.welcome_user.setText(_translate("MainWindow", "Здравствуйте, пожалуйста авторизируйтесь"))
        self.reg_button.setText(_translate("MainWindow", "Регистрация"))
        self.auth_button.setText(_translate("MainWindow", "Войти"))
        self.filters.setText(_translate("MainWindow", "Фильтры"))
        self.label_section.setText(_translate("MainWindow", "Выберите раздел:"))
        self.radioButton_3.setText(_translate("MainWindow", "только решенные"))
        self.radioButton_2.setText(_translate("MainWindow", "только не решенные"))
        self.radioButton_1.setText(_translate("MainWindow", "все"))
        self.label.setText(_translate("MainWindow", "Выбеите задачу"))
        self.show_list_task.setText(_translate("MainWindow", "Показать список задач"))
        self.menu.setTitle(_translate("MainWindow", "Помощь"))
        self.about.setText(_translate("MainWindow", "О программе"))


class Ui_FormTask(object):
    def setupUi(self, FormTask):
        FormTask.setObjectName("FormTask")
        FormTask.resize(545, 364)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormTask.sizePolicy().hasHeightForWidth())
        FormTask.setSizePolicy(sizePolicy)
        FormTask.setMinimumSize(QtCore.QSize(0, 0))
        FormTask.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(FormTask)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_task = QtWidgets.QLabel(FormTask)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_task.setFont(font)
        self.label_task.setObjectName("label_task")
        self.verticalLayout.addWidget(self.label_task)
        self.input_decision = QtWidgets.QTextEdit(FormTask)
        self.input_decision.setObjectName("input_decision")
        self.verticalLayout.addWidget(self.input_decision)
        self.label_verdict = QtWidgets.QLabel(FormTask)
        self.label_verdict.setEnabled(True)
        self.label_verdict.setObjectName("label_verdict")
        self.verticalLayout.addWidget(self.label_verdict)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_input = QtWidgets.QLabel(FormTask)
        self.label_input.setObjectName("label_input")
        self.horizontalLayout.addWidget(self.label_input)
        self.input_data = QtWidgets.QTextEdit(FormTask)
        self.input_data.setMaximumSize(QtCore.QSize(600, 30))
        self.input_data.setObjectName("input_data")
        self.horizontalLayout.addWidget(self.input_data)
        self.button_run_code = QtWidgets.QPushButton(FormTask)
        self.button_run_code.setObjectName("button_run_code")
        self.horizontalLayout.addWidget(self.button_run_code)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.button_run_test = QtWidgets.QPushButton(FormTask)
        self.button_run_test.setObjectName("button_run_test")
        self.verticalLayout.addWidget(self.button_run_test)
        self.output_answer = QtWidgets.QTextEdit(FormTask)
        self.output_answer.setEnabled(False)
        self.output_answer.setObjectName("output_answer")
        self.verticalLayout.addWidget(self.output_answer)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previous_task = QtWidgets.QPushButton(FormTask)
        self.previous_task.setObjectName("previous_task")
        self.horizontalLayout_2.addWidget(self.previous_task)
        self.next_task = QtWidgets.QPushButton(FormTask)
        self.next_task.setObjectName("next_task")
        self.horizontalLayout_2.addWidget(self.next_task)
        self.back_button = QtWidgets.QPushButton(FormTask)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_2.addWidget(self.back_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(FormTask)
        QtCore.QMetaObject.connectSlotsByName(FormTask)

    def retranslateUi(self, FormTask):
        _translate = QtCore.QCoreApplication.translate
        FormTask.setWindowTitle(_translate("FormTask", "Form"))
        self.label_task.setText(_translate("FormTask", "тут будет текст задачи"))
        self.label_verdict.setText(_translate("FormTask", "Решено"))
        self.label_input.setText(_translate("FormTask", "Входные данные"))
        self.button_run_code.setText(_translate("FormTask", "запустить"))
        self.button_run_test.setText(_translate("FormTask", "проверить"))
        self.previous_task.setText(_translate("FormTask", "Предыдущая задача"))
        self.next_task.setText(_translate("FormTask", "Следующая задача"))
        self.back_button.setText(_translate("FormTask", "К списку задач"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 233)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_login = QtWidgets.QLabel(Dialog)
        self.label_login.setObjectName("label_login")
        self.verticalLayout_2.addWidget(self.label_login)
        self.login = QtWidgets.QLineEdit(Dialog)
        self.login.setMaximumSize(QtCore.QSize(200, 16777215))
        self.login.setObjectName("login")
        self.verticalLayout_2.addWidget(self.login)
        self.label_password = QtWidgets.QLabel(Dialog)
        self.label_password.setObjectName("label_password")
        self.verticalLayout_2.addWidget(self.label_password)
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setMaximumSize(QtCore.QSize(200, 16777215))
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password)
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.input_name = QtWidgets.QLineEdit(Dialog)
        self.input_name.setMaximumSize(QtCore.QSize(200, 16777215))
        self.input_name.setObjectName("input_name")
        self.verticalLayout_2.addWidget(self.input_name)
        self.check_save_user = QtWidgets.QCheckBox(Dialog)
        self.check_save_user.setObjectName("check_save_user")
        self.verticalLayout_2.addWidget(self.check_save_user)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_login.setText(_translate("Dialog", "Введите логин"))
        self.label_password.setText(_translate("Dialog", "Введите пароль"))
        self.label_name.setText(_translate("Dialog", "Введите имя"))
        self.check_save_user.setText(_translate("Dialog", "сохранить авторизацию"))