Документация
    PyQT_project(Python_programming) - приложение для отработки решения задач на языке Python.
Данное приложение служит для отработки навыков программирования. Задачи хранятся в базе данных SQLite, разделены по темам.
    Задачи можно решать как авторизированным пользователям так и нет. Для авторизированных пользователей появляется дополнительная 
фильтрация задач(решенные/нерешенные/все), у не авторизированных только фильтрация по темам.
    Так же реализована система тестирования и сохранения решения задачи. Задачи сохраняются только при условии авторизации, 
в противном случае при после тестирования выскакивает диалоговое окно с предупреждением, что для сохранения результата необходима авторизация.

Настройка программы
Необходимые для работы приложения модули перечислены в файле requirements.txt 
Установка модулей из файла requirements.txt по команде в терминале: $ pip install -r requirements.txt

Установка программы
Не требуется.

Запуск программы
Запустить приложение из файла PyQT_project/main.py или из PyQT_project/main.exe

Инструкция
Главное окно разделено на две части:
    * Левая часть содержит авторизацию и фильтры для выбора задач.
        При регистрации нового пользователя автоматически происходит его авторизация, смена пользователя осуществляется через
        кнопки войти или регистрацию нового. Так же при авторизации и регистрации есть возможность сохранения сессии.
    * Правая часть для выбора задач. Вывести доступные задачи можно нажав кнопку "Показать список задач", при этом выводится 
        список доступных задач (с учетом выбранных фильтров в левой части). В списке отображаются только номера задач и название задачи.
        Для выбора задачи надо кликнуть на соответствующее название в списке.
    При выборе задачи открывается окно для решения, сверху выводится условие, ниже поле для написания кода программы на языке python.
Для авторизированных пользователей вместе с условием задачи из БД подтягивается последнее решение и вставляется в поле ввода решения.
если решение требует ввода данных от пользователя, это происходит через узкое поле ввода, слева от кнопки "Запустить".
    Что бы запуск кода прошел успешно входные данные нужно вписать в это поле заранее, а только потом запустить код.
Кнопка "Запустить" не тестирует, а только запускает код с введенными входными данными.
Кнопка "Проверить" не считывает ввенденные входные данные, она прогоняет код по заранее заложенным тестам и сохраняет решение при любому 
результате прохождения тестов (сохранение только для авторизированных пользователей).
    В нижнем поле выводится результат запуска программы или прохождения тестов. При запуске происходит результат работы программы или 
ошибки с какими упала программа. При тестировании выводится список тестов и результат прохождения. Если тест пройден выводится "Ок",
если тест провален то "No" , входные данные теста, ожидаемый результат и результат запущенного кода.

Решенные задачи обозначаются зеленым лейблом "решено" под полем ввода кода.

В нижней части кнопки для перелистывания списка задач (пролистываются только не все задачи из БД, а только выбранные в главном окне)
Пролистывание задач происходит циклически.


Дополнения
Исходный код хранится на github. Сделаны коммиты по каждой доработке.

Выполнена сборка приложения в формат .exe