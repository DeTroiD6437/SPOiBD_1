import os 
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройки графического интерфейса приложения."""
        self.setGeometry(50, 50, 400, 700)
        self.setWindowTitle("Резюме")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        """Открывает файлы изображений и создаёт метки изображений."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(script_dir, "images")
        
        background_path = os.path.join(images_dir, "fon.webp")
        try:
            with open(background_path):
                label = QLabel(self)
                pixmap = QPixmap(background_path)
                scaled_pixmap = pixmap.scaled(400, 150, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
                label.setPixmap(scaled_pixmap)
                label.resize(400, 150)
        except FileNotFoundError as error:
            print(f"Background image not found.\nError: {error}")
        
        profile_path = os.path.join(images_dir, "profile_image.jpg")
        try:
            with open(profile_path):
                label = QLabel(self)
                pixmap = QPixmap(profile_path)
                scaled_pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
                label.setPixmap(scaled_pixmap)
                label.move(150, 100)
                label.resize(100, 100)
        except FileNotFoundError as error:
            print(f"Profile image not found.\nError: {error}")

    def setUpMainWindow(self):
        """Создайте метки, которые будут отображаться в окне."""
        self.createImageLabels()
        
        name_label = QLabel(self)
        name_label.setText("Кувшинов Максим")
        name_label.setFont(QFont("Times New Roman", 16, QFont.Weight.Bold))
        name_label.move(100, 210)
        name_label.resize(250, 30)
        
        position_label = QLabel(self)
        position_label.setText("Full-Stack Разработчик")
        position_label.setFont(QFont("Arial", 12))
        position_label.move(120, 240)
        position_label.resize(200, 30)
        contacts_label = QLabel(self)
        contacts_label.setText("Контакты")
        contacts_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        contacts_label.move(20, 280)
        
        email_label = QLabel(self)
        email_label.setText("maxim.kuvshinov@email.com")
        email_label.move(20, 305)
        
        phone_label = QLabel(self)
        phone_label.setText("+7 (999) 123-45-67")
        phone_label.move(20, 325)
        
        location_label = QLabel(self)
        location_label.setText("Москва, Россия")
        location_label.move(20, 345)
        
        github_label = QLabel(self)
        github_label.setText("github.com/maxinkuvshinov")
        github_label.move(20, 365)

        skills_label = QLabel(self)
        skills_label.setText("Навыки")
        skills_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        skills_label.move(20, 395)
        
        skills_list_label = QLabel(self)
        skills_list_label.setText("Python (Django, Flask)\nJavaScript (React, Node.js)\nPHP (Laravel)\nSQL (PostgreSQL, MySQL)")
        skills_list_label.move(20, 420)
        skills_list_label.resize(350, 80)

        experience_label = QLabel(self)
        experience_label.setText("Опыт работы")
        experience_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        experience_label.move(20, 510)
        
        senior_position_label = QLabel(self)
        senior_position_label.setText("Senior Python Developer")
        senior_position_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        senior_position_label.move(20, 535)
        
        senior_company_label = QLabel(self)
        senior_company_label.setText("TechSolutions Inc.")
        senior_company_label.move(20, 555)
        
        senior_dates_label = QLabel(self)
        senior_dates_label.setText("Январь 2023 – настоящее время")
        senior_dates_label.setFont(QFont("Arial", 9))
        senior_dates_label.move(20, 575)
        
        fullstack_position_label = QLabel(self)
        fullstack_position_label.setText("Full-Stack Developer")
        fullstack_position_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        fullstack_position_label.move(20, 595)
        
        fullstack_company_label = QLabel(self)
        fullstack_company_label.setText("DigitalAgency Pro")
        fullstack_company_label.move(20, 615)
        
        fullstack_dates_label = QLabel(self)
        fullstack_dates_label.setText("Март 2020 – Декабрь 2022")
        fullstack_dates_label.setFont(QFont("Arial", 9))
        fullstack_dates_label.move(20, 635)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())