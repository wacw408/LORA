import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(1000, 600)
        
        self.back_btn = QPushButton(self)
        self.forward_btn = QPushButton(self)
        self.refresh_btn = QPushButton(self)
        
        self.browser = QWebEngineView()
        
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        
        self.layout_init()
        self.btn_init()
        self.browser_init()
    
    def layout_init(self):
        self.h_layout.setSpacing(0)
        self.h_layout.addWidget(self.back_btn)
        self.h_layout.addWidget(self.forward_btn)
        self.h_layout.addWidget(self.refresh_btn)
        self.h_layout.addStretch(2)
        
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.browser)
        
        self.setLayout(self.v_layout)

    def browser_init(self):
        self.browser.load(QUrl("file:///Users/sephiros/Desktop/program/visualization.html"))

    def btn_init(self):
        self.back_btn.setIcon(QIcon('/Users/sephiros/Desktop/program/back.png'))
        self.forward_btn.setIcon(QIcon('/Users/sephiros/Desktop/program/forward.png'))
        self.refresh_btn.setIcon(QIcon('/Users/sephiros/Desktop/program/reload.png'))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.refresh_btn.clicked.connect(self.browser.reload)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())



