from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
import sys

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def is_odd(n):
    return n % 2 != 0

def main():
    app = QApplication(sys.argv)
    ex = NumberChecker()
    sys.exit(app.exec_())

class NumberChecker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Number Checker')

        self.label = QLabel("Enter a number between 0 and 1,000,000:", self)
        self.textbox = QLineEdit(self)
        self.button = QPushButton('Check', self)
        self.result_label = QLabel("", self)
        self.factors_label = QLabel("", self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.factors_label)

        self.setLayout(vbox)

        self.button.clicked.connect(self.check_number)

        self.show()

    def check_number(self):
        num = int(self.textbox.text())
        if is_prime(num):
            self.result_label.setText(f"{num} (عدد اول است )")
        else:
            self.result_label.setText(f"{num} is a composite number.")
        factors_str = ', '.join(map(str, factors(num)))
        self.factors_label.setText(f"<font color='blue'>Factors of {num}: {factors_str}</font>")

if __name__ == '__main__':
    main()
