from PyQt6.QtGui import QPixmap, QColor, QFont
from PyQt6.QtWidgets import QWidget, QFrame, QHBoxLayout, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from client import Ui_Form
import os

# класс окна клиента / гостя
class ClientWindow(QWidget, Ui_Form):
    def __init__(self, user_data, full_name, db, auth_window):
        super().__init__()
        self.setupUi(self)

        self.user_data = user_data
        self.full_name = full_name
        self.db = db
        self.auth_window = auth_window

        if self.user_data is not None:
            self.label_2.setText(f"{full_name} | Клиент")
        else:
            self.label_2.setText(f"{full_name} | Гость")

        self.pushButton.clicked.connect(self.logout)

        self.load_products()

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

        return card

    # загрузка товаров
    def load_products(self):
        products = self.db.get_all_products()

        while self.ProductsLayout.count():
            item = self.ProductsLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for product in products:
            card = self.create_product_card(product)
            self.ProductsLayout.addWidget(card)

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