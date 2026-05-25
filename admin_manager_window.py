from PyQt6.QtGui import QPixmap, QColor, QFont
from PyQt6.QtWidgets import QWidget, QFrame, QHBoxLayout, QLabel, QVBoxLayout, QMessageBox, QPushButton
from PyQt6.QtCore import Qt
from admin_manager import Ui_Form
import os

# класс окна админа / менеджера
class AdminManagerWindow(QWidget, Ui_Form):
    def __init__(self, user_data, full_name, db, auth_window, is_admin=False):
        super().__init__()
        self.setupUi(self)

        self.user_data = user_data
        self.full_name = full_name
        self.db = db
        self.auth_window = auth_window
        self.is_admin = is_admin

        self.all_products = []
        self.search_text = ""
        self.provider_filter = "Все поставщики"
        self.sort_order = None

        if self.is_admin:
            self.label_2.setText(f"{full_name} | Администратор")
            self.label_7.setText(f"{full_name} | Администратор")
            self.setWindowTitle('Администратор')
        else:
            self.label_7.setText(f"{full_name} | Менеджер")
            self.label_2.setText(f"{full_name} | Менеджер")
            self.setWindowTitle('Менеджер')
            self.pushButton_3.setVisible(False)
            self.pushButton_5.setVisible(False)

        self.pushButton_3.clicked.connect(self.plug)
        self.pushButton_5.clicked.connect(self.plug)

        self.pushButton.clicked.connect(self.logout)
        self.pushButton_4.clicked.connect(self.logout)

        self.setup_search_and_filters()

        self.load_products()
        self.load_orders()

    # подключение обрабодчиков изменения текста поиска, фильтров и сортировки
    def setup_search_and_filters(self):
        self.lineEdit.textChanged.connect(self.change_search_text)
        self.pushButton_2.clicked.connect(self.clear_filters)
        self.comboBox.currentTextChanged.connect(self.change_provider_filter)
        self.comboBox_2.currentTextChanged.connect(self.change_sort_order)

    # изменение текста поиска
    def change_search_text(self, text):
        self.search_text = text
        self.apply_filters()

    # очистка фильтров
    def clear_filters(self):
        self.lineEdit.clear()
        self.comboBox.setCurrentText("Все поставщики")
        self.comboBox_2.setCurrentText("Без сортировки")

    # изменения фильтра по поставщику
    def change_provider_filter(self, provider):
        self.provider_filter = provider
        self.apply_filters()

    # изменение сортировки
    def change_sort_order(self, sort_option):
        if sort_option == "Без сортировки":
            self.sort_order = None
        elif sort_option == "По возрастанию (склад)":
            self.sort_order = 'asc'
        if sort_option == "По убыванию (склад)":
            self.sort_order = 'desc'

        self.apply_filters()

    # применение фильтров
    def apply_filters(self):
        if not self.all_products:
            return

        filtered = self.all_products.copy()

        if self.search_text:
            filtered = [p for p in filtered if self.search_in_product(p)]

        if self.provider_filter != "Все поставщики":
            filtered = [p for p in filtered
                        if p.get('provider_name') == self.provider_filter]

        if self.sort_order == 'asc':
            filtered.sort(key=self.get_stock)
        elif self.sort_order == 'desc':
            filtered.sort(key=self.get_stock, reverse=True)

        self.label_3.setText(f"Найдено: {len(filtered)} из {len(self.all_products)}")
        self.render_products(filtered)

    # получение колиечества товара на складе
    def get_stock(self, product):
        return product.get('quantity_stock', 0)

    # поиск по данным товара
    def search_in_product(self, product):
        text = self.search_text

        fields = [
            str(product.get('name', '')).lower(),
            str(product.get('description', '')).lower(),
            str(product.get('category_name', '')).lower(),
            str(product.get('provider_name', '')).lower(),
            str(product.get('manufacturer_name', '')).lower(),
            str(product.get('price', '')).lower(),
            str(product.get('unit', '')).lower(),
            str(product.get('quantity_stock', '')).lower(),
            str(product.get('discount', '')).lower(),
            str(product.get('image_path', '')).lower()
        ]

        return any(text in field for field in fields)

    # создание карточки товара
    def create_product_card(self, product):
        card = QFrame()
        card.setStyleSheet('''
            QFrame {
                border: 1px solid #00FA9A;
            }
        ''')

        discount = product.get('discount', 0)
        stock = product.get('quantity_stock', 0)

        text_color = "#000000"

        if stock == 0:
            card.setStyleSheet('''
                        QFrame {
                            background-color: #55ffff;
                        }
                    ''')
        elif discount > 15:
            card.setStyleSheet('''
                        QFrame {
                            background-color: #2E8B57;
                        }
                    ''')
            text_color = "#ffffff"

        layout = QHBoxLayout(card)

        photo_label = QLabel()
        photo_label.setFixedSize(180, 180)
        photo_label.setStyleSheet('border: none;')

        image_path = product.get('image_path')
        if image_path:
            full_path = os.path.join('images', image_path)
        else:
            full_path = None

        pixmap = QPixmap()

        if full_path and os.path.exists(full_path) and pixmap.load(full_path):
            photo_label.setPixmap(pixmap.scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio,
                                                Qt.TransformationMode.SmoothTransformation))
        else:
            if os.path.exists('images/picture.png'):
                pixmap = QPixmap('images/picture.png')
                photo_label.setPixmap(pixmap.scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio,
                                                    Qt.TransformationMode.SmoothTransformation))
            else:
                pixmap = QPixmap(180, 180)
                pixmap.fill(QColor("#CCCCCC"))
                photo_label.setPixmap(pixmap)

        layout.addWidget(photo_label)

        info_frame = QFrame()
        info_frame.setStyleSheet('border: none;')

        info_layout = QVBoxLayout(info_frame)

        title_label = QLabel(f"{product.get('category_name', 'Без категории')} | {product.get('name', 'Без названия')}")
        title_label.setFont(QFont('Times New Roman', 14))
        title_label.setStyleSheet(f'color: {text_color}; font-weight: bold;')
        info_layout.addWidget(title_label)

        description_label = QLabel(f"Описание товара: {product.get('description', 'Без описания')}")
        description_label.setFont(QFont('Times New Roman', 12))
        description_label.setStyleSheet(f'color: {text_color};')
        description_label.setWordWrap(True)
        info_layout.addWidget(description_label)

        manufacturer_label = QLabel(f"Производитель: {product.get('manufacturer_name', 'Не указан')}")
        manufacturer_label.setFont(QFont('Times New Roman', 12))
        manufacturer_label.setStyleSheet(f'color: {text_color};')
        info_layout.addWidget(manufacturer_label)

        provider_label = QLabel(f"Поставщик: {product.get('provider_name', 'Не указан')}")
        provider_label.setFont(QFont('Times New Roman', 12))
        provider_label.setStyleSheet(f'color: {text_color};')
        info_layout.addWidget(provider_label)

        price = product.get('price')

        if discount > 0:
            old_price_label = QLabel(f"Цена: {round(price, 2)} руб.")
            old_price_label.setFont(QFont('Times New Roman', 12))
            old_price_label.setStyleSheet(f'color: red; text-decoration: line-through;')
            info_layout.addWidget(old_price_label)

            final_price = float(price) * (1 - float(discount) / 100)

            new_price_label = QLabel(f"Цена со скидкой: {round(final_price, 2)} руб.")
            new_price_label.setFont(QFont('Times New Roman', 12))
            new_price_label.setStyleSheet(f'color: {text_color};')
            info_layout.addWidget(new_price_label)
        else:
            price_label = QLabel(f"Цена: {round(price, 2)} руб.")
            price_label.setFont(QFont('Times New Roman', 12))
            price_label.setStyleSheet(f'color: {text_color};')
            info_layout.addWidget(price_label)

        unit_label = QLabel(f"Единица измерения: {product.get('unit', 'шт.')}")
        unit_label.setFont(QFont('Times New Roman', 12))
        unit_label.setStyleSheet(f'color: {text_color};')
        info_layout.addWidget(unit_label)

        stock_label = QLabel(f"Количество на складе: {stock} {product.get('unit', 'шт.')}")
        stock_label.setFont(QFont('Times New Roman', 12))
        stock_label.setStyleSheet(f'color: {text_color};')
        info_layout.addWidget(stock_label)

        layout.addWidget(info_frame, 1)

        discount_frame = QFrame()
        discount_frame.setFixedSize(150, 180)
        discount_frame.setStyleSheet('border: none;')

        discount_layout = QVBoxLayout(discount_frame)
        discount_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        discount_label = QLabel(f"Действующая\nскидка")
        discount_label.setFont(QFont('Times New Roman', 12))
        discount_label.setStyleSheet(f'color: {text_color};')
        discount_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        discount_label.setWordWrap(True)
        discount_layout.addWidget(discount_label)

        discount_value_label = QLabel(f"{discount} %")
        discount_value_label.setFont(QFont('Times New Roman', 12))
        discount_value_label.setStyleSheet(f'color: {text_color};')
        discount_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        discount_layout.addWidget(discount_value_label)

        layout.addWidget(discount_frame)

        if self.is_admin:
            button_frame = QFrame()
            button_frame.setFixedSize(150, 180)

            button_layout = QVBoxLayout(button_frame)
            button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            ed_button = QPushButton(f"Редактировать")
            ed_button.setFont(QFont('Times New Roman', 12))
            ed_button.setStyleSheet(f'color: black;')
            ed_button.setProperty('product_id', product.get('id'))
            ed_button.clicked.connect(self.plug)
            button_layout.addWidget(ed_button)

            del_button = QPushButton(f"Удалить")
            del_button.setFont(QFont('Times New Roman', 12))
            del_button.setStyleSheet(f'color: white; background-color: red')
            del_button.setProperty('product_id', product.get('id'))
            del_button.clicked.connect(self.plug)
            button_layout.addWidget(del_button)

            layout.addWidget(button_frame)

        return card

    def render_products(self, products):
        while self.ProductsLayout.count():
            item = self.ProductsLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for product in products:
            card = self.create_product_card(product)
            self.ProductsLayout.addWidget(card)

    # загрузка поставщиков
    def load_providers(self):
        providers = set()
        for product in self.all_products:
            provider = product.get('provider_name')
            if provider:
                providers.add(provider)

        self.comboBox.blockSignals(True)
        self.comboBox.clear()
        self.comboBox.addItem("Все поставщики")
        self.comboBox.addItems(providers)
        self.comboBox.setCurrentText("Все поставщики")
        self.comboBox.blockSignals(False)

    # загрузка товаров
    def load_products(self):
        self.all_products = self.db.get_all_products()
        self.load_providers()
        self.apply_filters()

    # выход на окно авторизации
    def logout(self):
        reply = QMessageBox.question(
            self,
            'Выход из системы',
            'Вы действительно хотите выйти?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.hide()
            self.auth_window.show_auth_window()

    # заглушка
    def plug(self):
        QMessageBox.warning(self, 'Внимание', 'Функция в разработке')

    # создание карточки заказа
    def create_order_card(self, order):
        card = QFrame()
        card.setStyleSheet('''
            QFrame {
                border: 1px solid #00FA9A;
            }
        ''')

        text_color = "#000000"

        layout = QHBoxLayout(card)

        info_frame = QFrame()
        info_frame.setStyleSheet('border: none;')

        info_layout = QVBoxLayout(info_frame)

        title_label = QLabel(f"Артикул заказа: {order.get('receipt_code', 'Без артикула')}")
        title_label.setFont(QFont('Times New Roman', 14))
        title_label.setStyleSheet(f'color: {text_color}; font-weight: bold;')
        info_layout.addWidget(title_label)

        status_label = QLabel(f"Статус заказа: {order.get('status_name', 'Новый')}")
        status_label.setFont(QFont('Times New Roman', 12))
        status_label.setStyleSheet(f'color: {text_color};')
        info_layout.addWidget(status_label)

        address_label = QLabel(f"Адрес пункта выдачи: г. {order.get('city', 'Не указан')}, ул. {order.get('street', 'Не указана')}, д. {order.get('house', 'Не указан')}")
        address_label.setFont(QFont('Times New Roman', 12))
        address_label.setStyleSheet(f'color: {text_color};')
        address_label.setWordWrap(True)
        info_layout.addWidget(address_label)

        order_date_label = QLabel(f"Дата заказа: {order.get('order_date', 'Не указана')}")
        order_date_label.setFont(QFont('Times New Roman', 12))
        order_date_label.setStyleSheet(f'color: {text_color};')
        info_layout.addWidget(order_date_label)

        layout.addWidget(info_frame, 1)

        delivery_frame = QFrame()
        delivery_frame.setFixedSize(150, 180)
        delivery_frame.setStyleSheet('border: none;')

        delivery_layout = QVBoxLayout(delivery_frame)
        delivery_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        delivery_label = QLabel(f"Дата доставки")
        delivery_label.setFont(QFont('Times New Roman', 12))
        delivery_label.setStyleSheet(f'color: {text_color};')
        delivery_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        delivery_layout.addWidget(delivery_label)

        delivery_date_label = QLabel(f"{order.get('delivery_date', 'Не указана')}")
        delivery_date_label.setFont(QFont('Times New Roman', 12))
        delivery_date_label.setStyleSheet(f'color: {text_color};')
        delivery_date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        delivery_layout.addWidget(delivery_date_label)

        layout.addWidget(delivery_frame)

        if self.is_admin:
            button_frame = QFrame()
            button_frame.setFixedSize(150, 180)

            button_layout = QVBoxLayout(button_frame)
            button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            ed_button = QPushButton(f"Редактировать")
            ed_button.setFont(QFont('Times New Roman', 12))
            ed_button.setStyleSheet(f'color: black;')
            ed_button.setProperty('order_id', order.get('id'))
            ed_button.clicked.connect(self.plug)
            button_layout.addWidget(ed_button)

            del_button = QPushButton(f"Удалить")
            del_button.setFont(QFont('Times New Roman', 12))
            del_button.setStyleSheet(f'color: white; background-color: red')
            del_button.setProperty('order_id', order.get('id'))
            del_button.clicked.connect(self.plug)
            button_layout.addWidget(del_button)

            layout.addWidget(button_frame)

        return card

    # загрузка заказов
    def load_orders(self):
        orders = self.db.get_all_orders()

        while self.OrdersLayout.count():
            item = self.OrdersLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for order in orders:
            card = self.create_order_card(order)
            self.OrdersLayout.addWidget(card)