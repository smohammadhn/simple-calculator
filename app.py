import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Plus Minus Calculator")
        self.setGeometry(100, 100, 300, 260)
        
        # Always on top flag
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        
        # Force dark background always
        self.setStyleSheet("background-color: #2b2b2b;")
        
        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(15, 12, 15, 15)  # left, top, right, bottom
        
        # Label
        label = QLabel("Enter a number:")
        label.setFont(QFont("Arial", 12, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white;")
        layout.addWidget(label)
        
        # Input fields layout (3fr main, 1fr increment)
        inputs_layout = QHBoxLayout()
        inputs_layout.setSpacing(8)
        
        # Main input field
        self.entry = QLineEdit()
        self.entry.setFont(QFont("Arial", 14))
        self.entry.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #4a90e2;
                border-radius: 4px;
                background-color: white;
                color: black;
            }
        """)
        self.entry.setAlignment(Qt.AlignCenter)
        self.entry.returnPressed.connect(self.calculate)
        inputs_layout.addWidget(self.entry, 3)  # 3fr
        
        # Increment input field (smaller)
        self.increment_entry = QLineEdit("5")
        self.increment_entry.setFont(QFont("Arial", 14))
        self.increment_entry.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #95a5a6;
                border-radius: 4px;
                background-color: white;
                color: black;
            }
        """)
        self.increment_entry.setAlignment(Qt.AlignCenter)
        self.increment_entry.returnPressed.connect(self.calculate)
        inputs_layout.addWidget(self.increment_entry, 1)  # 1fr
        
        layout.addLayout(inputs_layout)
        
        # Buttons layout (2fr Calculate, 1fr Clear)
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(8)
        
        # Calculate button
        calc_btn = QPushButton("Calculate")
        calc_btn.setFont(QFont("Arial", 11, QFont.Bold))
        calc_btn.setStyleSheet("""
            QPushButton {
                padding: 10px;
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #357abd;
            }
        """)
        calc_btn.clicked.connect(self.calculate)
        buttons_layout.addWidget(calc_btn, 2)  # 2fr
        
        # Clear button
        clear_btn = QPushButton("Clear")
        clear_btn.setFont(QFont("Arial", 10, QFont.Bold))
        clear_btn.setStyleSheet("""
            QPushButton {
                padding: 10px;
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        clear_btn.clicked.connect(self.clear_fields)
        buttons_layout.addWidget(clear_btn, 1)  # 1fr
        
        layout.addLayout(buttons_layout)
        
        # Result label
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
        self.entry.setFocus()
    
    def keyPressEvent(self, event):
        # Esc key clears the input field
        if event.key() == Qt.Key_Escape:
            self.entry.clear()
            self.result_label.setText("")
        else:
            super().keyPressEvent(event)
    
    def calculate(self):
        try:
            num = float(self.entry.text())
            increment = float(self.increment_entry.text())
            plus = num + increment
            minus = num - increment
            self.result_label.setText(f"+{increment} = {plus}     -{increment} = {minus}")
        except ValueError:
            QMessageBox.critical(self, "Invalid input", "Please enter valid numbers")
    
    def clear_fields(self):
        self.entry.clear()
        self.result_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
