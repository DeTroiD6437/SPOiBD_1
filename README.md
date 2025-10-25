# 📄 Резюме - Приложение для отображения профиля

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![PyQt6](https://img.shields.io/badge/PyQt6-GUI%20Framework-green)
![Desktop](https://img.shields.io/badge/Desktop-Application-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Десктопное приложение для профессионального отображения резюме с поддержкой изображений, разработанное на PyQt6.

## 🖼️ Интерфейс приложения

Приложение отображает:
- Фотографию профиля и фоновое изображение
- Контактную информацию
- Навыки и технологии
- Опыт работы с хронологией

## 🚀 Быстрый старт

### Требования

- **Python** 3.6 или выше
- **PyQt6** - для графического интерфейса

### Установка


### Установка PyQt6
```bash
pip install PyQt6
```
### Запуск приложения
```bash
python user_profile.py
```
### Структура проекта
```
resume-app/
├── 📁 image/                   # Папка с изображениями
│   ├── fon.webp               # Фоновое изображение
│   └── profile_image.jpg      # Фото профиля
├── 📄 user_profile.py         # Основной файл приложения
└── 📄 README.md              # Документация
```
### 🛠️ Технологический стек

### 🏗️ **PyQt6.QtWidgets** - Компоненты интерфейса

| Компонент | Назначение | Использование в коде |
|---|---|---|
| `QApplication` | Управление приложением | `app = QApplication(sys.argv)` |
| `QWidget` | Основное окно | `class MainWindow(QWidget)` |
| `QLabel` | Текст и изображения | `name_label = QLabel(self)` |

### 🎨 **PyQt6.QtGui** - Графика и оформление

| Компонент | Назначение | Использование |
|---|---|---|
| `QFont` | Стилизация текста | `setFont(QFont("Arial", 16, QFont.Weight.Bold))` |
| `QPixmap` | Работа с изображениями | `pixmap = QPixmap(image_path)` |
| `scaled()` | Масштабирование изображений | `pixmap.scaled(100, 100)` |

### 🔧 **Системные библиотеки Python**

| Библиотека | Назначение | Ключевые функции |
|---|---|---|
| `os` | Работа с путями | `os.path.join(), os.path.dirname()` |
| `sys` | Системные функции | `sys.argv, sys.exit()` |

### 🌐 **PyQt6.QtCore** - Основные функции Qt

| Компонент | Назначение | Использование |
|---|---|---|
| `Qt.AspectRatioMode` | Режимы масштабирования | `KeepAspectRatio, KeepAspectRatioByExpanding` |

### 💻 **Основная функциональность**

### 🎯 Класс MainWindow - Главное окно приложения

```
def initializeUI(self):
    """Инициализация пользовательского интерфейса"""
    self.setGeometry(50, 50, 400, 600)  # Размер и позиция окна
    self.setWindowTitle("Резюме - Кувшинов Максим")
```
```
def createImageLabels(self):
    """Загрузка и обработка изображений"""
    # Автоматическое определение путей к изображениям
    # Обработка ошибок FileNotFoundError
    # Интеллектуальное масштабирование с сохранением пропорций
```
```
def setUpMainWindow(self):
    """Создание и компоновка элементов интерфейса"""
    # Динамическое создание меток
    # Позиционирование элементов
    # Настройка шрифтов и стилей
```
### Обработка ошибок
```
try:
    with open(image_path):
        # Загрузка изображения
except FileNotFoundError as error:
    print(f"Image not
```










