from PyQt6.QtWidgets import QMainWindow, QMessageBox
from auth import Ui_MainWindow
from db import Database
from client_window import ClientWindow
from admin_manager_window import AdminManagerWindow

# класс окна авторизации
class AuthWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        self.client_window = None
        self.admin_window = None
        self.manager_window = None

        self.pushButton_2.clicked.connect(self.auth_guest)
        self.pushButton.clicked.connect(self.auth)

    # вход за гостя
    def auth_guest(self):
        QMessageBox.information(self, 'Успех', 'Добро пожаловать!')
        self.client_window = ClientWindow(None, 'Гость', self.db, self)
        self.client_window.show()

        self.hide()

    # вход за авторизированного пользователя
    def auth(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()

        user = self.db.get_user(login, password)
        if user:
            full_name = f"{user.get('surname', '')} {user.get('name', '')} {user.get('patronymic', '')}"
            QMessageBox.information(self, 'Успех', f'Добро пожаловать, {full_name}!')

            if user.get('role_name', '') == 'Авторизированный клиент':
                self.client_window = ClientWindow(user, full_name, self.db, self)
                self.client_window.show()
            elif user.get('role_name', '') == 'Администратор':
                try:
                    self.admin_window = AdminManagerWindow(user, full_name, self.db, self, True)
                    self.admin_window.show()
                except Exception as e:
                    QMessageBox.critical(None, 'Ошибка', f'Ошибка: {e}')
            elif user.get('role_name', '') == 'Менеджер':
                self.manager_window = AdminManagerWindow(user, full_name, self.db, self, False)
                self.manager_window.show()
            self.hide()
        else:
            QMessageBox.warning(self, 'Ошибка', f'Неверный логин или пароль')

    # показ окна авторизации
    def show_auth_window(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.show()