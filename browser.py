from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.view = QWebEngineView(self)
        self.setWindowTitle("CodeComets Browser")
        self.view.load(QUrl("https://www.google.com"))

        self.view.titleChanged.connect(self.update_title)
        self.view.iconChanged.connect(self.update_icon)

        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

    def update_title(self, title):
        self.setWindowTitle(title)
        
    def update_icon(self, icon):
        self.setWindowIcon(icon)

if __name__ == "__main__":
    app = QApplication([])
    browser = Browser()
    browser.setGeometry(50, 50, 850, 500)
    browser.show()
    app.exec_()
