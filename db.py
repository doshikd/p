import pymysql
from PyQt6.QtWidgets import QMessageBox
from pymysql.cursors import DictCursor

# класс для работы с БД
class Database:
    def __init__(self, host='127.127.126.50', user='root', password='root', database='shoe_store'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.conn = None
        self.cursor = None

    # подключение к БД
    def connect(self):
        if self.conn:
            return True

        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4',
                cursorclass=DictCursor
            )
            self.cursor = self.conn.cursor()
            return True
        except pymysql.Error as e:
            QMessageBox.critical(None, 'Ошбика', f'Ошибка подключения к БД: {e}')
            self.conn = None
            self.cursor = None
            return False

    # получение пользователя по логину и паролю
    def get_user(self, login, password):
        if not self.connect():
            return None

        try:
            query = '''
                SELECT u.*, r.name as role_name
                FROM user u JOIN role r ON u.role_id = r.id
                WHERE u.login = %s AND u.password = %s
            '''
            self.cursor.execute(query, (login, password))
            return self.cursor.fetchone()
        except pymysql.Error as e:
            QMessageBox.critical(None, 'Ошбика', f'Ошибка запроса: {e}')
            return None

    # получение всех товаров
    def get_all_products(self):
        if not self.connect():
            return []

        try:
            query = '''
                SELECT p.*, pr.name as provider_name, m.name as manufacturer_name, pc.name as category_name
                FROM product p JOIN provider pr ON p.provider_id = pr.id
                JOIN manufacturer m ON p.manufacturer_id = m.id
                JOIN product_category pc ON p.category_id = pc.id
            '''
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except pymysql.Error as e:
            QMessageBox.critical(None, 'Ошбика', f'Ошибка запроса: {e}')
            return []

    # получение всех заказов
    def get_all_orders(self):
        if not self.connect():
            return []

        try:
            query = '''
                SELECT o.*, s.name as status_name, a.city, a.street, a.house
                FROM `order` o JOIN status s ON o.status_id = s.id
                JOIN address a ON o.address_id = a.id
            '''
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except pymysql.Error as e:
            QMessageBox.critical(None, 'Ошбика', f'Ошибка запроса: {e}')
            return []